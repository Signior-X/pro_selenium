# %%
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyttsx3

# %%
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


    # message_input = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    message_input_voice=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/div/span/button')
      # msg = input("Enter the message to be sent: ")
      # msg = "test"
    
    engine=pyttsx3.init()

    count = int(input("Enter the count: "))
    message_input_voice.click()
    for i in range(count):
        # message_input.send_keys(Keys.CONTROL + "v")
        # message_input.send_keys(' '+str(i))
        # message_input.send_keys(Keys.ENTER)
        
        engine.say("Hi")
        engine.runAndWait()
        

    print("Messages sent!")

print("Done")
# Happy Birthday Naresh


# %%