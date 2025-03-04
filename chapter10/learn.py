from pathlib import Path

path = Path("Learning_Python.txt")
contents = path.read_text()
path.write_text(contents)

lines = contents.splitlines()
for line in lines:
    modified_content = contents.replace("python", "C")
    path.write_text(modified_content)
    print(line)
#print(contents)