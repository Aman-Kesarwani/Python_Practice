import sqlite3
import json
from pathlib import Path

movies = json.loads(
    Path(r"D:\Workspace\Python_Practice\Python_Practice\movies.json").read_text())
print(type(movies))

print(movies)

with sqlite3.connect("db.sqlite3") as conn:
    command = "INSERT INTO Movies VALUES(?, ?, ?)"
    for movie in movies:
        conn.execute(command, tuple(movie.values()))
    conn.commit()

with sqlite3.connect("db.sqlite3") as conn:
    command = "select * from movies"
    cursor = conn.execute(command)

    for row in cursor:
        print(row)

movie_list = cursor.fetchall()
print(movie_list)  # fecchall fetch in one go..comment cursor traverse
