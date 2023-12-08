from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

# Set options for not prompting DevTools information
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Get to the application in the local server
print("testing started")
driver = webdriver.Chrome(options=options)
driver.get("http://127.0.0.1/testMe")
sleep(1)
driver.find_element(By.ID, "clear").click()

# Test the addition feature with positive numbers
driver.find_element(By.ID, "number-3").click()
driver.find_element(By.ID, "minus").click()
driver.find_element(By.ID, "number-1").click()
driver.find_element(By.ID, "equals").click()
result = driver.find_element(By.ID, "screen")
print(result.get_attribute('value'))

# Run assertion
assert "2" in result.get_attribute('value')
print("Succesful assertion")
print("TEST 1: Substraction of Positive Numbers")
driver.quit()
