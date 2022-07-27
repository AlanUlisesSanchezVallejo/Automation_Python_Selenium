from mailbox import linesep
from Flow1.imports import *
from Flow1.classes import *

def test_contact(driver,file):
    contactbtn = driver.find_element('xpath','//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[4]')
    contactbtn.click()




    try:
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]'))
        )

    finally:

        email = driver.find_element('id','emailAddress')
        email.send_keys(Keys.CONTROL+"A")
        email.send_keys(Keys.DELETE)
        randomName = random.randint(0,100)
        email.send_keys('test'+str(randomName)+'@solera.com')
        file.write('    Email inserted: ' + 'test'+str(randomName)+'@solera.com' + os.linesep)

        phone = driver.find_element('id','phone')
        phone.send_keys(Keys.CONTROL+"A")
        phone.send_keys(Keys.DELETE)
        randomPhone = random.randint(1111111111,9999999998)
        phone.send_keys(str(randomPhone))
        file.write('    Value phone inserted: ' + str(randomPhone) + os.linesep)
        time.sleep(2)




