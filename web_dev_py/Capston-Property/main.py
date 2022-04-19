import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# - - - - - - - - - - - - - - - - - - - - - - -
import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
# ----------------------------------------------------------------------
GM_EMAIL = ""
GM_PASSWORD = ""
# -----------------------------------------------------------------------
chrome_driver_path = "C:\devlopment\chromedriver_win32\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# ------------------------------------------------------------------------------
GOOGLE_FORM_URL =  "https://docs.google.com/forms/d/e/1FAIpQLSdrN2opoGdkmg736Q9BUJ9GxmS7omxFU6nbeNXi5VEUg-epag/viewform?usp=sf_link"
PROPERTY_URL = "https://www.zillow.com/los-angeles-ca/3-_beds/3.0-_baths/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Los%20Angeles%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-119.49113923828125%2C%22east%22%3A-117.33232576171875%2C%22south%22%3A33.32323263138699%2C%22north%22%3A34.71321742140052%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12447%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A100000%2C%22max%22%3A600000%7D%2C%22mp%22%3A%7B%22min%22%3A421%2C%22max%22%3A2529%7D%2C%22beds%22%3A%7B%22min%22%3A3%7D%2C%22baths%22%3A%7B%22min%22%3A3%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A9%7D"
# ------------------------------------------------------------------------------
driver.get(GOOGLE_FORM_URL)
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(PROPERTY_URL, headers=header)
html = response.text
soup = BeautifulSoup(html, "html.parser")
# ----------------------------------------------------------------------------------
# Beautiful soup scrraping
# link
prop_link = soup.select(".list-card-top a")
pro_link_list = []

for link in prop_link:
    href = link["href"]
    print(href)
    if "http" not in href:
        pro_link_list.append(f"https://www.zillow.com{href}")
    else:
        pro_link_list.append(href)

# pro_link_list = [link.get("href") for link in prop_link]
# print(pro_link_list)

# price
prop_price = soup.select("div.list-card-price")
# pro_price_list = [price.text for price in prop_price]
pro_price_list = [price.get_text().split("+")[0] for price in prop_price if "$" in price.text]
print(pro_price_list)

prop_adress = soup.select("address.list-card-addr")
# pro_address_list = [address.text for address in prop_adress]
pro_address_list = [address.get_text().split(" | ")[-1] for address in prop_adress]
print(pro_address_list)

# property = {}
#
# for item in range(0, len(pro_address_list)):
#         property[item] = {
#         "link": pro_link_list[item],
#         "price": pro_price_list[item],
#         "address": pro_address_list[item]
#  }


# ----------------------------------------------------------------
# Automatated form fill by Selenium





for i in range(len(pro_link_list)):
    time.sleep(2)

    auto_pro_link = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # auto_pro_link.send_keys(property[item]["link"][item])

    auto_price_fill = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # auto_price_fill.send_keys(property[item]["price"][item])

    auto_fill_address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # auto_fill_address.send_keys(property[item]["address"][item])

    auto_pro_link.send_keys(pro_link_list[i])
    auto_price_fill.send_keys(pro_price_list[i])
    auto_fill_address.send_keys(pro_address_list[i])

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    time.sleep(2)
    sendAnother = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    sendAnother.click()

