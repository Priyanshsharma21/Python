import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "piyuindia4@gmail.com"
TWITTER_PASSWORD = "Piyu@412002"


chrome_driver_path = "C:\devlopment\chromedriver_win32\chromedriver"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        go = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        go.click()
        time.sleep(60)
        downlode_speed = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        self.down = float(downlode_speed.text)
        uplode_Speed = self.driver.find_element(By.XPATH,
                                                  "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span")
        self.up = float(uplode_Speed.text)
        print(self.up)
        print(self.down)

    def tweet_at_provider(self):
        self.driver.implicitly_wait(10)

        self.driver.maximize_window()
        self.driver.get("https://twitter.com/login")

        self.driver.implicitly_wait(4)
        sleep(2)
        username = self.driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_EMAIL)
        self.driver.implicitly_wait(4)
        sleep(2)

        next_button = self.driver.find_element(By.XPATH,
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span')
        next_button.click()
        self.driver.implicitly_wait(10)
        sleep(2)

        try:
            auth = self.driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            auth.send_keys("7999937157")
            self.driver.implicitly_wait(4)
            sleep(2)
        except NotImplementedError:
            pass
        else:
            next_button = self.driver.find_element(By.XPATH,
                                                   '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div')
            next_button.click()
            self.driver.implicitly_wait(10)
            sleep(2)

            password = self.driver.find_element(By.XPATH,
                                                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(TWITTER_PASSWORD)
            self.driver.implicitly_wait(10)
            sleep(2)

            password.send_keys(Keys.ENTER)
            self.driver.implicitly_wait(10)
            sleep(2)

            time.sleep(5)
            tweet = self.driver.find_element(By.XPATH,
                                             "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
            tweet.send_keys(
                f"hey @airtelindia why is my internet speed {self.down}/Down, {self.up}/Up when I pay for {PROMISED_DOWN}/Down, {PROMISED_UP}/Up")

            send_tweet = self.driver.find_element(By.XPATH,
                                                  '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
            send_tweet.click()




bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweet_at_provider()