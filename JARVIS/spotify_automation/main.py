
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


# ------------------------------------------------------------


class Spotify():
    def __init__(self):
        self.driver = "C:\devlopment\chromedriver_win32\chromedriver"

    def login(self, songreq):
        driver = webdriver.Chrome(executable_path=self.driver)
        URL = "https://accounts.spotify.com/en/login"
        driver.get(URL)
        time.sleep(2)
        femail = driver.find_element(By.XPATH, '//*[@id="login-username"]')
        femail.send_keys('piyuindia4@gmail.com')
        fpass = driver.find_element(By.XPATH, '//*[@id="login-password"]')
        fpass.send_keys('Piyu@412002')
        submit = driver.find_element(By.XPATH, '//*[@id="login-button"]/div[1]/p')
        submit.click()
        time.sleep(2)
        webplayer = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/button[2]')
        webplayer.click()
        time.sleep(5)

# search
        fsearch = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/nav/div[1]/ul/li[2]/a/span')
        fsearch.click()
        search_song = driver.find_element(By.XPATH,
                                          '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/form/input')
        search_song.send_keys(songreq)
        time.sleep(4)
        song = driver.find_element(By.XPATH,
                                   '//*[@id="searchPage"]/div/div/section[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/button')
        song.click()
        song.send_keys(Keys.ENTER)


# spotify = Spotify()
# spotify.login("company")



