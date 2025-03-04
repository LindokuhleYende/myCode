from pathlib import Path

path = Path("Learning_Python.txt")
contents = path.read_text()
contents.replace("python", "C")
print(contents)