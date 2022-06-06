# Project: Data Modeling with Postgres 

This project is part of the Udacity Data Engineering Nanodegree program. 

## Introduction  and Description 

A startup called Sparkify in analyzing their data (songs and user activity stored as JSON files). Sparkify is interested in analyzing what songs users are listening to. 
The dataset for the project as mentioned above is stored in JSON files. There information is stored in 2 files, song and log files. Song file will contain information about the song and the log file will contain the information about the user access log information.
For this project, I will play the role data engineer and be creating a Postgres DB with tables to facilitate the song play data analysis. Here are the specific goals of the project: 
* Create a database schema and ETL pipeline for the analysis 
   * Please refer to the following link,http://github.com/kenhanscombe/project-postgres/blob/master/README.md, for a ER diagram 
```
(Details about Fact/Dimension tables were obtained from Udacity class instructions)

## Fact Table
* songplays - records in log data associated with song plays i.e. records with page NextSong
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

## Dimension Tables
2) users - users in the app
	* user_id, first_name, last_name, gender, level
3) songs - songs in music database
	* song_id, title, artist_id, year, duration
4) artists - artists in music database
	* artist_id, name, location, latitude, longitude
5) time - timestamps of records in songplays broken down into specific units
	* start_time, hour, day, week, month, year, weekday
```

* Define FACT and DIMENSION tables for a STAR schema for the analysis 
* Test the DB and ETL 
* Compare my results with the expected results.


## Database Schema Deign and ETL pipeline

*  Identify the  FACT (songplays) and 4 Dimension (users, time, songs, artists) tables.
*  Use postgres to create the database 
*  Use Python code to create, add and modify the database 
*  Test the changes 
*  Carry out the analysis to compare the results

## Sample code results

Here is a sample code that extracts data from songplays table, only for the rows for that 
the song_id and artist_id are not NULL

```
%sql SELECT * FROM songplays where song_id is not null and artist_id is not null;
```

## Acknowledgements:
* Udacity 
