from Flow1.imports import *
from Flow1.classes import *


def test_searchByLocation(driver):
	try:
		element = WebDriverWait(driver,15).until(
			EC.presence_of_element_located((By.ID, "name"))
			)

	finally:
		nameLocation = driver.find_element("id", "name")
		nameLocation.send_keys("Solera")
		#time.sleep(5)

		cityLocation = driver.find_element("id", "city")
		cityLocation.send_keys("Roanoke")
		#time.sleep(5)

		state = Select(driver.find_element("id", "state"))
		state.select_by_visible_text("Texas")
		time.sleep(2)

		searchButton = driver.find_element("xpath", "//*[@id='root']/div/div/div[1]/div/div/div[1]/form/div[2]/div/button[1]")
		searchButton.click()
		# time.sleep(2)
