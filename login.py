from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# Create a new instance of the web driver
driver = webdriver.Chrome()

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
        # print('-----------------------------')
        # print('Hint: Need to login for access CS network!')
        driver.get("http://cp.cs.cityu.edu.hk:16978/login.html?https://www.google.com.hk/")
        ele = driver.find_element_by_id('messageBox')
        if 'CityU CS Network Access Control' in ele.get_attribute('innerHTML'):
            # print('We are now at cs network portal login form page.')
            # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'modify')))
            driver.get("http://cp.cs.cityu.edu.hk:16978/loginform.html?https://www.google.com.hk/")
            username = driver.find_element_by_name("username")
            pw = driver.find_element_by_name("ctx_pass")
            with open('credential.txt') as f:
                content = f.readlines()
            # you may also want to remove whitespace characters like `\n` at the end of each line
            content = [x.strip() for x in content] 
            username.send_keys(content[0])
            pw.send_keys(content[1])
            driver.find_element_by_name("modify").click()
            print('-----------------------------')
            print('Congrats! You have just logged in. Happy surfing!')
            print('-----------------------------')
        driver.quit()
    except BaseException as e:
        print('Error. Please inspect the codes for automating login process.')
        driver.quit()