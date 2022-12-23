

cursor.execute("CREATE TABLE Movie (id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "title varchar(250) NOT NULL UNIQUE,"
               "year INTEGER NOT NULL,"
               "description varchar NOT NULL,"
               "rating FLOAT NOT NULL,"
               "ranking INTEGER NOT NULL,"
               "review varchar NOT NULL,"
               "img_url varchar NOT NULL"
               ")")

cursor.execute("INSERT INTO Movie VALUES(NULL,'Phone Booth', '2002', 'some bullshit','7.3','10','yep','img-link')")
a = cursor.execute("SELECT title FROM Movie")
print(a.fetchall()[0][0])