import requests
from bs4 import BeautifulSoup

# Initialize a list to store all car data
all_cars = []

# Define the base URL
base_url = "https://www.mekina.net/cars/?body_type=Sedan&page="

count = 0
# Loop through multiple pages
for page_number in range(1, 4):  # You can specify the range of pages you want to scrape

    # Make a request to the website
    res = requests.get(base_url + str(page_number))

    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(res.text, 'lxml')

    # Find all car listings on the page
    cars = soup.find_all('div', class_='category-grid-box-1')
    # Loop through the car listings on the current page
    for car in cars:
        car_name = car.find('h3').text.strip()
        car_price = car.find('div', class_='price').text.strip()
        count += 1
        all_cars.append({'Number':count,'Name': car_name, 'Price': car_price})
# Now, you have all the car data in the 'all_cars' list
for car_data in all_cars:
    print(car_data['Number'])
    print(car_data['Name'])
    print(car_data['Price'])
    print('_______________________________')
    

print(count)
