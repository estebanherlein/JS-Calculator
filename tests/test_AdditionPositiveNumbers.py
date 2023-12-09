from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import unittest

class AdditionTest(unittest.TestCase):

	# Get to the application in the local server
	def test_additionOfPositiveNumbers(self):
		options = Options()
		options.add_experimental_option("excludeSwitches", ["enable-logging"])
		print("Test additionOfPositiveNumbers started")
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
		if result.get_attribute('value') == '3':
			print("Test passed")
		else:
			print("Test failed")
		self.assertEqual(result.get_attribute('value'), '3')

if __name__ == '__main__':
    unittest.main()
