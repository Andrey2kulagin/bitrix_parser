from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import asyncio

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymorphy3


# Create your views here.
def login(driver):
    print("Начало логина")
    driver.get("https://mp24.bitrix24.ru/marketplace/app/10/")
    people_login = 'anoxinconsult@mail.ru'
    people_password = '1qazxcde32WSX'
    login_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login"))
    )
    login_input.send_keys(people_login)
    print("вставлен логин")
    time.sleep(1)
    login_input.send_keys(Keys.ENTER)
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_input.send_keys(people_password)
    password_input.send_keys(Keys.ENTER)
    print("вставлен пароль")

    # здесь будет логин


def search_settings(driver):
    time.sleep(5)
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    frame1 = driver.find_element(By.XPATH, '//*[@id="workarea-content"]/div/div/iframe')
    driver.switch_to.frame(frame1)
    frame2 = driver.find_element(By.CSS_SELECTOR, ".partner-application-install-select-country-iframe")
    driver.switch_to.frame(frame2)
    print("перешло на нужный фрейм")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".partner-application-b24-list-filter-cnr").click()
    div_with_form = driver.find_element(By.CSS_SELECTOR, 'div.main-ui-control.main-ui-select[data-name="PARTNERSHIP"]')
    div_with_form.click()
    time.sleep(2)
    print(div_with_form.get_attribute("innerHTML"))

    item = div_with_form.find_element(By.XPATH,
                                      '//*[contains(@class, "main-ui-select-inner-item-element") and text()="Битрикс24"]')
    print(item.get_attribute("innerHTML"))
    item.click()
    print("Значения установлены")
    button = driver.find_element(By.CSS_SELECTOR,
                                 ".ui-btn.ui-btn-primary.ui-btn-icon-search.main-ui-filter-field-button.main-ui-filter-find")
    print(button.get_attribute("innerHTML"))
    time.sleep(3)
    button.click()


def applications_analyze(driver):
    time.sleep(3)
    applications = driver.find_elements(By.CSS_SELECTOR, ".main-grid-row.main-grid-row-body")
    for application in applications:
        # print(application.get_attribute("innerHTML"))
        describtion = application.find_element(By.CSS_SELECTOR,
                                               ".main-grid-cell-inner")
        print(describtion.text, '\n\n')
        buttons = application.find_elements(By.CSS_SELECTOR,
                                           ".partner-application-b24-list-item-submit-link.js-partner-submit-application")
        #if len(buttons) == 0 or is_contains_stop_words(describtion.text, ['сети']):
            #continue
       # buttons[0].click()
        if is_contains_stop_words(describtion.text, ['сети']):
            continue
        else:
            print(describtion.text)

def is_contains_stop_words(string: str, stop_words: list):
    inf_stop_words = []
    morph = pymorphy3.MorphAnalyzer(lang='ru')
    for stop_word in stop_words:
        inf_stop_words.append(morph.parse(stop_word)[0].normal_form)
    for word in string.split():
        inf_word = morph.parse(word)[0].normal_form
        if inf_word in inf_stop_words:
            return True
    return False


def main():
    chrome_options = Options()
    # неробот
    print("Установка настроек")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    print("Настройки установлены")
    login(driver)
    search_settings(driver)
    applications_analyze(driver)
    time.sleep(5)


main()
