from typing import KeysView
from selenium import webdriver
import requests
from selenium.webdriver.common import keys
driver = webdriver.Chrome()
def test_yandex_search():
    response = requests.get("https://yandex.ru")
    assert response.ok
    driver.get('https://yandex.ru/')
    searchbox = driver.find_element_by_xpath('//*[@id="text"]')
    searchbox.send_keys('ViPNet Coordinator HW5000')
    searchbotton = driver.find_element_by_xpath('//*/form/div[2]/button')
    searchbotton.click()
    #searchbox.send_keys(Keys.ENTER)
    assert searchbox.get_attribute('value') == 'ViPNet Coordinator HW5000'
    searchpdf = driver.find_element_by_xpath('//*[@href="https://infotecs.ru/upload/iblock/db0/ViPNet_Coordinator_HW_5000_web_july_2018.pdf"]').click()
    assert "ViPNet_Coordinator_HW_5000_web_july_2018.pdf" in driver.page_source  


