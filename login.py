from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# Create a new instance of the web driver
driver = webdriver.Chrome('/usr/local/bin/chromedriver')

driver.get("https://www.google.com.hk")

try:
    # Insdie the page of https://www.google.com.hk, 
    # we should have an element of id 'gbwa'.
    # If there's no such element exist, we need to login.
    element_1 = driver.find_element_by_id('gbwa')
    print('-----------------------------')
    print('Status: Logged in.')
    print('Congrats! Happy surfing!')
    print('-----------------------------')
    driver.quit()
except NoSuchElementException:
    try:
        # driver.get("http://cp.cs.cityu.edu.hk:16978/login.html?https://www.google.com.hk/")
        # ele = driver.find_element_by_id('messageBox')
        # if 'CityU CS Network Access Control' in ele.get_attribute('innerHTML'):
        driver.get("http://cp.cs.cityu.edu.hk:16978/loginform.html")
        username = driver.find_element_by_name("username")
        pw = driver.find_element_by_name("ctx_pass")
        with open('/Users/pharrell/auto-login/credential.txt') as f:
            content = f.readlines()
        # remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content] 
        username.send_keys(content[0])
        pw.send_keys(content[1])
        driver.find_element_by_name("modify").click()
        print('-----------------------------')
        print('Congrats! You have just logged in. Happy surfing!')
        print('-----------------------------')
        driver.quit()
    except BaseException as e:
        print('Error: %s. \nPlease inspect the codes in ``login.py``.' % e)
        driver.quit()