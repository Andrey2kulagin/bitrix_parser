from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import asyncio

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create your views here.
def login(driver):
    driver.get("https://mp24.bitrix24.ru/marketplace/app/10/")
    people_login = 'anoxinconsult@mail.ru'
    people_password = '1qazxcde32WSX'
    login_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login"))
    )
    login_input.send_keys(people_login)
    time.sleep(1)
    login_input.send_keys(Keys.ENTER)
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_input.send_keys(people_password)
    password_input.send_keys(Keys.ENTER)

    # здесь будет логин
    return HttpResponse("Открыли страницу")


def search_settings(driver):
    time.sleep(1)
    frame = driver.find_element(By.ID, 'appframe_0dda8c75d8d81d494aabe301e5064553')
    time.sleep(10)
    print(frame.get_attribute("innerHTML"))
    #driver.switch_to.frame(frame)
    #partnership_block = driver.find_element(By.ID, "b24_partner_application_filter_search")
    '''partnership_block = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "execute"))
    )'''
    time.sleep(1)
   # partnership_block.click()
    '''partnership_block = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".main-ui-control.main-ui-select[data-name='PARTNERSHIP']"))
    )
    time.sleep(1)
    partnership_block.click()'''
    '''partnership_input = partnership_block.find_element(By.CSS_SELECTOR, ".main-ui-square-search-item")
    partnership_input.value = "B24"'''


def index(request):
    chrome_options = Options()
    # неробот
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    login(driver)
    search_settings(driver)
    time.sleep(5)


    return render(request, "parser/index.html")
