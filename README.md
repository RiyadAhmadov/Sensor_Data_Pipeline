# Sensor_Data_Pipeline

![SensorProject](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWRBtASfdRwswbNwtojVsRKD8SQT9O-KJKFw&usqp=CAU)

## Sensor data in real time

## Overview
Let's get a brief overview of the project. The project is to create information in real time and display it in power bi dashboards after passing through certain stages. This data is sensor data, and this data contains soil and weather data.

## Prerequisites
Let's look at the prerequisites that the project must install or have before using it:

*Python*
*Postgre SQL*
*Power BI*

## Data Generation

The first and main process is the generation of data. In this step, we first look at the characteristics of the data we will create. We research the features and select the price ranges that suit them. For example: Temperature (0.40). You can see this process in more detail in the py file.

## Air Sensors

![AirProject](https://grist.org/wp-content/uploads/2022/06/GettyImages-1241061959.jpg)

## Sand Sensors

![SandProject](https://www.mdpi.com/sensors/sensors-18-00820/article_deploy/html/images/sensors-18-00820-g009.png)

## Database Setup

As a second step, we connect to the postgre sql server in python and create 2 tables in database A. We define relevant features in this table. Then we send the values of these features to the database. This process is possible with a simple query. Since the process works in real time, it sends new data to database A every 10 seconds (conditionally).

## DBLink Creation:
In this part I am setting up dblink. I use dblink to connect the databases to each other. This method helps me to send data from one database to another. I combine the 2 tables in the first database and send them to the second database B. I achieve this process by typing dblink extension.

## Power BI Integration
In the last step, we visualize our data in Power BI. First, we pull data from database B with Power bi. Then we activate the page refresh part. We activate the 'page refresh' section to be in real time. It automatically refreshes the page every 10 seconds and our dashboard is updated for real time date.

## Database & Tables

## Database:
## 1) soil_sensor

id: Unique identifier for each record
soil_moisture_content: Measure of soil moisture
soil_pH_levels: Measure of soil pH levels
soil_temperature: Measure of soil temperature
soil_nutrient_levels: Measure of soil nutrient levels

## 2) weather_sensor

id: Unique identifier for each record
temperature: Temperature measurement
wind_speed: Wind speed measurement
humidity: Humidity measurement
wind_direction: Wind direction measurement
solar_radiation: Solar radiation measurement

## Database B:
## 1) Raw-data

sensor_id: Unique identifier for each record
soil_moisture_content: Measure of soil moisture
soil_pH_levels: Measure of soil pH levels
soil_temperature: Measure of soil temperature
soil_nutrient_levels: Measure of soil nutrient levels
w_temperature: Temperature measurement
wind_speed: Wind speed measurement
w_humidity: Humidity measurement
wind_direction: Wind direction measurement

## Real-Time Processing:

I built this process in realtime. That is, when I run the code, this code will run until we interrupt. The purpose of doing this process in real time is that we can take new measures by instantly receiving information about the data. We may need it in some sectors and businesses. I mentioned these types of business in my presentation, you can read more from there.

## Contact
For questions or feedback regarding this README or project, please contact *Riyad* at **riyadehmedov03@gmail.com**.







