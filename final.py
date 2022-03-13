import csv
dataset_1 = []
dataset_2 = []
with open('dataset_1.csv' , 'r') as f:
    csvReader= csv.reader(f)
    for row in csvReader:
        dataset_1.append(row)
with open('dataset_2_sorted.csv' , 'r') as f:
    csvReader= csv.reader(f)
    for row in csvReader:
        dataset_2.append(row)
headers_1 = dataset_1[0]
headers_2 = dataset_2[0]
headers = headers_1+headers_2
planet_data_1 = dataset_1[1:]
planet_data_2 = dataset_2[1:]
planet_data = []
for index , data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index]+planet_data_2[index])

with open('final.csv','a+') as f:
    csvWriter= csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)


