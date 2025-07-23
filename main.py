from pipelines import pipeline_scraping as ps
import argparse

def main():
    try:
        parser = argparse.ArgumentParser(description="Fetch datas into a database from a page of bookstoscrape.com")
        parser.add_argument('pages', type=int, help='Page number you want to fetch')
        parser.add_argument('database', type=str, help='Name of the database')
        args = parser.parse_args()
        ps.run_scraping_pipeline(args.pages, args.database)
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    main()
