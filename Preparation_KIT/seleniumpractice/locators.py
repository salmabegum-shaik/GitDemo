import time

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("salma")
driver.find_element(By.NAME,"email").send_keys("Salmabegumshaik@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("sallulllll")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR,'#inlineRadio1').click()
#static dropdown
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)
#dropdown.select_value()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message=driver.find_element(By.CLASS_NAME,"alert").text
print(message)
assert "success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("hdhdhdh")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()


time.sleep(2)
