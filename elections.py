# %%
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
from selenium.webdriver.common.by import By

# import pyttsx3

# %%
# Replace below path with the absolute path
# to chromedriver in your computer

import os
print(os.getcwd())
pathOfDriver = os.getcwd() + '/chromedriver.exe'
print(pathOfDriver)

#%%

driver = webdriver.Chrome()

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

    # target = row['Name']
    # thisName = row['First2']
    target = "Simo"
    thisName = "Smriti"

    if(target == ''):
        break
    print("Target set", target)

    # For the searching ans automatically selecting the first one
    search_box = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]')
    search_box.send_keys(Keys.CONTROL + "a")
    search_box.send_keys(target + Keys.ENTER)
    print(search_box)

    # just add a wait to find the contact
    time.sleep(3)

    currentOne = driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div/div/span').text
    if (lastOne != "" and lastOne == currentOne):
        print("Not found, skipping")
        continue

    lastOne = currentOne
    message_input = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
    msgs = ["""Hi """ + thisName + """,""",
    Keys.SHIFT + Keys.ENTER,
    """I am Hiya Jain, a second-year undergraduate student at IIT Mandi, contesting for the post of General Secretary.""",
    Keys.SHIFT + Keys.ENTER,
    Keys.SHIFT + Keys.ENTER,
    """In the two years I have spent in this college, I have judiciously utilized all available resources irrespective of the mode. I have held managerial positions in all three societies- Cultural, Literary and Technical as the Volunteer of PMC, Writing Club and E-Cell. Working in Ruvaan as the Sponsorship Head and event co-coordinator in addition to club positions and being the Cultural Secretary of Gauri Kund has enabled me to experience the administrative bottleneck.""",
    Keys.ENTER,
    """In my strong opinion, the need of the hour is a powerful voice, one that can put forth and fight for students' rights, and I truly believe I can be that voice. The ones who witnessed the open house know how successfully I tackled the questions and are also well aware of how exposure and the will to work, as well as the best use of opportunities available at hand indicates having a greater amount of experience.""",
    Keys.SHIFT + Keys.ENTER,
    Keys.SHIFT + Keys.ENTER,
    """Your vote matters a lot, cast it wisely. Above all, please do vote, that is the most important part.""",
    Keys.SHIFT + Keys.ENTER,
    Keys.SHIFT + Keys.ENTER,
    """Yours sincerely, Hiya Jain."""
    ]

    for msg in msgs:
       message_input.send_keys(msg)
 
    message_input.send_keys(Keys.ENTER)

    message_input.send_keys(Keys.CONTROL + "v")
    time.sleep(0.5)

    image_input = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]')
    image_input.send_keys(Keys.ENTER)
    time.sleep(0.2)

    print("Messages sent!")

print("Done")

# %% Quit
driver.quit()
