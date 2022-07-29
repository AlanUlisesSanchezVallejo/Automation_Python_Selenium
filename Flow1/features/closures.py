from ..imports import *
from ..classes import *

def test_closures(driver):
    try:
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]')) #Body edit details
        ) 
    
    finally:
        closuresBtn = driver.find_element('xpath','//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[6]') 
        closuresBtn.click()

        try:
            element = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]')) #Body toggle Closures
            ) 
        finally:
            for i in [3,4,5,6,7,8]:
                rand = random.randint(0,1)
                
                if (rand == 1):
                    toggle = driver.find_element('xpath','//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div['+str(i)+']/div')
                    toggle.click()
                
                elif (rand == 0):
                    continue
    
    time.sleep(2)







                                    