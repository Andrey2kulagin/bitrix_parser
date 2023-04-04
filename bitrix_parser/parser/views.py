from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import schedule
import asyncio
from .tasks import refresh


# Create your views here.
def login(driver):
    driver.get("https://mp24.bitrix24.ru/marketplace/app/10/?any=10%2F&current_fieldset=SOCSERV")
    # здесь будет логин
    return HttpResponse("Открыли страницу")


def index(request):
    chrome_options = Options()
    # неробот
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    login(driver)
    refresh(driver).delay()
    for i in range(170000000):
        print("Working")

    return render(request, "parser/index.html")
