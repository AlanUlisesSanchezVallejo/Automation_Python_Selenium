from tkinter import Radiobutton
from xml.dom.minidom import Element
from ..imports import *
from ..classes import *

def test_locationTypes(driver,file):
    locationTypes = driver.find_element("xpath",'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[3]')
    locationTypes.click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div'))
        )
    finally:
        rand = random.randint(1,5) 
        locationTypeBtn = driver.find_element("xpath",'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/p['+str(rand)+']/label')
        file.write('    Location Type selected: '+ str(rand) + os.linesep)
        locationTypeBtn.click()
        time.sleep(1)

