import json
import os

json_file = open('folders.json')

data = json.load(json_file)

os.rename(data['folder2'], data['temp'])
os.rename(data['folder1'], data['folder2'])
os.rename(data['temp'], data['folder1'])

print('changed names successfully')
