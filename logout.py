import time
from selenium import webdriver

# Create a new instance of the web driver
driver = webdriver.Chrome()

driver.get("http://cp.cs.cityu.edu.hk:16978/logout.html")
driver.quit()
print('-----------------------------')
print('You have logged out.')
print('-----------------------------')