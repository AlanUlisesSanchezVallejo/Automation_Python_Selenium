from .imports import *
from .classes import *


def test_login(driver):


	usuario = driver.find_element("id","email") # BUG FIXED FIND ELEMENT https://stackoverflow.com/questions/72773206/selenium-python-attributeerror-webdriver-object-has-no-attribute-find-el
	usuario.send_keys("kjohnstone@omnitracs.com")
	usuario.send_keys(Keys.ENTER)
	# time.sleep(1)

	pass1 = driver.find_element("id","password")
	pass1.send_keys("Omni123")
	pass1.send_keys(Keys.ENTER)

