#chromedriver linux install guide
#https://www.gregbrisebois.com/posts/chromedriver-in-wsl2/


#To run Selenium and chromedriver in WSL without opening a browser, 
#you can use Chrome in headless mode. 

############################################ GO YOU.COM !! #############################################
#
#  Headless mode enables you to run Chrome without the need for a graphical user interface. 
#  This is useful for running automated tests and scraping websites,
#  as it allows you to run Chrome in a virtual environment without the need for a display server.
#  Headless mode is available in Chrome 59 and later.
#  https://developers.google.com/web/updates/2017/04/headless-chrome
#  https://www.gregbrisebois.com/posts/chromedriver-in-wsl2/
#
########################################################################################################

#Here's an example code snippet that demonstrates how to set up 
#Selenium and chromedriver to run Chrome in headless mode on WSL:

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')

# This is the path to the chromedriver binary
chromedriver_path = '/usr/local/bin/chromedriver'

# Set up the webdriver object
driver = webdriver.Chrome(chromedriver_path,
                          options=chrome_options)

# Replace this URL with the website you want to scrape
url = 'http://www.example.com'

# Navigate to the website
driver.get(url)

# Perform any scraping/automation tasks here

# Close the webdriver
driver.quit()

#This code uses the webdriver module from Selenium to set up the chromedriver binary 
# and the chrome_options object to run Chrome in headless mode. 
# It then navigates to the specified URL and performs any scraping or automation tasks required. 
# Finally, it quits the webdriver instance to clean up any resources that were allocated.
#
# Note that in order to use this code, you'll need to have Chrome 
# and chromedriver installed in your WSL environment. 
# You can do this by following the steps in the documentation for your Linux distribution.


# I accidentaly discovered this by trying to open the visible browser window
# We don't need a visible browser window to run the test !!!