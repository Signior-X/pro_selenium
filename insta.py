#%% Import packages
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time
from dotenv import load_dotenv
import os

load_dotenv()

#%% Reading the file and importing random
import pandas as pd
import random

names = pd.read_csv('unigram_freq.csv')['word']


#%% Open chrome using driver
# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome() 

driver.get("https://instagram.com/") 
wait = WebDriverWait(driver, 600) 

#%% Login Form activity
login_form = driver.find_element_by_tag_name('form')
# print(login_form)

unField = login_form.find_element_by_name('username')
# print(unField)
unField.send_keys(Keys.CONTROL + "a")
unField.send_keys('sethpriyam1@gmail.com')

pwField = login_form.find_element_by_name('password')
# print(pwField)
pwField.send_keys(Keys.CONTROL + "a")
pwField.send_keys(os.getenv("INSTA_PASSWORD"))

# Now submit
pwField.send_keys(Keys.ENTER)

# Proceed to run the next cell after waiting to complete it
# Check how to wait for the page to complete loading
#%% Remove the start badge
not_now_xpath = '//*[@id="react-root"]/section/main/div/div/div/div/button'
not_now_btn = driver.find_element_by_xpath(not_now_xpath)
print(not_now_btn)
not_now_btn.click()

#%% Remove notification window if came up
not_now_xpath = '/html/body/div[4]/div/div/div[3]/button[2]'
not_now_btn = driver.find_element_by_xpath(not_now_xpath)
print(not_now_btn)
not_now_btn.click()

#%% Open the messages
chat_xpath = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]'
chat_btn = driver.find_element_by_xpath(chat_xpath)
print(chat_btn)
chat_btn.click()

#%% Open chat of the person
print("TO do later")

#%% Send message
message_area_xpath = '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea'
message_area = driver.find_element_by_xpath(message_area_xpath)
print(message_area)
msg = "Testing"
count = int(input('Enter the count: '))
message_area.send_keys(msg)
message_area.send_keys(Keys.CONTROL + "a")
message_area.send_keys(Keys.CONTROL + "c")
message_area.send_keys(Keys.ENTER)
for i in range(count):
    rand_val = random.randint(0,1000)
    message_area.send_keys(Keys.CONTROL + "v") 
    message_area.send_keys(Keys.ENTER)
print("Done")

#%% Comment on a post (first set the post)
comment_area = driver.find_element_by_class_name('X7cDz').find_element_by_tag_name('textarea')

count = int(input("Enter the count: "))
for i in range(count):
    comment_area.send_keys("Awesome Pics bro!" + Keys.ENTER)
    time.sleep(3)

#%% Quit
driver.quit()
