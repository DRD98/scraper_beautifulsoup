import environ
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

header = env('HEADER')
beautifulsoup_url = env('BEAUTIFUL_SOUP_URL')
name_div = env("NAME_DIV")
product_div = env('PRODUCT_DIV')
quantity_span_1 = env('QUANTITY_SPAN_1')
quantity_span_2 = env('QUANTITY_SPAN_2')
price_span = env('PRICE_SPAN')

selenium_url = env("SELENIUM_URL")
books_class = env("BOOKS_CLASS")
price_class = env("PRICE_CLASS")
availability_class = env("AVAILABILITY_CLASS")
rating_class = env("RATING_CLASS")
