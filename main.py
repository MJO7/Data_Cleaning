import csv
from email import header
data = []
with open('dataset_2.csv' , 'r') as f:
    csvReader= csv.reader(f)
    for row in csvReader:
        data.append(row)
headers = data[0]
planet_data = data[1:]
for data_point in planet_data:
    data_point[2]=data_point[2].lower()
planet_data.sort(key=lambda planet_data:planet_data[2])
with open('dataset_2_sorted.csv','a+') as f:
    csvWriter= csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)
