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
        car_more_info = car.h3.a['href'].strip()
        car_posted =car.find('ul', class_='list-unstyled').text.strip()
        car_plate = car.find('p', class_='location').text.strip()
        all_cars.append({'Name': car_name, 'Price': car_price, 'More Info': car_more_info, "Posted": car_posted, "Plate": car_plate})
# Now, you have all the car data in the 'all_cars' list
print("Loading car data")
print("What type of fuel do you want?")
type_of_fuel = input(">")
print("What year of production do you want?")
year_of_production = input(">")

for car_data in all_cars:
    if 'Toyota' in car_data['Name']:
      if type_of_fuel and year_of_production in car_data['Plate']:
        if 'weeks' in car_data['Posted']:
            print('Its an old data are you sure you want to see it. Y/N')
            weeks_old = input('>')
            if 'Y' or 'y':
                print(car_data['Name'])
                print(car_data['Price'])
                print(car_data['Posted'])
                print(car_data['Plate'])
                print(car_data['More Info'])
                print('_______________________________')
            else:
                print("Thats what I thought.")
        else:
                print(car_data['Name'])
                print(car_data['Price'])
                print(car_data['Posted'])
                print(car_data['Plate'])
                print(car_data['More Info'])
                print('_______________________________')
    

