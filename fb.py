#%% Import packages
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time
from dotenv import load_dotenv
import os

from selenium.webdriver.common.action_chains import ActionChains

load_dotenv()

#%% Reading the file and importing random
import pandas as pd
import random

names = pd.read_csv('unigram_freq.csv')['word']

#%% Open chrome using driver
# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome() 
driver.get("https://facebook.com/") 
wait = WebDriverWait(driver, 600) 

#%% Login Form activity
login_form = driver.find_element_by_tag_name('form')
# print(login_form)

unField = login_form.find_element_by_name('email')
# print(unField)
unField.send_keys(Keys.CONTROL + "a")
unField.send_keys('8894453632')

pwField = login_form.find_element_by_name('pass')
# print(pwField)
pwField.send_keys(Keys.CONTROL + "a")
pwField.send_keys(os.getenv("FB_PASSWORD"))

# Now submit
pwField.send_keys(Keys.ENTER)

# Proceed to run the next cell after waiting to complete it
# Check how to wait for the page to complete loading
#%% Send a new post

# Method 1 or Method 2
try:
    post_write_form = driver.find_element_by_name('xhpc_message')
    
    post_write_up = input("Enter Post Write Up: ")

    post_write_form.send_keys(Keys.CONTROL + "a")
    post_write_form.send_keys(post_write_up)

    submit_btn = driver.find_element_by_class_name('_1mf7')
    submit_btn.click()
    print("Done")

except:
    print("Trying different Method!")
    post_write = driver.find_element_by_class_name('_1mwp')
    # print(post_write)
    post_write.click()

    post_write_up = input("Enter Post Write Up: ")

    actions = ActionChains(driver)
    actions.send_keys(post_write_up)
    actions.perform()

    submit_btn = driver.find_element_by_class_name('_1mf7')
    submit_btn.click()
    print("Done")


# %% Comment
comment_on_post_form = driver.find_element_by_xpath('//*[@id="fbPhotoSnowliftFeedbackInput"]/div/div/div[2]/div/div/div/div/div/form/div')
comment_on_post_form.click()

comment_write_up = 'That was an Awesome Day!'

count = int(input("Enter the count: "))

# This created an infinte???
actions = ActionChains(driver)
for i in range(count):
    actions.send_keys(comment_write_up + Keys.ENTER)

actions.perform()

#%%
driver.quit()
