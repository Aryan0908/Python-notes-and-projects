from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:\Driver\chromedriver.exe")

driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys("Aryan")

l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("Sharma")

email = driver.find_element(By.NAME, "email")
email.send_keys("ryansharma09081990@gmail.com")

button = driver.find_element(By.CLASS_NAME, "btn")
button.click()


# driver.quit()