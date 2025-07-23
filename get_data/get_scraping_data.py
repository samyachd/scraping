import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_books_html(url: str) -> BeautifulSoup:
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    return soup
    """Fetch the HTML content of a book page.

    Args:
        url (str): The URL of the book page.

    Returns:
        BeautifulSoup: A BeautifulSoup object containing the HTML content.
    """

def extract_title(book: BeautifulSoup) -> str:
    return book.find("img")['alt']
    """Extract the title of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        str: The title of the book.
    """

def extract_price(book: BeautifulSoup) -> str:
    return book.find("p", class_="price_color").text
    """Extract the price of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        str: The price of the book.
    """

def extract_rating(book: BeautifulSoup) -> str:
    return book.find("p")['class'][1]
    """Extract the rating of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        str: The rating of the book.
    """

def extract_availability(book: BeautifulSoup) -> str:
    return book.find('p', class_="instock availability").text.strip()
    """Extract the availability of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        str: The availability of the book.
    """

def extract_book_info(book: BeautifulSoup) -> dict:
    book_dict = {"title": extract_title(book),
                "price": extract_price(book),
                "rating": extract_rating(book),
                "availability": extract_availability(book)}
    return book_dict
    """Extract all information of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        dict: A dictionary containing the title, price, rating, and availability of the book.
    """


def scrape_books(pages: int) -> list[dict]:
    base_url = f"http://books.toscrape.com/catalogue/page-{pages}.html"
    soup = get_books_html(base_url)
    books = soup.find_all("article", class_="product_pod")
    list_books = [extract_book_info(i) for i in books]
    return list_books
    """Scrape books from the specified number of pages.

    Args:
        pages (int): The number of pages to scrape.

    Returns:
        list: A list of dictionaries containing books information.
    """

    