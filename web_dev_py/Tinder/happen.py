import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


GM_EMAIL = ""
GM_PASSWORD = ""


chrome_driver_path = "C:\devlopment\chromedriver_win32\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://happn.app/")

# signin
time.sleep(5)
sign = driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div/div[1]/div")
sign.click()

time.sleep(5)
google = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[2]/div/div[1]/div[4]")
google.click()

time.sleep(1)
iAgree = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[2]/div/div[2]/button")
iAgree.click()

time.sleep(4)
iAccept = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[2]/div/div[2]/button[1]")
iAccept.click()

time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

#Login and hit enter
email = driver.find_element(By.XPATH, '//*[@id="email"]')
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
time.sleep(2)
email.send_keys(GM_EMAIL)
time.sleep(2)
password.send_keys(GM_PASSWORD)
time.sleep(2)
password.send_keys(Keys.ENTER)

#Switch back to Tinder window
driver.switch_to.window(base_window)

time.sleep(15)
reject = driver.find_element(By.CSS_SELECTOR, "#root > div > div.sc-kzXxXt.kspdSV > div > div.sc-ksLacT.cPuZdq > div.sc-gObXHz.dsXSBV > div.sc-gtbgjk.sc-OxKgF.hycFgX.ftkjlh")
reject.click()
time.sleep(1)
yes = driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div[2]/div/button")
yes.click()

while True:
    time.sleep(1)
    allReject = driver.find_element(By.CSS_SELECTOR, "#root > div > div.sc-kzXxXt.kspdSV > div > div.sc-ksLacT.cPuZdq > div.sc-gObXHz.dsXSBV > div.sc-gtbgjk.sc-OxKgF.hycFgX.ftkjlh")
    allReject.click()

