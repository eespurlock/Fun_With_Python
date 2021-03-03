'''
Author: Esther Edith Spurlock

Project Title: Jobs Scraper

Project Description: In my quest to find a job, I have found a multitude of companies that I would like to work for.
However, going onto their job board every day (or even every week) would take a long time. So, I intend to create this
web scraper that will go onto the careers page for each of these companies and scrape what job titles are available.
'''

#import statements
import pandas as pd
from datetime import datetime, timedelta
import bs4
import requests
import gc
print("Imports complete")

#Create constant variables for strings
ORG = 'Organization Name'
JOB = 'Job Title'

#create a place to store our data
data = {ORG : [],
        JOB: []}

def main():
    '''
    The main of our program

    Loops through the dictionary holding the organization names, job board URLs, and function names
    in order to scrape these pages and put the job titles with their corresponding organization name
    into our data dictionary

    Inputs: None

    Outputs: None, it changes the data dictionary in the function
    '''
    for key, value in links_dict.items():
        #makes the BeautifulSoup object
        print(key)
        url, funct = value
        req = requests.get(url) #Creating the request object
        if req:
            req_en = req.text.encode('iso-8859-1', 'ignore') #Encode the request object
        else:
            sys.exit("Not a valid request object")
    
        soup = bs4.BeautifulSoup(req_en, features="html.parser") #Turning the request object into a BeautifulSoup object

        if soup:
            delete_lst([req, req_en]) #Deleting references to objects we do not need
            lst = funct(soup)
            for job in lst:
                data[ORG].append(key)
                data[JOB].append(job)
            del soup

        else:
            del soup
            sys.exit("Not a valid soup object")
        
        print(key + " complete")
    
    df = pd.DataFrame(data=data) #turns our data into a Pandas dataframe
    print(df)

def delete_lst(del_lst):
    '''
    deletes a list of objects
    
    inputs: a list of objects to be deleted
    '''
    for item in del_lst:
        del item

def elevate_energy(soup):
    '''
    Scrapes job titles from Elevate Energy's page

    Inputs: soup: a BeautifulSoup object of Elevate Energy's jobs page

    Outputs: lst: a list of job titles on Elevate Energy's jobs page
    '''
    lst = []
    for instance in soup.find_all(['h3'], {"class": "event__title"}):
        lst.append(instance.get_text())
    return lst

def mission_measurement(soup):
    '''
    Scrapes job titles from Mission Measurment's page

    NOTE: MM's jobs page seems to have old job postings that are not visible on their jobs page still listed
        in their HTML code, so some of the jobs scraped from this page may not be available

    Inputs: soup: a BeautifulSoup object of Mission Measurement's jobs page

    Outputs: lst: a list of job titles on Mission Measurement's jobs page
    '''
    lst = []
    for instance in soup.find_all(['strong']):
        lst.append(instance.get_text())
    return lst

def GAO(soup):
    '''
    Scrapes job titles from USA Jobs for the Government Accountability Office

    NOTE: This is a work in progress!!
    
    Inputs: soup: a BeautifulSoup object of the USA Jobs page with GAO jobs

    Outputs: lst: a list of job titles available at the GAO
    '''
    lst = []
    for instance in soup.find_all(["a"], itemprop=["title"]):
        lst.append(instance.get_text())
    return lst

#crete a dictionary with all of the organizations, their careers page, and the function we will use to scrape the page
links_dict = {"Elevate Energy": ("https://www.elevatenp.org/careers/", elevate_energy),
              "Mission Measurement": ("http://missionmeasurement.com/about-us/#careers", mission_measurement)}
main() #calls our main function
#gets both today's date and yesterday's date
#today = datetime.today().strftime('%y-%m-%d')
#yesterday = datetime.today() - timedelta(days=1)
#yesterday = yesterday.strftime('%y-%m-%d')
#print(today)
#print(yesterday)
gc.collect() #collects the garbage
print("Complete")



