from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()
LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")
URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3637630487&distance=10&f_AL=true&f_E=2%2C3%2C4&f_JT=F&f_SB2=4&geoId=102571732&keywords=software%20engineer&location=New%20York%2C%20New%20York%2C%20United%20States&refresh=true&sortBy=R'
WINDOW_TIME = 60 * 60

# Initialize webdriver
driver = webdriver.Chrome()

# Define actions
actions = {
    "find_click": lambda x: driver.find_element(By.XPATH, x).click(),
    "find_write": lambda x, text: driver.find_element(By.XPATH, x).send_keys(text),
}

# Define handler for exceptions
def handle_exceptions(action, *args):
    try:
        actions[action](*args)
        return True
    except Exception as e:
        print(f"Element not found. Exception: {e}")
        return False

# Sign in
def sign_in():
    if handle_exceptions("find_click", '/html/body/div[1]/header/nav/div/a[2]'):
        if handle_exceptions("find_write", '//*[@id="username"]', LINKEDIN_EMAIL) and \
            handle_exceptions("find_write", '//*[@id="password"]', LINKEDIN_PASSWORD):
            if handle_exceptions("find_click", '//*[@id="organic-div"]/form/div[3]/button'):
                print("Signed in successfully")
                return True
    return False

# Navigate to URL
driver.get(URL)

# Start the script
start_time = time.time()
if sign_in():
    time.sleep(5)
    if handle_exceptions("find_click", '//button[contains(@class,"jobs-apply-button")]'):
        print("Clicked on jobs")

# Run for WINDOW_TIME duration
while time.time() - start_time < WINDOW_TIME:
    print(f"Program is running! Time remaining: {int((WINDOW_TIME - time.time() + start_time) / 60)} minutes and {int((WINDOW_TIME - time.time() + start_time) % 60)} seconds.")
    time.sleep(5)

driver.quit()
