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
driver = webdriver.Chrome()

driver.get("https://us04web.zoom.us/j/74265780536?pwd=L3MzbUpqb0RPZFRZaGRhRmRZdnZBUT09")
wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = 'Friends'

# Replace the below string with your own message
msg = "Message sent using python!"
input("Press Enter after scanning: ")

#%% after zoom setup and opening chat

text_area = driver.find_element_by_xpath('//*[@id="wc-container-right"]/div/div[2]/div[2]/div/div[2]/textarea')
text_area.send_keys("hello")
text_area.send_keys(Keys.CONTROL+"a")
text_area.send_keys(Keys.CONTROL+"x")
i=100
for i in range(i):
    text_area.send_keys(Keys.CONTROL+"v")
    text_area.send_keys(Keys.ENTER)
print("Done")
