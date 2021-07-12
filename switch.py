import json

file = open('folders.json')

data = json.load(file)

for key, val in data.items():
    print(key)