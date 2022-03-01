from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:\Driver\chromedriver.exe")

driver.get("https://orteil.dashnet.org/experiments/cookie/")


def cookieclick():
    for times in range(500):
        cookie = driver.find_element(By.ID, "cookie")
        cookie.click()


def buildings(total_cookies):
    try:
        cursor_tag = driver.find_element(By.ID, "buyCursor")
        cursor = int(cursor_tag.text.split("\n")[0].split(" ")[2])

        grandma_tag = driver.find_element(By.ID, "buyGrandma")
        grandma = int(grandma_tag.text.split("\n")[0].split(" ")[2])

        factory_tag  = driver.find_element(By.ID, "buyFactory")
        factory = int(factory_tag .text.split("\n")[0].split(" ")[2])

        mine_tag = driver.find_element(By.ID, "buyMine")
        mine = int(mine_tag.text.split("\n")[0].split(" ")[2])

        shipment_tag = driver.find_element(By.ID, "buyShipment")
        shipment = int(shipment_tag.text.split("\n")[0].split(" ")[2])

        alchemy_tag = driver.find_element(By.ID, "buyAlchemy lab")
        alchemy = int(alchemy_tag.text.split("\n")[0].split(" ")[2])

        portal_tag = driver.find_element(By.ID, "buyPortal")
        portal = int(portal_tag.text.split("\n")[0].split(" ")[2])

        machine_tag = driver.find_element(By.ID, "buyTime machine")
        machine = int(machine_tag.text.split("\n")[0].split(" ")[2])

    except ValueError:
        cursor_tag = driver.find_element(By.ID, "buyCursor")
        cursor = int(cursor_tag.text.split("\n")[0].split(" ")[2].replace(",", ""))

        grandma_tag = driver.find_element(By.ID, "buyGrandma")
        grandma = int(grandma_tag.text.split("\n")[0].split(" ")[2].replace(",", ""))

        factory_tag = driver.find_element(By.ID, "buyFactory")
        factory = int(factory_tag.text.split("\n")[0].split(" ")[2].replace(",", ""))

        mine_tag = driver.find_element(By.ID, "buyMine")
        mine = int(mine_tag.text.split("\n")[0].split(" ")[2].replace(",", ""))

        shipment_tag = driver.find_element(By.ID, "buyShipment")
        shipment = int(shipment_tag.text.split("\n")[0].split(" ")[2].replace(",", ""))

        alchemy_tag = driver.find_element(By.ID, "buyAlchemy lab")
        alchemy = int(alchemy_tag.text.split("\n")[0].split(" ")[3].replace(",", ""))

        portal_tag = driver.find_element(By.ID, "buyPortal")
        portal = int(portal_tag.text.split("\n")[0].split(" ")[2].replace(",", ""))

        machine_tag = driver.find_element(By.ID, "buyTime machine")
        machine = int(machine_tag.text.split("\n")[0].split(" ")[3].replace(",", ""))



    if total_cookies >= machine:
        product8 = driver.find_element(By.ID, "buyTime machine")
        product8.click()
    elif total_cookies >= portal:
        product7 = driver.find_element(By.ID, "buyPortal")
        product7.click()
    elif total_cookies >= alchemy:
        product6 = driver.find_element(By.ID, "buyAlchemy lab")
        product6.click()
    elif total_cookies >= shipment:
        product5 = driver.find_element(By.ID, "buyShipment")
        product5.click()
    elif total_cookies >= mine:
        product4 = driver.find_element(By.ID, "buyMine")
        product4.click()
    elif total_cookies >= factory:
        product3 = driver.find_element(By.ID, "buyFactory")
        product3.click()
    elif total_cookies >= grandma:
        product2 = driver.find_element(By.ID, "buyGrandma")
        product2.click()
    elif total_cookies >= cursor:
        product1 = driver.find_element(By.ID, "buyCursor")
        product1.click()

game = True

while game:
    cookieclick()

    time.sleep(0.5)

    count_tag = driver.find_element(By.ID, "money")

    try:
        count = int(count_tag.text)
    except ValueError:
        count = int(count_tag.text.replace(",", ""))


    buildings(total_cookies=count)
