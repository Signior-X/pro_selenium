#%% Import libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

#%% Open the driver
driver = webdriver.Chrome()

driver.get("http://mandifunker.pythonanywhere.com/")
wait = WebDriverWait(driver, 600)

#%% Do tasks here
n = 10
i=0
while(i<n):
    first = driver.find_element_by_xpath('/html/body/div/div/div[2]/a');
    first.click()
    print("Clicked")
    i+=1



