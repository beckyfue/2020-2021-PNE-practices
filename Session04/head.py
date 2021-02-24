from pathlib import Path
FILENAME = "../P0/sequences/RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()
line = file_contents.split("\n")
print(line[0])
