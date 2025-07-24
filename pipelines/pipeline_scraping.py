import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
from get_data import get_scraping_data as gs
from process_data import process_scraping_data as psd
from database import insert_data as id

file = '../scraping/data/data_scraping.csv'
file_clean = '../scraping/data/data_scraping_clean.csv'
url = "https://www.googleapis.com/books/v1/volumes"
payload = {"q":"food","filter":"paid-ebooks","maxResults":40,"orderBy":"relevance"}

def run_scraping_pipeline(pages:int, name: str):
    """Scraping du site web books.toscrape.com et de l'API googlebooks
       Enregistre database file dans database dir, csv files dans data

    Args:
        pages (int): nombre de pages à scraper
        name (str): nom de la database
        url (str): URL de l'API
        payload (dict): dictionnaire de paramètres
    """
    print("Scraping started ...")

    data_books_API = gs.get_books_API(url, payload)
    data_books_scrap = gs.scrape_books(pages)
    df_books = pd.DataFrame(data_books_scrap)
    df_books.to_csv(file, index=False)

    print("Scraping done, processing datas ...")

    psd.process_scraping(df_books)
    psd_data_books_API = psd.process_API(data_books_API)

    print("Process done, inserting to database ...")

    df_books.to_csv(file_clean, index=False)
    id.insert_to_database_scrap(file_clean, name)
    id.insert_to_database_API(psd_data_books_API, name)
    
    print(f'Database_{name}.db created in workspace')
    print("Script completed")
    