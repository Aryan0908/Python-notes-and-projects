from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import os


def write(tag, content):
    for word in content:
        tag.send_keys(word)
        time.sleep(0.3)


PROMISED_SPEED = 100
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")

# Getting the driver path
chrome_driver = "C:\Driver\chromedriver.exe"

# Specifying driver in selenium
driver = webdriver.Chrome(executable_path=chrome_driver)


class InternetSpeedBot:

    def __init__(self, sel_driver, down):
        self.ookla = sel_driver
        self.twitter = sel_driver
        self.current_down_speed = 0
        self.current_up_speed = 0

    def get_internet_speed(self):
        self.ookla.get("https://www.speedtest.net/")
        go_button = self.ookla.find_element(By.XPATH,
                                            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()

        time.sleep(130)
        print("times up")
        down_speed_tag = self.ookla.find_element(By.XPATH,
                                                 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        down_speed = float(down_speed_tag.text)
        self.current_down_speed = down_speed

        up_speed_tag = self.ookla.find_element(By.XPATH,
                                               '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        up_speed = float(up_speed_tag.text)
        self.current_up_speed = up_speed

    def tweet_at_provider(self):
        if self.current_down_speed < 100:
            self.twitter.get("https://twitter.com/")

            time.sleep(2)

            sign_in = self.twitter.find_element(By.XPATH,
                                                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
            sign_in.click()

            time.sleep(3)

            email_id = self.twitter.find_element(By.NAME, "text")
            write(tag=email_id, content=TWITTER_EMAIL)

            next_button = self.twitter.find_element(By.XPATH,
                                                    '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div')
            next_button.click()

            time.sleep(3)

            # try:
            username = self.twitter.find_element(By.NAME, "text")
            write(tag=username, content="@Aryan092002")

            time.sleep(1)

            next_button_2 = self.twitter.find_element(By.XPATH,
                                                      '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span')
            next_button_2.click()
            # except NoSuchElementException:
            #     pass

            time.sleep(2)

            password = self.twitter.find_element(By.NAME, "password")
            write(tag=password, content=TWITTER_PASSWORD)

            login_button = self.twitter.find_element(By.XPATH,
                                                     '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/span/span')
            login_button.click()

            time.sleep(3)

            complaint = self.twitter.find_element(By.XPATH,
                                                  '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
            complaint_content = f"Hey, Airtel. Why am I getting {self.current_down_speed}(down) and {self.current_up_speed}" \
                                f"(up), when I subscribed to 100mbps plan"
            write(tag=complaint, content=complaint_content)

            time.sleep(2)

            tweet_button = self.twitter.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
            tweet_button.click()
        else:
            pass


bot = InternetSpeedBot(sel_driver=driver, down=PROMISED_SPEED)
bot.get_internet_speed()
bot.tweet_at_provider()
