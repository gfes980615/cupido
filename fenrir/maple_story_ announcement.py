from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import time
from .models import TouristAttractionList
from django.http import JsonResponse
import re
import threading


options = Options()
webdriver_path = './chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

def announcement(request):
    driver = webdriver.Chrome(executable_path=webdriver_path, options=options,chrome_options=chrome_options)
    driver.get('https://www.instagram.com/explore/tags/%E6%A1%83%E5%9C%92%E6%99%AF%E9%BB%9E/?hl=zh-tw')
    print(driver.body)