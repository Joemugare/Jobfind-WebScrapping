#!/usr/bin/env python
# coding: utf-8

# # Scrapping Job Website Using Python

# In[ ]:


from bs4 import BeautifulSoup
import requests
import time


# # Import The Url

# In[ ]:


url = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
 


# In[3]:


url


# # Import the url using BoutifulSoup from library li from page of website
# # Create Publish date,Company name and skills

# In[8]:


soup = BeautifulSoup(url, 'lxml')
jobs =soup.find_all('li', class_= "clearfix job-bx wht-shd-bx")
for job in jobs:
    published_date = job.find('span', class_ ='sim-posted').span.text
    if 'few' in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name')
        skills = job.find('span', class_ ='srp-skills').text
        print(f'''
        company name :{company_name}
        Required Skills :{skills}
        Published :{published_date}
        ''')


# # Print the company name and skills 

# In[12]:


for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text
    if 'few' in published_date:  # Check if the job was posted recently
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        skills = job.find('span', class_='srp-skills').text.strip()
        print(f"Company Name: {company_name}")
        print(f"Required Skills: {skills}")

        
        


# # Create more info template and print

# In[14]:


for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text
    if 'few' in published_date:  # Check if the job was posted recently
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        skills = job.find('span', class_='srp-skills').text.strip()
        more_info = job.header.h2.a['href']
        print(f"Company Name: {company_name}")
        print(f"Required Skills: {skills}")
        print(f'More Info: {more_info}')


# # Create a tab to display unfamilier skill and print

# In[18]:


print('Put some skills that you are not familiar with')
unfamiliar_skill = input('>')

for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text
    if 'few' in published_date:  # Check if the job was posted recently
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        skills = job.find('span', class_='srp-skills').text.strip()
        more_info = job.header.h2.a['href']
        if unfamiliar_skill not in skills:
            print(f"Company Name: {company_name}")
            print(f"Required Skills: {skills}")
            print(f"More Info: {more_info}")


# # Create a loop and timeout for the search and complete the code

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
                with open(f'posts/{index}.txt''w') as f:
                    f.write(f"Company Name: {company_name}")
                    f.write(f"Required Skills: {skills}")
                    f.write(f"More Info: {more_info}")
                

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 5
        print(f'Waiting {time_wait} seconds...')
        time.sleep(time_wait * 60)




# In[ ]:




