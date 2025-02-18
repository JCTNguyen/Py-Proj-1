import csv 

#Define CSV filename
csv_filename = "leashes.csv"

#sample Leash data
leash_data = [
    ["Type", "Color", "Length"],
    ["CBA","Blue","8ft"],
    ["PWW", "Red", "6ft"],
]

#Data for CSV file
with open(csv_filename, mode='w', newline="") as file:
    writer = csv.writer(file)
    writer.writerows(leash_data)
    
print(" CSV file created successfully!")