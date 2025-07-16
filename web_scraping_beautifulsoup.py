import environ
import requests
import pandas as pd
from pathlib import Path
from bs4 import BeautifulSoup


BASE_DIR = Path(__file__).resolve().parent
env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MyScraper/1.0; +https://example.com/bot)"
}

url = env('URL')
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
products = soup.find_all("div", class_="SKUDeck___StyledDiv-sc-1e5d9gk-0 eA-dmzP")

product_data = []

for product in products:
    name_tag = product.find("div", class_="break-words")
    name = name_tag.text.strip() if name_tag else "N/A"

    qty_span = product.find("span", class_="PackChanger___StyledLabel-sc-newjpv-1")
    if not qty_span:
        qty_span = product.find("span", class_="PackSelector___StyledLabel-sc-1lmu4hv-0")
    quantity = qty_span.text.strip() if qty_span else "N/A"

    price_tag = product.find("span", class_="Pricing___StyledLabel-sc-pldi2d-1")
    price = price_tag.text.strip()[1:] if price_tag else "N/A"

    product_data.append({
        "Name": name,
        "Quantity": quantity,
        "Price": price
    })
    df = pd.DataFrame(product_data)
    df.to_excel(r"C:\Work\Product_Data\product_list.xlsx", index=False)
    



