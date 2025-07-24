import sqlite3
import pandas as pd

def insert_to_database_scrap(file: str,name: str):
    df_books = pd.read_csv(file)
    connection = sqlite3.connect("database/"+name+".db")
    df_books.to_sql("books",connection, if_exists="replace", index=False)
    cursor = connection.cursor()
    connection.close()
    return
    """
    Prepare datas, create database and insert scraped datas in database
    """
def insert_to_database_API(df_books_API: pd.DataFrame, name: str):
    connection = sqlite3.connect("database/"+name+".db")
    cursor = connection.cursor()
    cursor.execute("SELECT book_id FROM books")
    rows = cursor.fetchall()
    df_books_API.insert(0, "book_id", range(rows[-1][0]+1, rows[-1][0] + len(df_books_API['title'])+1))
    data_to_insert = df_books_API.values.tolist()
    cursor.executemany("INSERT INTO books VALUES(?, ?, ?, ?, ?)", data_to_insert)
    connection.commit()
    """
    Prepare API datas and insert API datas in database
    """
