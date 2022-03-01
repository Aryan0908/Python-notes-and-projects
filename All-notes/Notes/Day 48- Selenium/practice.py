from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:\Driver\chromedriver.exe")

driver.get("https://www.python.org/")

events_name_tag = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")
event_names = []

for names in events_name_tag:
    event_names.append(names.text)

time_name_tag = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu time")
event_time = []

for time in time_name_tag:
    text = time.text
    split = text.split("T")
    event_time.append(split[0])

time_and_event = {}

for number in range(0, len(event_names)):
    time_and_event[number] = {"time": event_time[number], "event": event_names[number]}

print(time_and_event)


driver.quit()
