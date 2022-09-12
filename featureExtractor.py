import csv

data = []
with open('01a-Mon.csv', 'r') as f:
    csvFile = csv.reader(f)
    # File Data Label
    label = next(csvFile)
    # File Data
    for row in csvFile:
        data.append(row)

f.close()

print(label)
print(data[1])


