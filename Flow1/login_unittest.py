import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")


	def test_login(self):
		driver = self.driver
		driver.get("http://dev.omnitracslabs.com")
		usuario = driver.find_element("id","email") # BUG FIXED FIND ELEMENT https://stackoverflow.com/questions/72773206/selenium-python-attributeerror-webdriver-object-has-no-attribute-find-el
		usuario.send_keys("kjohnstone@omnitracs.com")
		usuario.send_keys(Keys.ENTER)
		time.sleep(3)

		pass1 = driver.find_element("id","password")
		pass1.send_keys("Omni123")
		pass1.send_keys(Keys.ENTER)
		time.sleep(5)

		nameLocation = driver.find_element("id", "name")
		nameLocation.send_keys("Solera")
		time.sleep(5)

		cityLocation = driver.find_element("id", "city")
		cityLocation.send_keys("Roanoke")
		time.sleep(5)

		searchButton = driver.find_element("xpath", "//*[@id='root']/div/div/div[1]/div/div/div[1]/form/div[2]/div/button[1]")
		searchButton.click()
		time.sleep(5)

		resultFind = driver.find_element("xpath", "//*[@id='root']/div/div/div[1]/div/div/div[3]/div[1]/div[2]/a[1]/div")
		resultFind.click()
		time.sleep(5)

		








	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()


