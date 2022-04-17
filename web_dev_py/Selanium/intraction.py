from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# --------------------------------------------------------------------------
chrome_driver_path = "C:\devlopment\chromedriver_win32\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("http://secure-retreat-92358.herokuapp.com/")
# --------------------------------------------------------------------------
# click
# article_numbers = driver.find_element(By.CSS_SELECTOR, "#articlecount > a:nth-child(1)")
# # or
# click_portal = driver.find_element(By.LINK_TEXT, "All portals")
# click_portal.click()

# test
# type_in = driver.find_element(By.CSS_SELECTOR, "#searchInput")
# type_in.send_keys("Python")
# type_in.send_keys(Keys.ENTER)

# Sign up
fname = driver.find_element(By.CSS_SELECTOR, "body > form > input.form-control.top")
lname = driver.find_element(By.CSS_SELECTOR, "body > form > input.form-control.middle")
email = driver.find_element(By.CSS_SELECTOR, "body > form > input.form-control.bottom")
submit = driver.find_element(By.CSS_SELECTOR, "body > form > button")
fname.send_keys("Priyansh")
lname.send_keys("Sharma")
email.send_keys("piyuindia4@gmail.com")
submit.click()
