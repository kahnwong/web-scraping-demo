import requests
from bs4 import BeautifulSoup
from icecream import ic


start_url = "https://mechanicalkeyboards.com/shop/"

# extract raw data
r = requests.get(start_url)
soup = BeautifulSoup(r.content, "html.parser")

# parse data
entries = soup.select("div.product-box")
for entry in entries:
    d = {
        "name": entry.select_one("div.product-name a").get_text(),
        "url": entry.select_one("div.product-name a").get("href"),
        "price": entry.select_one("div.price span").get_text(),
    }

    ic(d)
