import time

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
SIMILAR_ACCOUNT = "derricchew"
INSTA_EMAIL = "piyuindia4@gmail.com"
INSTA_PASSWORD = "Piyu@412002"

chrome_driver_path = "C:\devlopment\chromedriver_win32\chromedriver"

class Instagram:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)


    def login(self):
        self.driver.implicitly_wait(10)

        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        email = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.send_keys(INSTA_EMAIL)

        time.sleep(1)

        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(INSTA_PASSWORD)

        time.sleep(1)

        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login.click()







    def find_followers(self):
        time.sleep(3)
        find = self.driver.find_element(By.CSS_SELECTOR, '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.QY4Ed.P0xOK > input')
        find.send_keys(SIMILAR_ACCOUNT)

        time.sleep(2)
        zen_priyansh = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')
        zen_priyansh.click()








    def follow(self):
        time.sleep(1)
        following = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/div')
        following.click()

        time.sleep(2)
        follow_list = self.driver.find_elements(By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN > div > div > div > div.isgrP > ul > div > li > div button')

        for follow in follow_list:

            try:
                follow.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()





insta = Instagram(chrome_driver_path)
insta.login()
insta.find_followers()
insta.follow()
