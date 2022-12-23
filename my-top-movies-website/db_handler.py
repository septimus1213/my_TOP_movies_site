import sqlite3

# ---- DATABASE SECTION -------- #
def GetData():
    db = sqlite3.connect("movies.db")
    cursor = db.cursor()
    lst = []
    for movie in cursor.execute("SELECT title, year, description, rating, ranking, review, img_url, id FROM Movie ORDER BY rating"):
        lst.append(list(movie))
    return lst

def WriteData(title,year,descr,rating,ranking,review,img_url):
    db = sqlite3.connect("movies.db")
    cursor = db.cursor()
    # row order: id, title, year, description, rating, ranking, review, img_url
    cursor.execute(f""" INSERT INTO Movie VALUES(NULL,?,?,?,?,?,?,?)""",(title,year,descr,rating,ranking,review,img_url))
    db.commit()
    
    # return the id of fresh row
    row_id = cursor.execute(f"""SELECT id FROM Movie WHERE title = ?; """,(title,))
    return row_id.fetchone()[0]


def UpdateData(id,new_rating,new_review):
    db = sqlite3.connect("movies.db")
    cursor = db.cursor()
    cursor.execute(f"""  UPDATE Movie
                        SET rating = ?,
                        review = ?
                        WHERE id = ?; """, (new_rating,new_review,id))
    db.commit()

def RemoveData(id):
    db = sqlite3.connect("movies.db")
    cursor = db.cursor()
    cursor.execute(f""" DELETE FROM Movie WHERE id= ?""", (id,))
    db.commit()
# ------------------------------ #