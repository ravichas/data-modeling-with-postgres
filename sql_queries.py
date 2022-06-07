# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS  users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
   CREATE TABLE IF NOT EXISTS songplays ( 
       songplay_id SERIAL PRIMARY KEY, 
       start_time timestamp NOT NULL, 
       user_id int NOT NULL, 
       level varchar, 
       song_id varchar, 
       artist_id varchar,
       session_id int, 
       location varchar, 
       user_agent varchar
    );
""")
 

user_table_create = ("""
   CREATE TABLE IF NOT EXISTS users ( 
       user_id int PRIMARY KEY, 
       first_name varchar, 
       last_name varchar, 
       gender varchar, 
       level varchar
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs ( 
        song_id varchar NOT NULL PRIMARY KEY, 
        title varchar NOT NULL, 
        artist_id varchar NOT NULL, 
        year int NOT NULL,
        duration numeric NOT NULL
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (    
        artist_id varchar(255) NOT NULL PRIMARY KEY, 
        name varchar(255) NOT NULL,
        location varchar,
        latitude float,
        longitude float
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time ( 
        start_time bigint NOT NULL PRIMARY KEY, 
        hour int NOT NULL , 
        day int NOT NULL ,  
        week int NOT NULL , 
        month int NOT NULL , 
        year int NOT NULL, 
        weekday varchar NOT NULL
    );
""")

# INSERT RECORDS

songplay_table_insert = ("""
    insert into songplays ( songplay_id, start_time, user_id, level, song_id, 
                            artist_id, session_id , location, user_agent) 
    values (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

user_table_insert = ("""insert into users ( user_id,  
    first_name, last_name, gender, level) 
    values (%s, %s, %s, %s,%s)
    ON CONFLICT DO NOTHING;
""")

song_table_insert = ("""
    insert into songs ( song_id, title, artist_id, year, duration) 
    VALUES (%s, %s, %s, %s, %s) 
    ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""insert into artists ( artist_id, name, 
    location, latitude, longitude) values (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

time_table_insert = ("""insert into time ( start_time, hour, 
    day, week, month, year, weekday) values (%s, %s, %s, %s,%s, %s, %s) 
    ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""SELECT s.song_id AS song_id, a.artist_id AS artist_id 
FROM ( songs s 
       INNER JOIN artists a ON s.artist_id = a.artist_id) 
       WHERE s.title = %s AND a.name = %s AND s.duration = %s 
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, 
                        song_table_create, artist_table_create, time_table_create]

drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, 
                      artist_table_drop, time_table_drop]
