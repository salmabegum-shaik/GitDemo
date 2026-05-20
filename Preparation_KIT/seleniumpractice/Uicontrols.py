import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        time.sleep(2)
        checkbox.is_selected() #it will return true or false after checking the checkbox is selected or not
        assert checkbox.is_selected()
        break

