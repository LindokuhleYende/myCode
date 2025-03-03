from pathlib import Path

path = Path("Learning_Python.txt")
contents = path.read_text()
print(contents)