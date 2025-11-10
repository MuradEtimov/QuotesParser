from bs4 import BeautifulSoup
import requests
import lxml
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)",
    "Accept-Language": "en-US,en;q=0.9"
}

def aray():
    """Parsing all pages"""
    for page in range(1, 20):
        print(f"Page № {page}...")
        sleep(2)
        url = f"https://quotes.toscrape.com/page/{page}/"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"⚠️ Page {page} doesnt dowlaund({response.status_code})")
            break

        soup = BeautifulSoup(response.text, "lxml")
        quotes = soup.find_all("div", class_="quote")

        # Покажем, сколько цитат нашли
        print(f"Find {len(quotes)} quotes.")

        # Если нет цитат — значит, страницы закончились
        if not quotes:
            print(f"❌ Quotes on page {page} didt find. im stopping.")
            break

        for q in quotes:
            text = q.find("span", class_="text").text.strip()
            author = q.find("small", class_="author").text.strip()
            tags = q.find("meta", class_="keywords").get("content").strip()

            author_link = "https://quotes.toscrape.com" + q.find("a")["href"]
            author_page = requests.get(author_link, headers=headers)
            soup_author = BeautifulSoup(author_page.text, "lxml")

            born_date = soup_author.find("span", class_="author-born-date").text.strip()
            born_location = soup_author.find("span", class_="author-born-location").text.strip()

            yield (author, born_date, born_location, text, tags)
