import os

import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pymongo
from random import randint
from time import sleep
import numpy as np
from flask import Flask, jsonify
import json

yourAPI = "AIzaSyC3lF94PxnSx34-WtKyRO_2ETFq-RSD2Ao"

#############################################################
#FUNCTIONS DEFINITIONS
#############################################################
def splinterS(browser,numberPages):
    title = []
    Location = []
    JobId = []
    pDate = []
    urlL = []
    Description = []

    tit = []
    Loc = []
    JId = []
    pDa = []
    urL = []
    Des = []
    
    for x in range(numberPages+1):
        html = browser.html
        sleep(randint(40,58))
        suppe = bs(html, 'html.parser')

        results = suppe.find_all('div',class_='job')
        urls = suppe.findAll("div",class_="job-tile")

        for url in urls:
            partial_url = url.a["href"]
            urlL.append("https://amazon.jobs" + partial_url)

        for result in results:
            title.append(result.find("h3").text)
            LocId = (result.find("p").text).split(" | ")
            JobIdx = LocId[1].split(": ")
            Location.append(LocId[0])
            JobId.append(JobIdx[1])
            pDate.append(result.find("h2").text)
            Description.append(result.find("span").text)

        try:
            browser.find_by_css('button.btn.circle.right').first.click()
        
        except:
            print("Scraping Complete")
    for y in range(10,len(title)):
            tit.append(title[y])
            Loc.append(Location[y])
            JId.append(JobId[y])
            pDa.append(pDate[y])
            Des.append(Description[y])
            urL.append(urlL[y])
    return tit, Loc, JId, pDa, urL, Des
#############################################################
def geocoord(cityx, st, countryL, key):

    geocoorCity = []
    geocoorState = []
    dummy_list = []
    
    for m in range(0,len(cityx)):
        city = cityx[m]
        state = st[m]
        country = countryL[m]
        url = 'https://maps.googleapis.com/maps/api/geocode/json?' 
        
        try:
            responseCity = requests.get(url, params ={"address": city, "region": country, "key": yourAPI,})
            resultsCity = responseCity.json()
            if not resultsCity["results"]:
                responseCity = requests.get(url, params ={"address": country, "region": country, "key": yourAPI,})
                resultsCity = responseCity.json()
                latiCity = resultsCity["results"][0]["geometry"]["location"]["lat"]
                longCity = resultsCity["results"][0]["geometry"]["location"]["lng"]
            else:
                latiCity = resultsCity["results"][0]["geometry"]["location"]["lat"]
                longCity = resultsCity["results"][0]["geometry"]["location"]["lng"]
            dummy_list.extend([latiCity, longCity])
            geocoorCity.append(dummy_list)

            if (state == "NaN"):
                geocoorState.append(dummy_list)
                dummy_list = []
            else: 
                dummy_list = []
                responseState = requests.get(url, params ={"address": state, "region": country, "key": yourAPI,})
                resultsState = responseState.json()
            if not resultsState["results"]:
                responseState = requests.get(url, params ={"address": country, "region": country, "key": yourAPI,})
                resultsState = responseState.json()
                latiState = resultsState["results"][0]["geometry"]["location"]["lat"]
                longState = resultsState["results"][0]["geometry"]["location"]["lng"]
            else:
                latiState = resultsState["results"][0]["geometry"]["location"]["lat"]
                longState = resultsState["results"][0]["geometry"]["location"]["lng"]
            dummy_list.extend([latiState, longState])
            geocoorState.append(dummy_list)
            dummy_list = []

        except:
            print("something went wrong")
    return geocoorCity, geocoorState
#############################################################
#############################################################

def primeFunc():
    urx="https://amazon.jobs/en"
    html = requests.get(urx)
    
    bsobj = bs(html.content, "html.parser")

    result_f = bsobj.find_all('div', class_="nav-link-wrapper")

    for result in result_f:
        try:
            link = result.a['href']
            if (link=="/en/job_categories"):
                print('-------------')
                jobC = "https://amazon.jobs"+ link
                print(jobC)
        except AttributeError as e:
            print(e)

    htmz = requests.get(jobC)
    
    sopa = bs(htmz.content, "html.parser")

    filter_One = sopa.find_all('div',class_='container collection-tiles')

    filter_Two=filter_One[0].div["data-react-props"]
    items = eval(filter_Two)["items"]
    jobCat_url=[]
    jobCat_title=[]

    for item in items:
        try:
            title = item['title']
            part_url = item['link']
            job_url = "https://amazon.jobs"+ part_url
            jobCat_url.append(job_url)
            jobCat_title.append(title)
        except AttributeError as e:
            print(e)
    urg = jobCat_url[0]

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(urg)

    html = browser.html
    suppe = bs(html, 'html.parser')

    layer = suppe.find("div",class_="title count col-5")
    Category = suppe.find("div",class_="title col-7").text

    lon = len(layer.text) - len(layer.find("p").text)
    numberJobs = int(layer.text[0:lon])
    numberPages = int(np.ceil(numberJobs/10))

    bunchLists = splinterS(browser,numberPages) #calling function Splinter
    title = bunchLists[0]
    Location = bunchLists[1]
    jobId = bunchLists[2]
    pDate = bunchLists[3]
    urlL = bunchLists[4]
    Description = bunchLists[5]


    countryL = []
    st = []
    cityx = []
    for loc in Location:
        comP_loc = loc.split(",")
        if (len(comP_loc) == 3):
            countryL.append(comP_loc[0])
            st.append(comP_loc[1])
            cityx.append(comP_loc[2])
        if (len(comP_loc) == 2):
            countryL.append(comP_loc[0])
            st.append("NaN")
            cityx.append(comP_loc[1])


    geocoorLists = geocoord(cityx, st, countryL, yourAPI) #Calling Function Geo
    geocoorCity = geocoorLists[0]
    geocoorState = geocoorLists[1]

    dictio = {}
    data = []
    for t in range(0,len(geocoorCity)):
        dictio["category"] = Category
        dictio["title"] = title[t]
        dictio["Job_ID"] = jobId[t]
        dictio["Location"] = Location[t]
        dictio["Posting_date"] = pDate[t]
        dictio["URL"] = urlL[t]
        dictio["Description"] = Description[t]
        dictio["city_Coordinates"] = geocoorCity[t]
        dictio["state_Coordinates"] = geocoorState[t]
        data.append(dictio.copy())

    return data


