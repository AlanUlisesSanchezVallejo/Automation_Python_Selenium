from ..imports import *
from ..classes import *

def test_locationDetails(driver, file):

    try:
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located(('xpath','//*[@id="root"]/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div'))
        )

    finally:
        geofenceBtn = driver.find_element('xpath','//*[@id="simple-tab-1"]')
        geofenceBtn.click()
        time.sleep(2)
        
        truckPathsBtn = driver.find_element('xpath','//*[@id="simple-tab-2"]')
        truckPathsBtn.click()
        time.sleep(2)

        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(10)

        # visitTrends = driver.find_element('xpath','//*[@id="root"]/div/div/div[1]/div/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/div[2]')
        # visitTrends.click()
        # time.sleep(2)

        # lastMonth = driver.find_element('xpath','//*[@id="root"]/div/div/div[1]/div/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]')
        # lastMonth.click()
        # time.sleep(2)