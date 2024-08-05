from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://https://rahulshettyacademy.com/AutomationPractice/")


action= ActionChains(driver)
action.double_click()
action.drag_and_drop()
action.context_click()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()

