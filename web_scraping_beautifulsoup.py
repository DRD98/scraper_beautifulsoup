import environ
import requests
import pandas as pd
from bs4 import BeautifulSoup

from env_config import (
    beautifulsoup_url,
    header,
    name_div,
    product_div,
    quantity_span_1,
    quantity_span_2,
    price_span,
)


headers = {
    "User-Agent": header
}

response = requests.get(beautifulsoup_url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
products = soup.find_all("div", class_ = product_div)

product_data = []

for product in products:
    name_tag = product.find("div", class_=name_div)
    name = name_tag.text.strip() if name_tag else "N/A"

    qty_span = product.find("span", class_ = quantity_span_1)
    if not qty_span:
        qty_span = product.find("span", class_ = quantity_span_2)
    quantity = qty_span.text.strip() if qty_span else "N/A"

    price_tag = product.find("span", class_ = price_span)
    price = price_tag.text.strip()[1:] if price_tag else "N/A"

    product_data.append({
        "Name": name,
        "Quantity": quantity,
        "Price": price
    })
    df = pd.DataFrame(product_data)
    df.sort_values("Name", inplace=True)
    df.to_excel(r"C:\Work\Product_Data\product_list_beautifulsoup.xlsx", index=False)
    



