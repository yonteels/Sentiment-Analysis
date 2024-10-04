import csv
import pandas

with open('review.csv', mode = 'r') as file:
    csvFile = csv.DictReader(file)

    #write into mysql or sqlite or something
    for row in csvFile:
        print(row['Japanese Title'])
        print(row['English Title'])
        print(row['Rating'])
        print(row['Reviewer'])
        print(row['Review'])
        print(row['Reviewers'])
        print(row['Rating'])

