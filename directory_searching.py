from pathlib import Path

path = Path("ecommerce_1")

print(path.iterdir())

for p in path.iterdir():
    print(p)

path_list = [p for p in path.iterdir()]
print(path_list)

path_list_dir = [p for p in path.iterdir() if p.is_dir()]
print(path_list_dir)

# search using filtering
py_files = [p for p in path.glob("*.py")]
print(py_files)

# search recursively directoy with in director

py_files_rec = [p for p in path.glob("**/*.py")]
print(py_files_rec)

py_files_rec_1 = [p for p in path.rglob("*.py")]
print(py_files_rec_1)
