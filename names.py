#%% Reading the file and importing random
import pandas as pd
import random

names = pd.read_csv('unigram_freq.csv')['word']

print(names.tail())
'''
for i in range(10):
    print(names[i])

i = random.randint(0,300000)
print(names[i])
'''

#%% Import for webdriver
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time

#%% Open the chrome and scan
# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome() 

driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 

# Replace 'Friend's Name' with the name of your friend  
# or the name of a group  
target = 'Friends'

# Replace the below string with your own message 
msg = "Message sent using python!"
input("Press Enter after scanning: ")


#%% The main cell
while(True):
    target = input("Enter the target (_cancel for stop) : ")
    if(target == '_cancel'):
        break
    print("Target set")

        # For the searching ans automatically selecting the first one
    search_box = driver.find_element_by_class_name('_2S1VP')
    search_box.send_keys(target + Keys.ENTER)
    print(search_box)

    main_content_holder = driver.find_element_by_tag_name('footer')
    message_input = main_content_holder.find_element_by_class_name('_2S1VP')

    count = int(input("Enter the count: "))

    for i in range(count):
        rand_val = random.randint(0,333332)
        message_input.send_keys((names[rand_val]+'  '+str(rand_val)) + Keys.ENTER)

    print("Messages sent!")

print("Done")
