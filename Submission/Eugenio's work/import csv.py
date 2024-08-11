import csv
import json

csv_file = 'Resources/storms_final.csv'
json_file = 'Resources/storms_final.js'

data = []
with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data.append(row)

with open(json_file, 'w') as file:
    file.write('const jsonData = ')
    json.dump(data, file, indent=4)