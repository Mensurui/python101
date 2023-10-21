import requests
from bs4 import BeautifulSoup

# Make a request to the website
res = requests.get("https://www.mekina.net/cars/?body_type=Sedan")

# Parse the page with BeautifulSoup
soup = BeautifulSoup(res.text, 'lxml')
# Print the page title
cars = soup.find_all('div', class_='category-grid-box-1')

for car in cars:
    car_name = car.find('h3').text.strip()
    print(car_name)