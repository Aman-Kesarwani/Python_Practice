import json
from pathlib import Path

movies = [
    {"id": 101, "title": "Harry Potter", "year": 1989},
    {"id": 201, "title": "Terminator", "year": 1993}
]

data = json.dumps(movies)
print(data)
print(type(data))
Path("movies.json").write_text(data)

data_1 = Path("movies.json").read_text()

print(data)
print(type(data))
# parse into array of objects
movies_dict = json.loads(data)
print(movies_dict)
print(type(movies_dict))

print(movies[0]['title'])
