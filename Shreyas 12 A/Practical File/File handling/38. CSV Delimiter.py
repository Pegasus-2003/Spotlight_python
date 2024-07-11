import csv
with open('csvfile2.csv', 'r') as f:
    data = csv.reader(f,delimiter = '\t')
    for i in data:
        print(','.join(i))

