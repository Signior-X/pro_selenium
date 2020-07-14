# %%
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

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

# %% The main cell
while(True):

    target = input("Enter the target (_cancel for stop) : ")
    # target = "Rashmi"
    # input("Press Enter")
    if(target == '_cancel'):
        break
    print("Target set")

    # For the searching ans automatically selecting the first one
    search_box = driver.find_element_by_class_name('_2S1VP')
    search_box.send_keys(target + Keys.ENTER)
    print(search_box)

    main_content_holder = driver.find_element_by_tag_name('footer')
    message_input = main_content_holder.find_element_by_class_name('_2S1VP')

      # msg = input("Enter the message to be sent: ")
      # msg = "test"

    count = int(input("Enter the count: "))

    for i in range(count):
        message_input.send_keys(Keys.CONTROL + "v")
        # message_input.send_keys(' '+str(i))
        message_input.send_keys(Keys.ENTER)
    

    print("Messages sent!")

print("Done")
# Nirlaj to vo hai jo kaayaro ki bhati yudh chhor ke bhag jaate hai

#%% Updated one (Copy text which to be send)
while(True):

    target = input("Enter the target (Empty for stop) : ")
    # target = "Rashmi"
    # input("Press Enter")
    if(target == ''):
        break
    print("Target set", target)

    # For the searching ans automatically selecting the first one
    search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_box.send_keys(target + Keys.ENTER)
    print(search_box)

    message_input = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    msg = input("Enter the message to be sent: ")
    # msg = "test"


    count = int(input("Enter the count: "))

    for i in range(count):
        message_input.send_keys(msg)
        # message_input.send_keys(' '+str(i))
        message_input.send_keys(Keys.ENTER)
    

    print("Messages sent!")

print("Done")
# Happy Birthday Naresh

#%% Pattern Birthday Wish
while(True):

    target = input("Enter the target (Empty for stop) : ")
    # target = "Rashmi"
    # input("Press Enter")
    if(target == ''):
        break
    print("Target set", target)

    # For the searching ans automatically selecting the first one
    search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_box.send_keys(target + Keys.ENTER)
    print(search_box)

    message_input = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

      # msg = input("Enter the message to be sent: ")
      # msg = "test"

    wishMsg = input("Enter the name only: ")
    if(wishMsg == ''):
        continue
    wishMsg = 'Happy Birthday ' + wishMsg
    print(wishMsg)
    
    i=1
    while(i<=len(wishMsg)):
        message_input.send_keys(wishMsg[:i])
        message_input.send_keys(Keys.ENTER)
        i+=1
    print("Messages sent!")

print("Done")
# Happy Birthday Naresh

#%% Pattern message
while(True):

    target = input("Enter the target (Empty for stop) : ")
    # target = "Rashmi"
    # input("Press Enter")
    if(target == ''):
        break
    print("Target set", target)

    # For the searching ans automatically selecting the first one
    search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_box.send_keys(target + Keys.ENTER)
    print(search_box)

    message_input = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

      # msg = input("Enter the message to be sent: ")
      # msg = "test"

    wishMsg = input("Enter the message: ")
    if(wishMsg == ''):
        continue
    print(wishMsg)
    
    i=1
    while(i<=len(wishMsg)):
        message_input.send_keys(wishMsg[:i])
        message_input.send_keys(Keys.ENTER)
        i+=1
    print("Messages sent!")

print("Done")
# Happy Birthday Naresh

# %% Quit
driver.quit()
