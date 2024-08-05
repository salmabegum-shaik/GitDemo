import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radiobuttons = driver.find_elements(By.CSS_SELECTOR,".radioButton")
for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio2":
       radiobutton.click()
       time.sleep(2)
       radiobutton.is_selected()
       assert  radiobutton.is_selected()
       break

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
assert driver.find_element(By.CSS_SELECTOR,"#displayed-text")
driver.find_element(By.CSS_SELECTOR,"#hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()



