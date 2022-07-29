from lib2to3.pgen2.driver import Driver
from multiprocessing.connection import wait
from re import A
from typing import final
from ..imports import *
from ..classes import *


def test_appointmentSch(driver):
    appointmentBtn = driver.find_element('xpath','//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[7]')
    appointmentBtn.click()
    try:
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]'))
        )
    finally:
        
        # print('hola')
        state = Select(driver.find_element('xpath', '//*[@id="appointmentType"]')) #Scroll Down menu appointment Type
        rand = 1#random.randint(0,1)
        # print('adios')

        if (rand ==0 ):
            state.select_by_visible_text('FCFS')
            specialInstructions = driver.find_element('xpath','//*[@id="specialInstructions"]')
            specialInstructions.send_keys('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate sit amet libero vel luctus. Suspendisse rutrum, nisi in molestie lobortis, dui dui mollis ante, aliquam accumsan dolor erat sit amet justo. Curabitur eget ultrices lectus. Nunc sollicitudin felis enim, sit amet auctor sem ornare nec. Sed pellentesque, massa vel mollis dictum, libero velit placerat nibh, sodales porta sem nisi sit amet lectus. Pellentesque mattis malesuada turpis in ultrices.')

        else:
            state.select_by_visible_text('By Appointment Only')

            # Fill ONLINE, BY Phone and  By email
            for i in [1,2,3]:
                randomClick = random.randint(0,1) # Click or not the checkboxes randomly
                onlineBtn = driver.find_element('xpath','//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div['+str(i)+']/label/span')
                if randomClick == 0:
                    continue
                else:
                    onlineBtn.click()
                    try: 
                        error = driver.find_element(By.CLASS_NAME,'bh-error') # Error class whe textbox is open and there is not any value (webpage, phone or email)
                    except:
                        print('except')
                    else:
                        if (i==1):
                            print('else')
                            onlineTxt = driver.find_element('xpath','//*[@id="websiteAddress"]')
                            onlineTxt.send_keys('www.solera.com')

                        elif (i==2):
                            phoneNumber = driver.find_element('xpath','//*[@id="phoneNumber"]')
                            randPhone = random.randint(1000000000,9999999999)
                            phoneNumber.send_keys(randPhone)
                            # time.sleep(3)

                        elif (i==3):
                            email = driver.find_element('xpath','//*[@id="emailAddress"]')
                            randEmail = random.randint(0,100)
                            email.send_keys('Soleratest_'+str(randEmail)+'@mail.com')


            specialInstructions = driver.find_element('xpath','//*[@id="specialInstructions"]')
            specialInstructions.send_keys(Keys.CONTROL,"A")
            specialInstructions.send_keys(Keys.DELETE)
            specialInstructions.send_keys('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam eleifend faucibus risus non pellentesque. Nunc interdum condimentum tellus, non sollicitudin erat porta ut. Curabitur imperdiet odio nulla, in euismod felis vulputate in. Fusce tempus tempor arcu sit amet auctor. In non tortor at nulla fringilla molestie. Cras nec felis quis urna aliquam pellentesque et vehicula eros. Suspendisse scelerisque nec diam eu rhoncus. Suspendisse maximus neque neque, sit amet commodo nunc malesuada ut.')

    time.sleep(5)



          
