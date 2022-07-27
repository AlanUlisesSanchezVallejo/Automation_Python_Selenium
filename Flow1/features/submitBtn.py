from Flow1.imports import *
from Flow1.classes import *

def test_submitButton(driver,file):
    submit = driver.find_element('xpath', '//*[@id="root"]/div/div/div[1]/div/div/div[1]/div[2]/button[2]')
    submit.click()
    
    try:
        element = WebDriverWait(driver,15).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[1]/div'))
        )
    
    finally:
        file.write('--- Data Saved successfully ---' + os.linesep)
        time.sleep(3)