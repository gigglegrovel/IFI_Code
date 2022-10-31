# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 17:30:56 2021

@author: End User
"""

import scrapy
import math
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

path = "C:/Users/End User/chromedriver.exe"

driver = webdriver.Chrome(path)

driver.get("https://my.flexmls.com/ampimls/search/idx_links/20121120155711416234000000/listings")

search = driver.find_element(By.ID,"desktopHideMapButton")

search.click()

time.sleep(10)

posts = 1438

scrolls = math.ceil(posts / 10 )

element = driver.find_element(By.ID, "preparedDate")

for i in range(scrolls):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(5)

source_data = driver.page_source
doc = BeautifulSoup(source_data, "html.parser")

