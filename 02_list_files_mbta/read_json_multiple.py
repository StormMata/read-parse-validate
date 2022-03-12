import json
import glob

# -----------------------------------
#  use glob
# -----------------------------------

# list all files in data directory

pattern  = './data/*/*.json'

files = []

for file in glob.glob(pattern):
    files.append(file)

for file in files:
    with open(file) as parsed:
        parsed = json.load(file)
        print(parsed)