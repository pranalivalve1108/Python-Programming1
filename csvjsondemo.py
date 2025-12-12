#Create/Write JSON file
''' import json
data = {"name": "Pranali", "age":24}
with open("F:\\Python_Practice\\Python_Practice_Project\\output.json","w") as file:
    json.dump(data, file, indent=4)

#Read JSON file
with open("F:\\Python_Practice\\Python_Practice_Project\\output.json","r") as file:
    data = json.load(file)
    print(data)


#Create/Write CSV file
import csv
with open("F:\\Python_Practice\\Python_Practice_Project\\output.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Pranali', 23])
    writer.writerow(['Swara', 25])

import csv
rows = [
    ['Name', 'Education'],
    ['Pranali', 'Computer Engi.'],
    ['Swara', 'Electrical Engi.']
]
with open("F:\\Python_Practice\\Python_Practice_Project\\output.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(rows)


#Using Dictionary
import csv
data = [
    {'Name': 'Pranali', 'Age': 23},
    {'Name': 'Prashant', 'Age': 28}
]
with open("F:\\Python_Practice\\Python_Practice_Project\\output.csv", "w") as file:
    fieldnames = ['Name', 'Age']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

#Read CSV file
import csv
with open('F:\\Python_Practice\\Python_Practice_Project\\output.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Name'], row['Age']) '''




#Convert CSV into JSON file
import csv, json
with open("F:\\Python_Practice\\Python_Practice_Project\\output.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

with open("F:\\Python_Practice\\Python_Practice_Project\\converted.json", "w") as jsonfile:
    json.dump(rows,jsonfile,indent=4)









