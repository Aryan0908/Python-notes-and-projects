from selenium import webdriver
from selenium.webdriver.common.by import By

# Getting the driver path
chrome_driver = "C:\Driver\chromedriver.exe"

# Specifying driver in selenium
driver = webdriver.Chrome(executable_path=chrome_driver)

# Opening the site
driver.get("https://www.python.org/")

# Selecting by id
# id = driver.find_element_by_id("id_of the element")

# Selecting  by name
name = driver.find_element_by_name("q")
name.get_attribute("placeholder")

# Selecting bby class
class_ = driver.find_element_by_class_name("python_logo")

# Selecting by css selector
selector = driver.find_element_by_css_selector(".document-widget a")
print(selector.text)


# Closing a single tab
driver.close()

# Closing the whole browser
driver.quit()