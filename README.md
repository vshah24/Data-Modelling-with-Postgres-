# Data-Modelling-with-Postgres-

## Overview -
  A startup **Sparkify (music streaming company)** have been collecting data about songs and users activity across their platform. The analytics team wants to analyze and understand what songs users are interested listening to. The data is spread across multiple json files, which makes it hard to query and do the analysis.

  The goal of this project is to create a postgres data model and develop an ETL pipeline that transfers data from local json files to these tables in postgres database making it easier for the analytics team to analyze the data and understand the user behaviour. 
  
  
  
## Project Files - 
  1. **song_data/ and log_data/** - contains song and log files on user activity in json format.
  2. **sql_queries.py** - Contains sql queries that has a creation,insertion and dropping templates of fact and dimension tables.
  3. **create_tables.py** - creates **sparkify** database and tables.
  4. **etl.ipynb** - It's a prototype which inserts data from 1 json file. 
  5. **etl.py** - Defines the ETL pipeline, which pulls data from song and log json files located in the local directory, performing data transformation and inserts them into the Postgres database.
  6. **test.ipynb** - To check if the data is successfully loaded to the Postgres database



## Datasets -
  Currently, we are collecting data for songs and user activities that are stored in two different directories (`song and log`),in json format.
  
  * **Song Dataset** : Song dataset json format
  ```
  {
    "num_songs": 1, 
    "artist_id": "ARJIE2Y1187B994AB7", 
    "artist_latitude": null, 
    "artist_longitude": null, 
    "artist_location": "", 
    "artist_name": "Line Renaud", 
    "song_id": "SOUPIRU12A6D4FA1E1", 
    "title": "Der Kleine Dompfaff", 
    "duration":  152.92036, 
    "year": 0
  }
  ```
  * **Log Dataset** : Log dataset json format
  ```
  {
  "artist": null, 
  "auth": "Logged In", 
  "firstName": "Walter", 
  "gender": "M", 
  "itemInSession": 0, 
  "lastName": "Frye", 
  "length": null, 
  "level": "free", 
  "location": "San Francisco-Oakland-Hayward, CA", 
  "method": "GET",
  "page": "Home", 
  "registration": 1540919166796.0, 
  "sessionId": 38,
  "song": null, 
  "status": 200, 
  "ts": 1541105830796, 
  "userAgent": "\"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"", 
  "userId": "39"
  }
  ```



## Schema - 
#### Fact Tables
1. **Songplays** - records in log data associated with song plays i.e. records with page `Next Song`
  
    ```songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent```

#### Dimension Tables
2. **users** - users in the app

    ```user_id, first_name, last_name, gender, level```
    
3. **songs** - songs in music database

    ```song_id, title, artist_id, year, duration```
    
4. **artists** - artists in music database

   ``` artist_id, name, location, latitude, longitude```
 
5. **time** - timestamps of records in songplays broken down into specific units

    ```start_time, hour, day, week, month, year, weekday```
    
 

## Run Project Locally -
1. To run the project , open the Terminal and enter the following
```
    python sql_queries.py
    python create_tables.py
    python etl.py
 ```
 2. To verify everything was loaded successfully  - ``` Run the test.ipynb file```

