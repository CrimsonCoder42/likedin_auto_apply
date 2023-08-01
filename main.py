from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
import time
import os


load_dotenv()

LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")

URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3637630487&distance=10&f_AL=true&f_E=2%2C3%2C4&f_JT=F&f_SB2=4&geoId=102571732&keywords=software%20engineer&location=New%20York%2C%20New%20York%2C%20United%20States&refresh=true&sortBy=R'
WINDOW_TIME = 60 * 60
driver = webdriver.Chrome()
driver.get(URL)

start_time = time.time()
# setup webdriver

#define your functions


def find_click_xpath(x):
    try:
        main_btn = driver.find_element(By.XPATH, x)
        main_btn.click()
        print("Button found and clicked")
        return True
    except Exception as e:
        print("Element not found ", e)
        return False


def find_click_class_name(x):
    try:
        main_btn = driver.find_element(By.CLASS_NAME, x)
        main_btn.click()
        print("Button found and clicked")
        return True
    except Exception as e:
        print("Element not found ", e)
        return False


def find_write_xpath(x, text):
    try:
        main_input = driver.find_element(By.XPATH, x)
        main_input.send_keys(text)
        print("input found and text entered")
        return True
    except Exception as e:
        print("Element not found ", e)
        return False


def sign_in_auto():
    try:
        fill_email = find_write_xpath('//*[@id="username"]', LINKEDIN_EMAIL)
        fill_password = find_write_xpath('//*[@id="password"]', LINKEDIN_PASSWORD)
        if fill_email and fill_password:
            submit = find_click_xpath('//*[@id="organic-div"]/form/div[3]/button')
            if submit:
                print("Signed in")
                return True
    except Exception as e:
        print("Element not found ", e)
        return False

# sign in 1
first_signin = find_click_xpath('/html/body/div[1]/header/nav/div/a[2]')
print("first sign in", first_signin)
# sign in 2
if first_signin:
    second_sign = sign_in_auto()
    if second_sign:
        print("second sign in", second_sign)
        time.sleep(5)
        if find_click_class_name('jobs-apply-button'):
            print("clicked on jobs")





while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    minutes_left = int(WINDOW_TIME - elapsed_time) // 60
    seconds_left = int((WINDOW_TIME - elapsed_time) % 60)

    if elapsed_time > WINDOW_TIME:
        break

    print(f"Program is running! {minutes_left}:{seconds_left} left.")


    time.sleep(5)


driver.quit()



