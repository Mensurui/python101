import time
from bs4 import BeautifulSoup
import requests

print("Put some skills you are not familiar or interested in")
input_string = input(">")
unfamiliar_skills = list(map(str, input_string.split()))

print(f'Filtering out {unfamiliar_skills}')
print(f'Loading...')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    count = 0
    for index, job in enumerate (jobs) :
        date = job.find('span', class_='sim-posted').span.text.strip()
        if 'few' in date:
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.strip()
            more_info = job.header.h2.a['href'].strip()
            unfamiliar_skill_found = False  # Flag to track unfamiliar skill

            for unfamiliar_skill in unfamiliar_skills:
                if unfamiliar_skill in skills:
                    unfamiliar_skill_found = True
                    break

            if not unfamiliar_skill_found:
                count += 1
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name}\n')
                    f.write(f'Required Skills: {skills}\n')
                    f.write(f'More Information: {more_info}\n')
                
                print(f'File saved as {index}')

    print(f'Found {count} jobs that match your criteria')
    
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait =10
        print(f'Waiting for {time_wait} minutes to complete...')
        time.sleep(time_wait*60)
