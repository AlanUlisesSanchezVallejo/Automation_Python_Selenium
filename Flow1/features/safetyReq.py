from ..imports import *
from ..classes import *

def test_safety(driver):
    safetyBtn = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[10]')
    safetyBtn.click()

    try:
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]'))        
            )

    finally:

        ######## Required Equipment #########

        for i in [1,2,3,4,5]:
            requiredEquipment = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/div['+str(i)+']/label')
            requiredRand = random.randint(0,1)
            if (requiredRand == 0):
                continue

            else:
                requiredEquipment.click()

        ########## Additional Required Equipment ###########


        additionalSafetyReq = ['Additional 1',
                                'Additional 2',
                                'Additional 3']

        addEquipmentTXT = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/form/div/div[1]/div[1]/div/input[1]') # Textbox
        addBtn = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]') #Add button "+"
        i = 0

        while i < len(additionalSafetyReq):
            addEquipmentTXT.send_keys(additionalSafetyReq[i])
            time.sleep(2)
            newSelection = driver.find_element(By.XPATH,'//*[@id="additional-equipment0-item-0"]') #New selection box when user inserts a value
            newSelection.click()
            addBtn.click()

            time.sleep(1)
            i+=1

        deleteRand = random.randint(2,len(additionalSafetyReq)+1)

        delete = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/form/div/div['+str(deleteRand)+']/div[2]')
        delete.click()
    time.sleep(5)



            