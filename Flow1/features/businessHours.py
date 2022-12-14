from ..imports import *
from ..classes import *


def test_businessHours(driver,file):
    businessBtn = driver.find_element('xpath', '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[5]')
    businessBtn.click()

    try:
        element = WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]'))
        )
    finally:
        rand = 2#random.randint(1,2)
        if (rand == 1):
            open24_7 = driver.find_element('xpath','//*[@id="0"]/div[2]/label/span')
            open24_7.click()
            file.write('    Open 24/7 option was selected' + os.linesep)
            
        elif (rand == 2):
            for i in range(3,10):
                rand1 = 3 #random.randint(1,3)
                if (rand1 == 1):
                    open24 = driver.find_element('xpath', '//*[@id="0"]/div['+str(i)+']/div[1]/div/div[1]/label/span')
                    open24.click()
                    file.write('    Day: '+ repr(i-2) + ' Open 24 hours option was selected' + os.linesep)

                elif (rand1 == 2):
                    closed = driver.find_element('xpath', '//*[@id="0"]/div['+str(i)+']/div[1]/div/div[2]/label/span')
                    closed.click()
                    file.write('    Day: '+ repr(i-2) + ' Closed option was selected' + os.linesep)

                elif (rand1 == 3):
                    for j in [1,2]:
                        openTime = driver.find_element('xpath', '//*[@id="0"]/div['+str(i)+']/div[2]/div['+str(j)+']/input')

                        if (j == 1):
                            randHour = random.randint(1, 12)
                            randMin  = random.randint(0, 59)

                            randHourstr = str(randHour)

                            if(len(randHourstr)<2):
                                randHourstr = '0'+randHourstr
                                openTime.send_keys(randHourstr) 
                            else:
                                openTime.send_keys(randHour) 

                            randMinStr = str(randMin)
                            
                            if (len(randMinStr)<2 ):
                                randMinStr = '0'+randMinStr
                                openTime.send_keys(randMinStr)
                                # randMinStr = '0'+randMinStr rama flow1
                                # openTime.send_keys(Keys.RIGHT)
                                
                            else:
                                openTime.send_keys(randMin)

                            openTime.send_keys('AM')  
                            file.write('    Day: '+ repr(i-2) + ' Open Time: ' + repr(randHour)+':'+ repr(randMinStr) + 'AM   ')
                            

                        elif (j == 2):
                            randHour = random.randint(1, 12)
                            randMin  = random.randint(0, 59)

                            randHourstr = str(randHour)

                            if (len(randHourstr)<2):
                                randHourstr = '0'+randHourstr
                                openTime.send_keys(randHourstr) 
                            elif(len(randHourstr)==2):
                                openTime.send_keys(randHourstr) 
                                # time.sleep(1)

                             
                            randMinStr = str(randMin)
                            
                            if (len(randMinStr)<2):
                                randMinStr = '0'+randMinStr
                                openTime.send_keys(randMinStr)
                                # randMinStr = '0'+randMinStr
                                # openTime.send_keys(Keys.RIGHT)
                                # time.sleep(1)
                                
                            else:
                                openTime.send_keys(randMin)
                            openTime.send_keys('PM') 
                            file.write('    Day: '+repr(i-2)+ ' Close Time: ' + repr(randHour)+':'+ repr(randMinStr) + 'PM' + os.linesep)
                            
                    
        time.sleep(3)
