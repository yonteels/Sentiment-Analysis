import pandas as pd
import mysql.connector

df = pd.read_csv('animeData.csv')

conn = mysql.connector.connect(
    host='localhost',  
    user='root',  
    password='admin',  
    database='animedatabase',  
    port = '3306'
)

cursor = conn.cursor()
line =0;

for _, row in df.iterrows():
    print(line)
    line += 1
    sql = """
    INSERT INTO allanime (Title, Rating, `Rank`, Popularity, Synopsis, Episodes, Status, Aired, Genres)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (
        row['Title'], 
        row['Rating'] if row['Rating'] != 'N/A' else None, 
        int(row['Rank']) if not pd.isnull(row['Rank']) else None,
        int(row['Popularity']) if not pd.isnull(row['Popularity']) else None,
        row['Synopsis'], 
        int(row['Episodes']) if not pd.isnull(row['Episodes']) else None,
        row['Status'], 
        row['Aired'], 
        row['Genres']
    ))


conn.commit()
cursor.close()
conn.close()

print("Data successfully inserted into MySQL database.")
