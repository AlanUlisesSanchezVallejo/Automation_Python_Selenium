# from ast import If
from ..classes import *
from ..imports import *

def test_editDetails(driver):
    handles = driver.window_handles 
    print('Estos son los IDs de las pestañas abiertas:   ',handles)
    print(type(handles)) 

    for handle in handles:  ## Switch between tabs
        driver.switch_to.window(handle)
        print(driver.title)
    
    try: 
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[1]/div/div/div/div[2]/div[1]/div/a/button")) #Edit Details button
        )

    finally:
        editButton = driver.find_element("xpath", "//*[@id='root']/div/div/div[1]/div/div/div/div[2]/div[1]/div/a/button")
        editButton.click()
        # time.sleep(5)
        # time.sleep(15)
        # driver.close()


    





  


