import sqlite3
import pandas as pd

def insert_to_database(file: str,name: str):
    df_books = pd.read_csv(file)
    connection = sqlite3.connect(name+".db")
    df_books.to_sql("books",connection, if_exists="replace")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return

    """
    Prepare datas, create database and insert datas in database
    """

