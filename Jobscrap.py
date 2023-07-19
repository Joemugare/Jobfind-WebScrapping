#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import time
import os


# In[ ]:


def find_jobs():
    print('Put some skills that you are not familiar with')
    unfamiliar_skill = input('>')

    url = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(url, 'lxml')
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').text
        if 'few' in published_date:  # Check if the job was posted recently
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.strip()
            more_info = job.h2.a['href']  # Corrected attribute access
            if unfamiliar_skill not in skills:
                # Create 'posts' directory if it doesn't exist
                if not os.path.exists('posts'):
                    os.makedirs('posts')
                
                with open(f'posts/{index}.txt', 'w') as f:  # Fixed the open statement
                    f.write(f"Company Name: {company_name}\n")
                    f.write(f"Required Skills: {skills}\n")
                    f.write(f"More Info: {more_info}\n")
                print(f"Job details saved in 'posts/{index}.txt'")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 5
        print(f'Waiting {time_wait} seconds...')
        time.sleep(time_wait * 60)



# In[ ]:





# In[ ]:




