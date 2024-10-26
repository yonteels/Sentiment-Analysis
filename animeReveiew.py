import pandas as pd
import mysql.connector

df = pd.read_csv('animeReview.csv')

conn = mysql.connector.connect(
    host='localhost',  
    user='root',  
    password='admin',  
    database='animeReview',  
    port = '3306'
)

cursor = conn.cursor()







