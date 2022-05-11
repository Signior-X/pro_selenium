# %%
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
# import pyttsx3

# %%
# Replace below path with the absolute path
# to chromedriver in your computer

import os
print(os.getcwd())
pathOfDriver = os.getcwd() + '/chromedriver'
print(pathOfDriver)

driver = webdriver.Chrome(pathOfDriver)

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = 'Friends'

# Replace the below string with your own message
msg = "Message sent using python!"
input("Press Enter after scanning: ")

#%% Reading the data here


#%% Final message for running

targets = ["pranshu", "hiya", "yuvi"]

for target in targets:
    if(target == ''):
        break
    print("Target set", target)

    # For the searching ans automatically selecting the first one
    search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_box.send_keys(target + Keys.ENTER)
    print(search_box)

    # just add a wait to find the contact
    time.sleep(3)


    message_input = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    msg = "test"

    message_input.send_keys(msg)
    message_input.send_keys(Keys.ENTER)

    message_input.send_keys(Keys.CONTROL + "v")
    time.sleep(0.5)

    image_input = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]')
    image_input.send_keys(Keys.ENTER)
    time.sleep(0.2)

    print("Messages sent!")


print("Done")
# Happy Birthday Naresh

# %% Quit
driver.quit()
