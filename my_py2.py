import psycopg2
import random
import time

# Define your PostgreSQL database connection parameters
host = 'localhost'
database = 'databaseA'
username = 'postgres'
pwd = 'eriya494949'
port = 5432
conn = None
cur = None

database1 = 'databaseB'
conn1 = None
cur1 = None

try:
    conn = psycopg2.connect(
        host=host,
        dbname=database,
        user=username,
        password=pwd,
        port=port
    )
    cur = conn.cursor()
    conn1 = psycopg2.connect(
        host=host,
        dbname=database1,
        user=username,
        password=pwd,
        port=port
    )
    cur1 = conn1.cursor()


    # Let's write query for creating weather_sensor table
    create_wscript = """
CREATE TABLE IF NOT EXISTS weather_sensor (
    id SERIAL PRIMARY KEY,
    temperature FLOAT NOT NULL,
    wind_speed FLOAT NOT NULL,
    humidity FLOAT NOT NULL,
    wind_direction FLOAT NOT NULL,
    solar_radiation FLOAT NOT NULL
);
"""

    # Let's write query for creating soil_sensor table
    create_sscript = """
CREATE TABLE IF NOT EXISTS soil_sensor (
    id SERIAL PRIMARY KEY,
    soil_moisture_content FLOAT NOT NULL,
    soil_pH_levels FLOAT NOT NULL,
    soil_temperature FLOAT NOT NULL,
    soil_nutrient_levels VARCHAR(10) not null
);
"""

    #First, create the dblink extension if not already created
    extentions = "CREATE EXTENSION IF NOT EXISTS dblink;"

    create_scriptB = """ CREATE TABLE IF NOT EXISTS raw_data (
        w_temperature FLOAT NOT NULL,
        wind_speed FLOAT NOT NULL,
        w_humidity FLOAT NOT NULL,
        wind_direction FLOAT NOT NULL,
        solar_radiation FLOAT NOT NULL,
        sensor_id INT PRIMARY KEY,
        soil_moisture_content FLOAT NOT NULL,
        soil_pH_levels FLOAT NOT NULL,
        soil_temperature FLOAT NOT NULL,
        soil_nutrient_levels VARCHAR(10) NOT NULL);
    """

    #Next, establish a connection to databaseB
    connect = """SELECT dblink_connect('myconn1',
    'dbname=databaseA port=5432 host=localhost user=postgres password=eriya494949');
    """


    # Create the tables outside the loop
    cur.execute(create_wscript)
    cur.execute(create_sscript)
    conn.commit()

    cur1.execute(create_scriptB)
    cur1.execute(connect)
    conn1.commit()

    # Let's determine id
    id = 40
    # Create while loop for real-time
    while True:

        cur.execute("SELECT MAX(id) FROM soil_sensor;")
        max_id = cur.fetchone()[0] or 2

        # Insert data into weather_sensor
        insert_wscript = 'INSERT INTO weather_sensor (id, temperature, wind_speed, humidity, wind_direction, solar_radiation) VALUES (%s, %s, %s, %s, %s, %s)'
        temperature = random.uniform(0, 40)
        wind_speed = random.uniform(0, 30)
        humidity = random.randint(30, 80)
        wind_direction = random.uniform(0, 360)
        solar_radiation = random.uniform(0, 2000)
        insert_wvalue = (id, temperature, wind_speed, humidity, wind_direction, solar_radiation)
        cur.execute(insert_wscript, insert_wvalue)

        # Insert data into soil_sensor
        insert_sscript = 'INSERT INTO soil_sensor (id, soil_moisture_content, soil_pH_levels, soil_temperature, soil_nutrient_levels) VALUES (%s, %s, %s, %s, %s)'
        soil_moisture_content = random.uniform(10, 50)
        soil_pH_levels = random.uniform(5.5, 7.0)
        soil_temperature = random.uniform(5, 40)
        nutrient_levels = ['N', 'P', 'K']
        soil_nutrient_levels = random.choice(nutrient_levels)
        insert_svalue = (id, soil_moisture_content,soil_pH_levels,soil_temperature,soil_nutrient_levels)
        cur.execute(insert_sscript,insert_svalue)
        print(max_id)
        conn.commit()

        #Now, you can execute queries on databaseB from databaseA
        add_to_b = f"""insert into raw_data(w_temperature, wind_speed, w_humidity, wind_direction, solar_radiation, sensor_id, soil_moisture_content, soil_pH_levels, soil_temperature, soil_nutrient_levels)
        SELECT *
        FROM dblink('myconn1',
        'SELECT w.temperature, w.wind_speed, w.humidity, w.wind_direction, w.solar_radiation, s.id, s.soil_moisture_content, s.soil_pH_levels, s.soil_temperature, s.soil_nutrient_levels FROM soil_sensor s INNER JOIN weather_sensor w ON s.id = w.id where s.id = {max_id}')
        AS p(temperature FLOAT, wind_speed FLOAT, humidity FLOAT, wind_direction FLOAT, solar_radiation FLOAT, id INT, soil_moisture_content FLOAT, soil_pH_levels FLOAT, soil_temperature FLOAT, soil_nutrient_levels VARCHAR(10));
        """

        conn1.commit()
        cur1.execute(add_to_b)
        id += 1
        time.sleep(1)


except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
    if cur1 is not None:
        cur1.close()
    if conn1 is not None:
        conn1.close()