from re import A
from typing import final
from ..imports import *
from ..classes import *


def test_searchByAddress(driver):
    try:
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[1]/form/div[1]/div[1]'))
        )

    finally:
        addressBtn = driver.find_element('xpath','//*[@id="root"]/div/div/div[1]/div/div/div[1]/form/div[1]/div[1]/label[2]')
        addressBtn.click()
        try:
            element = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div[1]/form/div[2]'))
            )
        finally:
            address = driver.find_element('xpath','//*[@id="address"]')
            address.send_keys('1500 Solana Blvd Ste 6300 Bldg 6')
            city = driver.find_element('id','city')
            city.send_keys('Roanoke')
            state = Select(driver.find_element("id", "state"))
            state.select_by_visible_text('Texas')
            searchButton = driver.find_element("xpath", "//*[@id='root']/div/div/div[1]/div/div/div[1]/form/div[2]/div/button[1]")
            searchButton.click()
            # time.sleep(2)

            time.sleep(1)


