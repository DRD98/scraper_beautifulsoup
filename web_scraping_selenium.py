import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from env_config import (
    selenium_url,
    books_class,
    price_class,
    availability_class,
    rating_class
)


book_data = []

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(selenium_url)

while True:
    time.sleep(4)
    books = driver.find_elements(By.CLASS_NAME, books_class)

    for book in books:

        short_name = book.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a")
        name = short_name.get_attribute("title")
        price = book.find_element(By.CLASS_NAME, price_class).text
        available = book.find_element(By.CLASS_NAME, availability_class).text
        rating = book.find_element(By.CLASS_NAME, rating_class)
        classes = rating.get_attribute("class").split()[1]
        rating_number = rating_map.get(classes, 0)

        book_data.append({
            "Book name": name,
            "Price": price,
            "Availability": available,
            "Star rating": rating_number,
        })

    try:
        next_button = driver.find_element(By.CLASS_NAME, "next").find_element(By.TAG_NAME, "a")
        next_button_link = next_button.get_attribute("href")
        driver.get(next_button_link)
    except NoSuchElementException:
        print("\n No more pages found.")
        print("\n ------------------------ End of Web Sraper ------------------------")
        break

driver.quit()

df = pd.DataFrame(book_data)
df.sort_values("Book name", inplace=True)
df.to_excel(r"C:\Work\Product_Data\product_list_selenium.xlsx", index=False)

