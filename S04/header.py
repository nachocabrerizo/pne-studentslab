from pathlib import Path

from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

# -- Constant with the new of the file to open
FILENAME = "sequences/RNU6_269P.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

lines = file_contents.split("\n")

print(lines[0])
