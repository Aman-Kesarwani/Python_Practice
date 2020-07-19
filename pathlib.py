from pathlib import Path

path = Path("ecommerce_1/__init__.py")
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
print(path)
print("abs:", path.absolute())
path = path.with_suffix(".txt")
print(path.absolute())
