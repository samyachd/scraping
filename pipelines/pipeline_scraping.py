import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
from get_data import get_scraping_data as gs
from process_data import process_scraping_data as psd
from database import insert_data as id

file = '../scraping/data/data_scraping.csv'
file_clean = '../scraping/data/data_scraping_clean.csv'

def run_scraping_pipeline(pages:int, name: str):
    print("Scraping started ...")
    data_books = gs.scrape_books(pages)
    df_books = pd.DataFrame(data_books)
    df_books.to_csv(file)
    print("Data_scraping.csv saved in data folder")
    print("Step 1 done")
    psd.process_scraping(df_books)
    print("Process scraping done")
    df_books.to_csv(file_clean)
    id.insert_to_database(file_clean, name)
    print(f'Database_{name}.db created in workspace')
    print("Step 2 done")