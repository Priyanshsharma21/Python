from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# ----------------------------------------------------------------------

chrome_driver_path = "C:\devlopment\chromedriver_win32\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
URL = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(URL)
# ----------------------------------------------------------------------
# cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
#
#
# #Get upgrade item ids.
# items = driver.find_elements(By.CSS_SELECTOR, "#store div")
# item_ids = [item.get_attribute("id") for item in items]
#
# # time
# timeout = time.time() + 5
# five_min = time.time() + 60*5 # 5minutes
#
# while True:
#     cookie.click()
#
#     if time.time() > timeout:
#         # Get all upgrade <b> tags
#         all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
#         item_prices = []
#
#         for price in all_prices:
#             ele_text = price.text
#             if ele_text != "":
#                 cost = int(ele_text.split("-")[1].strip().replace(",", ""))
#                 item_prices.append(cost)
#
#         # Create dictionary of store items and prices
#         cookie_upgrade = {}
#         for n in range(len(item_prices)):
#             cookie_upgrade[item_prices[n]] = item_ids[n]
#
#
#         # get current cookie count
#         money_element = driver.find_element(By.CSS_SELECTOR, "#money").text
#         if "," in money_element:
#             money_element = money_element.replace(",", "")
#         cookie_count = int(money_element)
#
#         # Find upgrades that we can currently afford
#         affordable_upgrades = {}
#         for cost, id in cookie_upgrade.items():
#             if cookie_count > cost:
#                 affordable_upgrades[cost] = id
#
#          # Purchase the most expensive affordable upgrade
#         highest_price_affordable_upgrade = max(affordable_upgrades)
#         print(highest_price_affordable_upgrade)
#         to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
#
#         driver.find_element(By.ID, to_purchase_id).click()
#
#         # Add another 5 seconds until the next check
#         timeout = time.time() + 5
#
#     # After 5 minutes stop the bot and check the cookies per second count.
#     if time.time() > five_min:
#         cookie_per_s = driver.find_element(By.ID, "cps").text
#         print(cookie_per_s)
#         break

time_to_buy = time.time() + 5
stop_time = time.time() + 5 * 60

while True:
    cookie = driver.find_element(by=By.ID, value="cookie")
    cookie.click()

    if time.time() >= time_to_buy:
        store_items = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        not_available = driver.find_elements(by=By.CSS_SELECTOR, value=".grayed b")
        available = [item for item in store_items if item not in not_available]

        for item in available[::-1]:
            item.click()
            break

        time_to_buy = time.time() + 5

    if time.time() >= stop_time:
        cps = driver.find_element(by=By.ID, value="cps").text
        print(cps)
        break







driver.quit()