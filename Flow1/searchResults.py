# from ast import Try
from .imports import *
from .classes import *


def test_SearchResults(driver):
	try:
		element = WebDriverWait(driver,15).until(
			EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
		)
	finally:
		selectResult = driver.find_element("xpath", "//*[@id='root']/div/div/div[1]/div/div/div[3]/div[1]/div[2]/a[1]/div")
		selectResult.click()
		time.sleep(3)