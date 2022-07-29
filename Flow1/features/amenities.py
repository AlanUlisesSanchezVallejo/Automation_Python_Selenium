from ..imports import *
from ..classes import *

def test_amenities(driver):
    amenitiesBtn = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[8]')
    amenitiesBtn.click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]'))
        )

    finally:
        for i in [1,2,3,4,5,6]:
            rand = random.randint(1,2)
            radioBtn = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div['+str(i)+']/div[3]/p['+str(rand)+']/label')
            radioBtn.click()
            # time.sleep(1)
        
        ###### Additional Amenities ######



        additionalAmenities =   ['Additional 1',
                                'Additional 2',
                                'Additional 3'] #These are just examples, was taken randomly from internet
        i=0
        amenityTXT  = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[3]/form/div/div/div[1]/div/input[1]')
        addBtn = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[3]/form/div/div[1]/div[2]')
        
        print (len(additionalAmenities))
        while i < len(additionalAmenities):
            amenityTXT.send_keys(additionalAmenities[i])
            time.sleep(2)
            newSelection = driver.find_element(By.XPATH, '//*[@id="additional-amenity0-item-0"]')
            newSelection.click()
            addBtn.click()
            time.sleep(2)
            i+=1


        #### Deleting a random Additional Amenitie ########
        
        deleteRand = random.randint(2,len(additionalAmenities)+1)

        delete = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[3]/form/div/div['+str(deleteRand)+']/div[2]')
        delete.click()

    time.sleep(5)






