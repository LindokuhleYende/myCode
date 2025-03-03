from pathlib import Path


path = Path('lindokuhle.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)
print(contents)