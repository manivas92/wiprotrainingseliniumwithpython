import csv

with open("C:\Users\maniv\PycharmProjects\Python advanced programming\dataformats\data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)