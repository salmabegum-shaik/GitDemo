import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Click Here").click()
time.sleep(2)
windowsOpen=driver.window_handles
driver.switch_to.window(windowsOpen[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
