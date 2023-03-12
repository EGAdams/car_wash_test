# Python script to open web page using selenium and chrome driver
# wait for the phone icon to appear and then click on it
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
# import chromedriver options
from selenium.webdriver.chrome.options import Options


#for headless browser use this arguments
chrome_options = Options()
chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome( options=chrome_options )
# open the web page
driver.get("https://www.floridascarwash.com")

# wait for the phone icon to appear and then click on it
try:
    # wait for the phone icon with id "floadingphone" to appear  
    driver.implicitly_wait( 3 )

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "floatingphone")))
    driver.find_element_by_id("floatingphone").click()

    # wait for the phone icon to appear and then click on it
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "floatingphone")))
    
    # might need to wait for the database write to complete
    time.sleep( 1 )

    # close the browser window after 5 seconds
    driver.close()

    print("Test Passed")

     # if we get here then we have not found the phone icon within 10 seconds so fail the test case 
except: 

     print("Test Failed")
