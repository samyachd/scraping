import pandas as pd

def process_scraping(df_books: pd.DataFrame):
    df_books["title"] = df_books["title"].astype("string")
    df_books["rating"] = df_books["rating"].map({"One":1,"Two":2,"Three":3,"Four":4,"Five":5})
    df_books["price"] = df_books['price'].str.slice(1).astype("float")
    df_books["availability"] = df_books["availability"].map({"In stock":True,"Out of stock":False})