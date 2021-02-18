# Применив selenium, напишите unit-test для авторизации на Яндексе по url: https://passport.yandex.ru/auth/

import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


def init_selenium():
    '''
    Авторизация и запуск Selenium. Поиска его у меня на диске, в системе и т.д. Первоначальные настройки для работы.
    '''

    path = os.path.join(os.getcwd(), 'chromedriver.exe')
    options = Options()

    # chrome binary location specified here

    options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    options.add_argument("--start-maximized")  # open Browser in maximized mode
    options.add_argument("--no-sandbox")  # bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    browser = webdriver.Chrome(executable_path=path, options=options)

    return browser


def auth_yandex_mail(login, password):
    '''
    Функция для авторизации в Яндекс почте. Sleep поставил на каждом этапе, чтобы не было проблем с возможными
    капчами, поэтому на каждом этапе сделал такое.
    '''

    browser = init_selenium()
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
    url = browser.current_url
    if ('phone' in url) or ('mail.yandex.ru' in url):
        return 'OK'
    # else:
    #     return 'Error'

if __name__ == "__main__":
    ya = auth_yandex_mail('test', 'test')
    print(ya)