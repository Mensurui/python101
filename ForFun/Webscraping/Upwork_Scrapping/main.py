import requests
from bs4 import BeautifulSoup

# Make a request to the website
res = requests.get("https://finance.yahoo.com/u/yahoo-finance/watchlists/crypto-top-tokens-outstanding")

# Parse the page with BeautifulSoup
soup = BeautifulSoup(res.text, 'lxml')
# Print the page title
print(soup.title.string)
