import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chromeoptions=webdriver.ChromeOptions()
chromeoptions.add_argument("headless")
chromeoptions.add_argument("--ignore-certificate-errors")

driver=webdriver.Chrome(options=chromeoptions)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")#scroll to the bottom
driver.get_screenshot_as_file("screen.png")