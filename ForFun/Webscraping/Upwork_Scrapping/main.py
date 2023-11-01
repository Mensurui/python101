import time
import requests
from bs4 import BeautifulSoup


def find_cars():
    all_cars = []

    base_url = "https://www.mekina.net/cars/?body_type=Sedan&page="

    count = 0
    for page_number in range(1, 4): 

        res = requests.get(base_url + str(page_number))

        soup = BeautifulSoup(res.text, 'lxml')

        cars = soup.find_all('div', class_='category-grid-box-1')
        for car in cars:
            car_name = car.find('h3').text.strip()
            car_price = car.find('div', class_='price').text.strip()
            car_more_info = car.h3.a['href'].strip()
            car_posted =car.find('ul', class_='list-unstyled').text.strip()
            car_plate = car.find('p', class_='location').text.strip()
            all_cars.append({'Name': car_name, 'Price': car_price, 'More Info': car_more_info, "Posted": car_posted, "Plate": car_plate})
    print("Loading car data")
    print("What type of fuel do you want?")
    type_of_fuel = input(">")
    print("What year of production do you want?")
    year_of_production = input(">")
    print("What company production do you want?")
    company_of_production = input(">")

    for index, car_data in enumerate (all_cars):
        if company_of_production in car_data['Name']:
         if type_of_fuel and year_of_production in car_data['Plate']:
            if 'weeks' not in car_data['Posted']:
                print(car_data['Name'])
                value_name = car_data['Name']
                value_price = car_data['Price']
                value_posted = car_data['Posted']
                value_plate = car_data['Plate']
                value_more_info = car_data['More Info']
                with open(f'posts/{index}.txt', 'w', encoding='utf-8') as f:
                        f.write(f'Company Name: {value_name}\n')
                        f.write(f'Car Price: {value_price}\n')
                        f.write(f'Posted: {value_posted}\n')
                        f.write(f'Details: {value_plate}\n')
                        f.write(f'More Information: {value_more_info}\n')
                print(f'File saved as {index}')
            elif 'weeks' in car_data['Posted']:
                print("Car data outdated press Y/y to view data press N/n to leave")
                input_agreed = input(">")
                if input_agreed == "Y":
                    value_name = car_data['Name']
                    value_price = car_data['Price']
                    value_posted = car_data['Posted']
                    value_plate = car_data['Plate']
                    value_more_info = car_data['More Info']
                    with open(f'posts/{index}.txt', 'w', encoding='utf-8') as f:
                            f.write(f'Company Name: {value_name}\n')
                            f.write(f'Car Price: {value_price}\n')
                            f.write(f'Posted: {value_posted}\n')
                            f.write(f'Details: {value_plate}\n')
                            f.write(f'More Information: {value_more_info}\n')
                
                    print(f'File saved as {index}')
                elif input_agreed == "N":
                    print("Thanks for your feedback.")

    print("No more cars to view")

if __name__ == '__main__':
    while True:
        find_cars()
        time_wait =1
        print(f'Waiting for {time_wait} minutes to complete...')
        time.sleep(time_wait*60)


