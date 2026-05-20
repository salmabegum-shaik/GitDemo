from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://vinothqaacademy.com/mouse-event/")
actions1=ActionChains(driver)
double_click = driver.find_element(By.ID,"doubleBtn")
right_click=driver.find_element(By.ID,"rightBtn")
source=driver.find_element(By.ID,"dragItem")
target=driver.find_element(By.ID,"dropZone")
actions1.double_click(double_click).perform()
actions1.context_click(right_click).perform()
actions1.drag_and_drop(source,target)
hover=driver.find_element(By.CSS_SELECTOR,".tooltip-container")
actions1.move_to_element(hover).perform()
slider=driver.find_element(By.ID,"handle_max")
actions1.click_and_hold(slider).move_by_offset(200, 0).release().perform()
actions1.drag_and_drop_by_offset(slider, 200, 0).perform()