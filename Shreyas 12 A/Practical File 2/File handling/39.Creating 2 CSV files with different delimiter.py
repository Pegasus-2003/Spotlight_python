import csv

with open('csvfile2.csv', mode='w') as file:
    csvwriter = csv.writer(file, delimiter=' ')
    csvwriter.writerow(['a', 'b', 'c'])
    csvwriter.writerow(['e', 'f', 'g'])
    csvwriter.writerow(['h', 'i', 'j'])


def rewrite():
    aList = []
    file = open('csvfile2.csv', "r")
    reader = csv.reader(file, delimiter=',')
    # next(reader, None) # Skip the header but I want to preserve it in the output csv file
    for row in reader:
        for col in row:
            aList.append(col.lower())

    file.close()
    file = open('csvfile2', 'w')
    csvwriter = csv.writer(file, delimiter=',')
    for a in aList:
        csvwriter.writerow(a.split())


rewrite()

        
