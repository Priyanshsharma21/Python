from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# -------------------Automation setup code-----------------------------------
crome_driver_path = Service("C:\devlopment\chromedriver_win32\chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=crome_driver_path, options=op)
# crome driver is the bridge which tells selenium to operate on
# ---------------------------------------------------------------------------
driver.get("https://www.amazon.in/MuscleBlaze-Performance-Informed-Certified-Chocolate/dp/B09QGCD8QK/?_encoding=UTF8&pd_rd_w=VMnPo&pf_rd_p=ee853eb9-cee5-4961-910b-2f169311a086&pf_rd_r=AQ7J1HJZW1G6GJA4Y6JZ&pd_rd_r=465155b4-17cf-43a7-bfa6-0979a742970e&pd_rd_wg=a0KBO&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1")
# price = driver.find_element(By.CSS_SELECTOR, "div.a-section.a-spacing-none.aok-align-center .a-offscreen")
price = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[1]')
print(price)

pp = driver.find_element(By.CSS_SELECTOR, "#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span.a-offscreen")
print(pp.text)





# driver.close() # close tab
driver.quit() # close window
