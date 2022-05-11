# %%
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd

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

dataFile1 = "Btech21.csv"
df = pd.read_csv(dataFile1)
df

#%% Final message for running

# What if the target is not found??

lastOne = ""
for index, row in df.iterrows():

    target = str(row['Mobile Phone'])
    thisName = row['First2']

    if(target == ''):
        break
    print("Target set", target)

    # For the searching ans automatically selecting the first one
    search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_box.send_keys(Keys.CONTROL + "a")
    search_box.send_keys(target + Keys.ENTER)
    print(search_box)

    # just add a wait to find the contact
    time.sleep(3)

    currentOne = driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div/div/span').text
    if (lastOne != "" and lastOne == currentOne):
        print("Not found, skipping")
        continue

    lastOne = currentOne
    message_input = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    msgs = ["""Hi """ + thisName + """,""",
    Keys.SHIFT + Keys.ENTER,
    """I am Aachman Gandhi, an undergraduate student from the 2020 batch. I am contesting for the post of Cultural Secretary in the upcoming gymkhana elections. I am the lead volunteer for the Dramatics Society (2021-2022). I am also a core member of the Photography and Moviemaking Club(2021-2022). I am also an active member of the Debating Society. I was the Publicity Head of Ruvaan, the intercollege literary fest of our college.""",
    Keys.SHIFT + Keys.ENTER,
    Keys.SHIFT + Keys.ENTER,
    """If elected, I wish to execute my vision of a more rich, inclusive, diverse and flourishing culture in our college.""",
    Keys.ENTER,
    """I request you to go through my manifesto and if you have any views or any point of my manifesto that you want to discuss with me then fell free to share you thoughts with me.""",
    Keys.SHIFT + Keys.ENTER,
    Keys.SHIFT + Keys.ENTER,
    """Your vote matters a lot, cast it wisely. Above all, please do vote, that is the most important part.""",
    Keys.SHIFT + Keys.ENTER,
    """Contact No.- 9915239089"""
    ]

    for msg in msgs:
       message_input.send_keys(msg)
 
    message_input.send_keys(Keys.ENTER)

    message_input.send_keys(Keys.CONTROL + "v")
    time.sleep(5)

    image_input = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]')
    image_input.send_keys(Keys.ENTER)
    time.sleep(5)

    print("Messages sent!")


print("Done")
# Happy Birthday Naresh

# %% Quit
driver.quit()

# %%
