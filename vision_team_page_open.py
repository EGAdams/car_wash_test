#!/usr/bin/env python3
import os
import sys
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException

# allow imports from ~/car_wash_test
HOME_DIR = os.path.expanduser("~")
sys.path.append(f"{HOME_DIR}/car_wash_test")
from database_admin import DatabaseAdmin
import ip_check


def wait_for_alert_dismissal(driver, timeout=300):
    """Blocks until the JS alert has been dismissed by the user."""
    def _gone(drv):
        try:
            drv.switch_to.alert
            return False
        except NoAlertPresentException:
            return True
    WebDriverWait(driver, timeout).until(_gone)


def main():
    # 1) Clear database
    print("Clearing the database tables…")
    DatabaseAdmin().get_ready_for_test()

    # 2) Launch Chrome
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # 3) Navigate & dump source
        driver.get("https://www.visionteamrealestate.com")
        with open("page_source.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

        # 4) Click the phone button once
        WebDriverWait(driver, 60).until(
            lambda d: d.execute_script(
                "return window.getComputedStyle(document.getElementById('staticcallbutton')).display !== 'none';"
            )
        )
        btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "staticcallbutton"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        print("Clicking #staticcallbutton…")
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(5)  # allow DB sync

        # 5) Prepare input & send one message
        send_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "chatbot_send_airplane"))
        )

        now = datetime.now().strftime("%H:%M:%S")
        input_el = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "chatbot_input_text"))
        )
        input_el.click(); input_el.clear()
        input_el.send_keys(f"Test from programatically built browser at {now}")

        # 6) Alert → wait for YOU to click OK → send
        driver.execute_script(f"alert('Press OK to send the test message ({now}).');")
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        print(f"⚠️  Alert up for message @ {now} — click OK in browser…")
        wait_for_alert_dismissal(driver)

        send_btn.click()
        print(f"Sent one message @ {now}")

    except TimeoutException as te:
        print(f"⏰ Timeout waiting for element: {te}")
    except Exception as e:
        print(f"❌ Test Failed: {e}")
    finally:
        # leave browser open for manual testing
        print("\n✅ Script complete. Browser remains open for manual tests.")
        input("👉  Press ENTER when you're done to close everything…")
        driver.quit()

        # optional IP check after you close
        try:
            print("Running IP check verification…")
            ip_check.verify_ip_user()
            print("IP Check Test Passed")
        except Exception as ip_e:
            print(f"IP Check failed: {ip_e}")


if __name__ == "__main__":
    main()
