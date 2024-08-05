import time

#import srvice
from selenium import webdriver

#service("")

driver=webdriver.Chrome()
driver.get('https://rahulshettyacademy.com')
print(driver.current_url)
print(driver.title)
print(driver.maximize_window())
time.sleep(2)