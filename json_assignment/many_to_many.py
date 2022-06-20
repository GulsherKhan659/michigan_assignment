def run():
    import json
    from json_assignment.JSON_PARSING import Data
    import sqlite3


    # CONECT DATA BASE
    conn = sqlite3.connect("./json_assignment/db_roster.db")

    # CREATE COURSE TO HANDLE SQLITE FILE
    cur = conn.cursor()

    # executescript run multiple SQL SCRIPT and seperated by ;
    cur.executescript('''
    DROP TABLE IF EXISTS USER;
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Member;
    DROP TABLE IF EXISTS Course;
        
    CREATE TABLE User(   
         id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
         name TEXT UNIQUE
    );
    
    CREATE TABLE Member(
        course_id INTEGER,
        user_id INTEGER,
        role INTEGER,
        PRIMARY KEY (user_id,course_id)
    );
    
    CREATE TABLE Course(
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE
    )
    ''')

    filename = "./json_assignment/roster_data.json"
    file = open(filename).read()
    filej = json.loads(file)

    for detail in filej:
        data = Data(detail)


        cur.execute("INSERT OR IGNORE INTO User(name)VALUES(?)", (data.user,))
        cur.execute("SELECT id from User WHERE name = ?", (data.user,))
        user_id = cur.fetchone()[0]
        cur.execute("INSERT OR IGNORE INTO Course(title) VALUES(?)", (data.course,))
        cur.execute("SELECT id from Course WHERE title = ?", (data.course,))
        course_id = cur.fetchone()[0]
        cur.execute("INSERT OR IGNORE INTO Member (course_id,user_id,role)VALUES(?,?,?)", (course_id, user_id, data.role))
        conn.commit()
