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

driver.get("https://us04web.zoom.us/j/79938903843?pwd=N2JOcnFCTC9CZi9zclVER0E3STN6UT09")
wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = 'Friends'

# Replace the below string with your own message
msg = "Message sent using python!"
input("Press Enter after scanning: ")


# %% SEnd mesages by class of text area

text_area_by_class = driver.find_element_by_class_name('chat-box__chat-textarea')
text_area_by_class.send_keys('kal meri saadhi pr juice gira tha')
text_area_by_class.send_keys(Keys.ENTER)
text_area_by_class.send_keys('Aur main dobara nahane gayi thi')
text_area_by_class.send_keys(Keys.ENTER)
text_area_by_class.send_keys('Tumm chane cooker me chadhakar mere pass ayi thi tab rasode mei Kaun tha?')
text_area_by_class.send_keys(Keys.ENTER)
text_area_by_class.send_keys('wahaa kaun tha?')
text_area_by_class.send_keys(Keys.ENTER)
text_area_by_class.send_keys('main thi? tum thi? mai thi? tum thi? kaun tha?')
text_area_by_class.send_keys(Keys.ENTER)
text_area_by_class.send_keys('Kaun Tha?')
text_area_by_class.send_keys(Keys.ENTER)
text_area_by_class.send_keys('KAUN THA?')
text_area_by_class.send_keys(Keys.ENTER)
text_area_by_class.send_keys('*****************')
text_area_by_class.send_keys(Keys.ENTER)

## RENAME
action = ActionChains(driver)
firstLevelMenu = driver.find_element_by_id("participants-list-0")
action.move_to_element(firstLevelMenu).perform()
#  Rename button click onluy after the previous one
rename_button = driver.find_element_by_xpath('//*[@id="participants-list-0"]/div[2]/div/div/button')
rename_button.click()
# Rename send keys and submit
rename_input = driver.find_element_by_xpath('//*[@id="newname"]')
rename_input.send_keys(Keys.CONTROL + 'a')
rename_input.send_keys("Gopi Bahu")
rename_input.send_keys(Keys.ENTER)

time.sleep(2)
text_area_by_class = driver.find_element_by_class_name('chat-box__chat-textarea')
text_area_by_class.send_keys('Rashi Ben')
text_area_by_class.send_keys(Keys.ENTER)
text_area_by_class.send_keys('**************')
text_area_by_class.send_keys(Keys.ENTER)

time.sleep(2)
## RENAMe
action = ActionChains(driver)
firstLevelMenu = driver.find_element_by_id("participants-list-0")
action.move_to_element(firstLevelMenu).perform()
#  Rename button click onluy after the previous one
rename_button = driver.find_element_by_xpath('//*[@id="participants-list-0"]/div[2]/div/div/button')
rename_button.click()
# Rename send keys and submit
rename_input = driver.find_element_by_xpath('//*[@id="newname"]')
rename_input.send_keys(Keys.CONTROL + 'a')
rename_input.send_keys("Kokila")
rename_input.send_keys(Keys.ENTER)


text_area_by_class = driver.find_element_by_class_name('chat-box__chat-textarea')
text_area_by_class.send_keys('Ye Rashi')
text_area_by_class.send_keys(Keys.ENTER)
text_area_by_class.send_keys('Cooker mei se chane nikal diye')
text_area_by_class.send_keys(Keys.ENTER)
text_area_by_class.send_keys('Aur Khaali Cooker gas par Chadha diya')
text_area_by_class.send_keys(Keys.ENTER)
text_area_by_class.send_keys('CHADHA DIYA!')
text_area_by_class.send_keys(Keys.ENTER)
text_area_by_class.send_keys('CHADHA DIYA!!')
text_area_by_class.send_keys(Keys.ENTER)

