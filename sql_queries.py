# DROP TABLES

songplay_table_drop = "Drop table if exists songplays"
user_table_drop = "Drop table if exists users"
song_table_drop = "Drop table if exists songs"
artist_table_drop = "Drop table if exists artists"
time_table_drop = "Drop table if exists time"


# CREATE TABLES
songplay_table_create = ("""Create table if not exists songplays
                            (
                            songplay_id serial primary key, 
                            start_time timestamp not null, 
                            user_id int not null, 
                            level varchar, 
                            song_id varchar, 
                            artist_id varchar, 
                            session_id int , 
                            location varchar, 
                            user_agent varchar
                            )
                        """)


user_table_create = ("""Create table if not exists users
                        (
                        user_id int not null, 
                        first_name varchar, 
                        last_name varchar, 
                        gender varchar, 
                        level varchar
                        )
                    """)


song_table_create = ("""Create table if not exists songs 
                        (
                        song_id varchar not null, 
                        title varchar, 
                        artist_id varchar not null, 
                        year int, 
                        duration float
                        )
                    """)



artist_table_create = ("""Create table if not exists artists 
                        (
                        artist_id varchar not null, 
                        name varchar, 
                        location varchar, 
                        latitude varchar, 
                        longitude varchar
                        )
                    """)


time_table_create = ("""Create table if not exists time 
                        (
                        start_time timestamp not null,
                        hour varchar, 
                        day varchar, 
                        week varchar, 
                        month varchar, 
                        year varchar , 
                        weekday varchar
                        )
                    """)


# INSERT RECORDS
songplay_table_insert = (""" Insert into songplays (start_time , user_id , level , song_id , artist_id , session_id , location , user_agent) 
VALUES (%s, %s, %s,%s, %s,%s,%s, %s)
""")

user_table_insert = (""" Insert into users (user_id , first_name , last_name , gender , level ) 
VALUES (%s, %s, %s,%s, %s)
""")

song_table_insert = ("""Insert into songs (song_id , title , artist_id , year , duration) 
VALUES (%s, %s, %s,%s, %s)
""")

artist_table_insert = (""" Insert into artists (artist_id , name , location , latitude , longitude) 
VALUES (%s, %s, %s,%s, %s)
""")

time_table_insert = ("""Insert into time (start_time,hour , day , week , month , year , weekday) 
VALUES (%s, %s, %s, %s, %s, %s, %s)
""")



# FIND SONGS
song_select = ("""
SELECT songs.song_id, artists.artist_id
FROM songs JOIN artists ON songs.artist_id=artists.artist_id
WHERE songs.title = %s AND artists.name = %s and songs.duration = %s
""")

# QUERY LISTS (2018-11-27 17:28:50.796)

create_table_queries = [user_table_create, artist_table_create, time_table_create,song_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]