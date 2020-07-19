from pathlib import Path
from time import ctime
import shutil

path = Path("ecommerce_1/__init__.py")

source = Path("ecommerce_1/__init__.py")
target = Path() / "__init__.py"

shutil.copy(source, target)

target.write_text("Hello you are copited and then written")
# source.write_text(source.read_text())
# print(path.stat())
print(ctime(path.stat().st_ctime))
print(path.read_text())
