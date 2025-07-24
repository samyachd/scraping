import pandas as pd

def process_scraping(df_books: pd.DataFrame):
    df_books.reset_index(inplace=True)
    df_books.rename(columns={"index":"book_id"}, inplace=True)
    df_books["title"] = df_books["title"].astype("string")
    df_books["rating"] = df_books["rating"].map({"One":1,"Two":2,"Three":3,"Four":4,"Five":5})
    df_books["price"] = df_books['price'].str.slice(1).astype("float")
    df_books["availability"] = df_books["availability"].map({"In stock":True,"Out of stock":False})
    return df_books

def safe_get(data, *keys):
    for key in keys:
        if type(data) == dict:
            data = data.get(key)
        else:
            return None
    return data

def process_API(db: list):
    books_list = [
    {
        "title": safe_get(book, "volumeInfo", "title"),
        "price": safe_get(book, "saleInfo", "listPrice", "amount"),
        "rating": safe_get(book, "volumeInfo", "averageRating")
    }
    for book in db
]
    df_books_API = pd.DataFrame(books_list)
    df_books_API = df_books_API.dropna()
    df_books_API = df_books_API.reset_index(drop=True)
    df_books_API["availability"] = False
    return df_books_API