from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = "C:\devlopment\chromedriver_win32\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

event_dates = driver.find_elements(By.CSS_SELECTOR, "div.medium-widget.event-widget.last > div > ul > li > time")
event_name = driver.find_elements(By.CSS_SELECTOR,"#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li > a")

# events = {}
events = {i:{"time" : event_dates[i].text, "event": event_name[i].text}for i in range(len(event_dates))}
print(events)
# for i in range(0, len(event_dates)):
#     events[i] = {
#         "event": event_name[i].text,
#         "time" : event_dates[i].text,
#     }

print(events)

driver.quit()
