import httpx 
from selectolax.parser import HTMLParser 
from dataclasses import dataclass , asdict 
import pandas as pd
from tqdm import tqdm 

# base url to scrape
base_url = 'https://www.thomann.de/gb/search_dir.html?sw=guitar&smcs=e182f5_12248'

# dataclass to store product information
@dataclass 
class Product:
    manufactuer: str 
    title: str 
    price: str 

# function to get html source code
def get_html(page):
    url = f'https://www.thomann.de/gb/search_dir.html?ls=25&pg={page}&sw=guitar&smcs=e182f5_12248'
    src = httpx.get(url)
    return HTMLParser(src.text)

# function to parse html and extract the data
def parse_html(html):
    products = html.css("div.product") # select the div that contains the product information
    results = []
    for item in products:
        new_item = Product(
            manufactuer= item.css_first("span.title__manufacturer").text().strip(),
            title= item.css_first("span.title__name").text().strip(),
            price= item.css_first("span.fx-typography-price-primary").text().strip()
        )
        results.append(asdict(new_item))
    return results

 
def main():
    res = []
    for x in tqdm(range(1,600)):
        html = get_html(x)
    res += parse_html(html)
    
    df = pd.DataFrame(res)
    print(df)
    
if __name__ == '__main__':
    main() 
