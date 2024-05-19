from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Note, to access XPATH: 
#1. Press Ctrl + Shift + C on your keyboard to open the Developer Tools in your browser.
#2. Move your mouse to the element for which you want the XPath.
#3. Look in the right pane of the Developer Tools to find the XPath of the selected element.

web = webdriver.Chrome()
web.get('google form link here')

time.sleep(2) #give url some time to render

#short paragraph 
Name = 'John' #your input
name=web.find_element(By.XPATH,'xpath of short paragraph answer here') 
name.send_keys(Name)

#multiple choice answer
category=web.find_element(By.XPATH,'xpath of clickable options')
time.sleep(2)
category.click()

# Time input
hour_xpath = 'XPath for the hour input' 
minute_xpath = 'XPath for the minute input'  

# Find the elements for hour, minute
hour_field = web.find_element(By.XPATH, hour_xpath)
minute_field = web.find_element(By.XPATH, minute_xpath)

# Enter the time values
hour_field.send_keys('17') #5pm = 17:00
time.sleep(2)
minute_field.send_keys('00')
time.sleep(2)

submit=web.find_element(By.XPATH,'xpath of submit button')
submit.click()

