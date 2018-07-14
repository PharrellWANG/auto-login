import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# Create a new instance of the web driver
driver = webdriver.Chrome()

driver.get("http://cp.cs.cityu.edu.hk:16978/logout.html")
driver.quit()
print('-----------------------------')
print('You have logged out.')
print('-----------------------------')