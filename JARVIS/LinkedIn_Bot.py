from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
# ------------------------------------------------------------
chrome_driver_path = "C:\devlopment\chromedriver_win32\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
URL = "https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1&geoId=104994045&keywords=python%20developer&location=Moscow%20City%2C%20Russia"


EMAIL = ""
PASSWORD = ""
driver.get(URL)
# ------------------------------------------------------------------
# sign in
time.sleep(3)
login_btn = driver.find_element(By.CSS_SELECTOR, "body > div.cta-modal.show > a.cta-modal__primary-btn")
login_btn.click()

time.sleep(3)
email_inp = driver.find_element(By.CSS_SELECTOR, "#username")
email_inp.send_keys(EMAIL)

time.sleep(3)
password_inp = driver.find_element(By.CSS_SELECTOR, "#password")
password_inp.send_keys(PASSWORD)

time.sleep(3)
sign_in_btn = driver.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button")
sign_in_btn.click()


# apply for job
time.sleep(2)
list_of_jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")


for company in list_of_jobs:
    print("Click")
    company.click()
    time.sleep(2)

    try:
        goto_btn = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        goto_btn.click()
        time.sleep(5)

        inp_no = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        if inp_no.text == "":
            inp_no.send_keys("")

        # If the submit_button is a "Next" button, then this is a multistep application, so skip.
        submit_application = driver.find_element(By.CSS_SELECTOR, "footer button")
        if submit_application.get_attribute("data-control-name") =="continue_unify":
            close_button = driver.find_element(By.CSS_SELECTOR, "artdeco-button__icon")[1]
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_application.click()

        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-button__text")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue













time.sleep(5)
driver.quit()
