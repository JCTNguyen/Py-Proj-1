import csv 
csv_filename = "leashes.csv"

with open (csv_filename, mode='r', newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        