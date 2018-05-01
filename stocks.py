import requests
from bs4 import BeautifulSoup as BS
from lxml import html

MY_ADDRESS = "atish.patel95@yahoo.com"
stocks = {"apple":"AAPL:US", "netflix":"NFLX:US"}

#take in a requests object
#iterate through .price selectors and print the text
def get_price(r):
    soup = BS(r.content, 'html.parser')
    spans = soup.select('.price')
    for i in range(len(spans)):
        return spans[i].getText()

#take in ticker (and optionally base url and extension)
#create url for that companies page
def get_url(product, base="https://www.bloomberg.com/", extension="quote/"):
    base_url = base
    extension = extension
    product = product
    url = base_url + extension + product
    return url

#use cli to ask for stock company name
#check that name with the stocks data structure to get ticker
#use the ticker to get request from that companies page
def main():
    my_stock = raw_input("Enter stock to track: ")
    ticker = stocks[my_stock.lower()]
    r = requests.get(get_url(ticker))
    r.raise_for_status()
    price = get_price(r)
    print("the price of your stock is " + price)

if __name__ == '__main__': main()
