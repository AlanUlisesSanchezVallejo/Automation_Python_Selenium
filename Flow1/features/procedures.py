from msilib.schema import Control
from ..imports import *
from ..classes import *

def test_procedures(driver):
    proceduresBtn = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[11]')
    proceduresBtn.click()

    try:
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]'))
        )
    finally:

        #### Main Procedures ###

        for i in [1,2,3]:
            
            radioBtnRand = random.randint(1,2)
            radioBtn = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div['+str(i)+']/div[3]/p['+str(radioBtnRand)+']/label')
            radioBtn.click()

        additionalDriver = driver.find_element(By.ID,'drivingDirections')
        additionalDriver.send_keys(Keys.CONTROL,"A")
        additionalDriver.send_keys(Keys.DELETE)
        additionalDriver.send_keys('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam eleifend faucibus risus non pellentesque. Nunc interdum condimentum tellus, non sollicitudin erat porta ut. Curabitur imperdiet odio nulla, in euismod felis vulputate in. Fusce tempus tempor arcu sit amet auctor. In non tortor at nulla fringilla molestie. Cras nec felis quis urna aliquam pellentesque et vehicula eros. Suspendisse scelerisque nec diam eu rhoncus. Suspendisse maximus neque neque, sit amet commodo nunc malesuada ut.')



    time.sleep(5)