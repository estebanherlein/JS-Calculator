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
driver.find_element(By.ID, "number-1").click()
driver.find_element(By.ID, "plus").click()
driver.find_element(By.ID, "number-2").click()
driver.find_element(By.ID, "equals").click()
result = driver.find_element(By.ID, "screen")

# Run assertion
assert "3" in result.get_attribute('value')
print("Succesful assertion")
print("TEST 0: Addition of positive numbers")
driver.quit()
