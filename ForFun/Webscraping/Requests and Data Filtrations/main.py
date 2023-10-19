from bs4 import BeautifulSoup
import requests

print("Put some skills you are not familiar or interested in")
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')
print(f'Loading...')

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
count = 0
for job in jobs:
    date = job.find('span', class_='sim-posted').span.text.strip()
    if 'few' in date:
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        skills = job.find('span', class_='srp-skills').text.strip()
        more_info = job.header.h2.a['href'].strip()
        if unfamiliar_skill not in skills:
            count += 1

            print(f'Company Name: {company_name}')
            print(f'Required Skills: {skills}')
            print(f'More Information: {more_info}')
    
            print('_____________________________________________________________________________________________________________________________')
        

print(f'Found {count} jobs that match your criteria')
