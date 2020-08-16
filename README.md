# Data-Modelling-with-Postgres-

#### Overview
A startup **Sparkify (imaginary music streaming company)** have been collecting data about songs and users activity across their platform. The analytics team wants to analyze and understand what songs users are interested listening to. The data is spread across multiple json files, which makes it hard to query and do the analysis.

The goal of this project is to create a postgres data model and develop an ETL pipeline that transfers data from local json files to these tables in postgres database making it easier for the analytics team to analyze the data and understand the user behaviour. 


#### Datasets
Currently, we are collecting data for songs and user activities that are stored in two different directories (`song and log`),in json format.

* Song Dataset : Song dataset json format
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

* Log DataSet : Log dataset json format
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


