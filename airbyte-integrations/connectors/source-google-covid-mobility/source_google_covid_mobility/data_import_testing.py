import csv, json
from io import StringIO
import requests
url = "https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv"

response = requests.get(url)

data = {}
count = 0
f = StringIO(response.text)
csv_reader = csv.DictReader(f, delimiter=',')
for rows in csv_reader:
    if count > 5:
        break
    id = rows['place_id']
    data[id] = rows
    count += 1

print(data)