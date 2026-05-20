import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID,"name").send_keys("name")
driver.find_element(By.ID,"alertbtn").click()
alert=driver.switch_to.alert
time.sleep(2)
alertText=alert.text
print(alertText)
alert.accept()#it will click on ok button
#alert.dismiss()
time.sleep(2)




