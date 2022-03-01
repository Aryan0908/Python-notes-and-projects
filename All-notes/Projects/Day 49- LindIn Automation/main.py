from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\Driver\chromedriver.exe")

driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London"
    "%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(5)

signin_tab = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
signin_tab.click()

time.sleep(3)

username_tab = driver.find_element(By.ID, "username")
username_tab.send_keys("9802aryan@gmail.com")

password_tab = driver.find_element(By.ID, "password")
password_tab.send_keys("7859804175Ayan.")

time.sleep(1)

login_tab = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
login_tab.click()

time.sleep(3)

jobs_tab = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")

for job in jobs_tab[0:3]:
    job.click()
    time.sleep(1)
    save_tab = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save_tab.click()
    time.sleep(1)