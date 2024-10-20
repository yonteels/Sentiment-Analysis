import csv
import pandas
import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user = "admin",
    password = "admin"
)

cursor =mydb.cursor()

with open('animeData.csv', mode = 'r') as file:
    csvFile = csv.DictReader(file)





mydb.close