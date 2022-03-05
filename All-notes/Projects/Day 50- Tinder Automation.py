from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

driver = webdriver.Chrome("C:\Driver\chromedriver.exe")

driver.get(
    "https://tinder.com/")

time.sleep(2)

login_button = driver.find_element(By.XPATH,
                                   '//*[@id="q-1330521921"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

time.sleep(2)

try:
    facebook_login = driver.find_element(By.XPATH,
                                         '//*[@id="q1236064299"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    facebook_login.click()
except NoSuchElementException:
    options_button = driver.find_element(By.XPATH, '//*[@id="q1236064299"]/div/div/div[1]/div/div[3]/span/button')
    options_button.click()

    facebook_login = driver.find_element(By.XPATH,
                                         '//*[@id="q1236064299"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    facebook_login.click()

time.sleep(2)

original_window = driver.window_handles[0]
facebook_login = driver.window_handles[1]
driver.switch_to.window(facebook_login)

userid = driver.find_element(By.ID, 'email')
userid.send_keys("ryansharma09081990@gmail.com")

password = driver.find_element(By.ID, "pass")
password.send_keys("7859804175@Facebook.")

login_button = driver.find_element(By.NAME, "login")
login_button.click()

time.sleep(5)

driver.switch_to.window(original_window)

try:
    accept_button = driver.find_element(By.XPATH, '//*[@id="q-1330521921"]/div/div[2]/div/div/div[1]/div[1]/button')
    accept_button.click()
except NoSuchElementException:
    pass

time.sleep(1)

try:
    location_button = driver.find_element(By.XPATH, '//*[@id="q1236064299"]/div/div/div/div/div[3]/button[1]')
    location_button.click()
except NoSuchElementException:
    pass

time.sleep(1)

try:
    notification_button = driver.find_element(By.XPATH, '//*[@id="q1236064299"]/div/div/div/div/div[3]/button[2]')
    notification_button.click()
except NoSuchElementException:
    pass

time.sleep(6)

for _ in range(90):

    time.sleep(1)

    try:
        dislike_button = driver.find_element(By.XPATH,
                                             '//*[@id="q-1330521921"]/div/div[1]/div/div/main/div/div/div[1]/div/div[5]/div/div[4]/button')

        dislike_button.click()
    except ElementClickInterceptedException:
        try:
            match_button = driver.find_element(By.LINK_TEXT, "BACK TO TINDER")
            match_button.click()
        except NoSuchElementException:
            time.sleep(3)

