# Применив selenium, напишите unit-test для авторизации на Яндексе по url: https://passport.yandex.ru/auth/


import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

path = os.path.join(os.getcwd(), 'chromedriver.exe')

options = Options()

login = 'text'
password = 'text'

options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"    #chrome binary location specified here
options.add_argument("--start-maximized") #open Browser in maximized mode
options.add_argument("--no-sandbox") #bypass OS security model
options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(executable_path=path, options=options)

browser.get('https://passport.yandex.ru/auth/')
sleep(1)

search_input_tag = browser.find_element_by_id('passp-field-login')
sleep(1)
search_input_tag.click()
search_input_tag.send_keys(login)
search_input_tag.send_keys(Keys.ENTER)
sleep(1)
search_input_tag = browser.find_element_by_id('passp-field-passwd')
sleep(1)
search_input_tag.click()
sleep(1)
search_input_tag.send_keys(password)
sleep(1)
search_input_tag.send_keys(Keys.ENTER)
sleep(1)

browser.close()