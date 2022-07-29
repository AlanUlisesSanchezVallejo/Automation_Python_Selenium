from ..imports import *
from ..classes import *


def test_services(driver):
    servicesbtn = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[9]')
    servicesbtn.click()

    try:
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]'))
        )
    
    finally:
        rand = random.randint(0,1)

        ######## Lumper Service (YES/NO) ######
        if (rand == 0): 
            lumperService = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/p[2]/label')
            lumperService.click()
        
        else:
            lumperService = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/p[1]/label')
            lumperService.click()

            lumperFee = driver.find_element(By.ID,'lumperCost')
            dolarRand = random.randint(0,9999)
            centsRand = random.randint(0,99)
            lumperFee.send_keys(str(dolarRand)+'.'+str(centsRand))

            currency = Select(driver.find_element(By.ID,'currencyType'))
            currencyRand = random.randint(0,1)
            if (currencyRand == 0):
                currency.select_by_visible_text('USD')
            else:
                currency.select_by_visible_text('CAD')
            

            ######## Payment Option ############
            for i in [1,2,3,4]:
                paymentOption = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[3]/div['+str(i)+']/label')

                paymentOptionRand = random.randint(0,1)

                if (paymentOptionRand == 0):
                    continue
                else:
                    paymentOption.click()
                    
    time.sleep(5)

           













        



