from lib2to3.pgen2 import driver
from .imports import *
from .classes import *


def test_locationNames(driver,file):
    try:
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[2]"))
        )
    finally:
        # locationNamesBtn = driver.find_element("xpath", "//*[@id='root']/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[2]")
        # locationNamesBtn.click()
        locationName = driver.find_element("xpath", "//*[@id='locationMainName']")
        locationName.send_keys(Keys.CONTROL+"A") #Select all the text already exists
        locationName.send_keys(Keys.DELETE) #Delete the previous text to insert a new one
        randomName = random.randint(0,100)
        locationName.send_keys('Solera'+str(randomName))
        file.write('    Name inserted:' + 'Solera'+str(randomName) + os.linesep)
        time.sleep(1)
        # # locationMainName.send_keys(Keys.ENTER)
