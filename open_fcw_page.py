# Python script to open web page using selenium and chrome driver
# wait for the phone icon to appear and then click on it
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os, sys
# import chromedriver options
from selenium.webdriver.chrome.options import Options

HOME_DIR = os.path.expanduser( "~" )
sys.path.append( f"{ HOME_DIR }/car_wash_test" )
from database_admin import DatabaseAdmin
import ip_check


print( "clearing the database tables... " )
db_admin = DatabaseAdmin()
db_admin.get_ready_for_test()


#for headless browser use this arguments
chrome_options = Options()
# Comment out headless mode for debugging to see the browser window
# chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome( options=chrome_options )
# open the web page
driver.get("https://www.visionteamrealestate.com")
with open("page_source.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

# wait for the phone icon to appear and then click on it
try:
    # wait for the phone icon with id "floadingphone" to appear  
    driver.implicitly_wait( 3 )

    print ( "waiting for floatingphone element to be present..." )
    # Check if the element with id "staticcallbutton" exists and print its display style
    exists = driver.execute_script('return document.getElementById("staticcallbutton") !== null;')
    display_style = driver.execute_script('var el = document.getElementById("staticcallbutton"); return el ? window.getComputedStyle(el).display : "not found";')
    print(f"'staticcallbutton' exists: {exists}, display style: {display_style}")

    # Trigger the database_sync_started event on #staticcallbutton to make it visible
    driver.execute_script('jQuery("#staticcallbutton").trigger("database_sync_started");')

    # Wait up to 60 seconds for the display style of staticcallbutton to become not "none"
    WebDriverWait(driver, 60).until(lambda d: d.execute_script('return window.getComputedStyle(document.getElementById("staticcallbutton")).display !== "none";'))

    # Wait for the container with id "staticcallbutton" to be visible
    container = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "staticcallbutton")))
    # Then find the floatingphone element inside the container
    # Change click target to staticcallbutton to trigger click handler properly
    element = container
    # Wait for the staticcallbutton element to be clickable
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "staticcallbutton")))
#     print(f"Element tag name: {element.tag_name}")
#     print(f"Element location: {element.location}")
#     print(f"Element size: {element.size}")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    driver.save_screenshot("before_js_click.png")
    print("Clicking element using JavaScript click...")
    driver.execute_script("arguments[0].click();", element)
    driver.save_screenshot("after_js_click.png")

    # Check the display style of the floatingphone element after click
    display_style = driver.execute_script("return window.getComputedStyle(arguments[0]).display;", element)
    print(f"Display style of 'floatingphone' element after click: {display_style}")

    # might need to wait for the database write to complete
    SLEEP_AFTER_CLICK = 5
    print( f"sleeping { SLEEP_AFTER_CLICK } seconds after click to wait for database write..." )
    time.sleep( SLEEP_AFTER_CLICK )

    print( "closing the driver..." )
    driver.close()

    # Run IP check verification
    print( "Running IP check verification..." )
    ip_check.verify_ip_user()
    print( "Test Passed" )

     # if we get here then we have not found the phone icon within 10 seconds so fail the test case
except Exception as e:
     # print exception text
     print(f"Test Failed: {e}")
