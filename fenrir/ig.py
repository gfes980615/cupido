from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from .models import TouristAttractionList
from django.http import JsonResponse
import re
import threading


options = Options()
webdriver_path = './chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

def get_ig(request):
    driver = webdriver.Chrome(executable_path=webdriver_path, options=options,chrome_options=chrome_options)
    driver.get('https://www.instagram.com')

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'username')))
    username_input = driver.find_elements_by_name('username')[0]
    password_input = driver.find_elements_by_name('password')[0]
    print("inputing username and password...")
    username = "gfes980615@yahoo.com.tw"
    password = "fr860816ed"
    # ------ 輸入帳號密碼 ------
    username_input.send_keys(username)
    password_input.send_keys(password)

    # ------ 登入 ------
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,
    '//*[@id="loginForm"]/div/div[3]/button/div')))
    # ------ 網頁元素定位 ------
    login_click = driver.find_elements_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')[0]
    # ------ 點擊登入鍵 ------
    login_click.click()

    searchbox = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='搜尋']")
        )
    )
    driver.get('https://www.instagram.com/ryu19860812/')
    searchbox.send_keys("#桃園")
    searchbox.click()
    print(driver.body)
    print(driver.page_source)