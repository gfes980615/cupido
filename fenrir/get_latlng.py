from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import time
from .models import TouristAttractionList
from django.http import JsonResponse
import re
import threading

options = Options()
webdriver_path = '.\chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


def searchLatLng(request):
    touristList = TouristAttractionList.objects.filter(latitude__isnull=True, longitude__isnull=True)
    
    for tourist in touristList:
        job(tourist)
    
    return JsonResponse({'data':'success'})

def job(tourist):
    try:
        objects = TouristAttractionList.objects.filter(place=tourist.place)
        address = tourist.address
        location = address.split(" ")
        url = getLatLongURL(location[1])
        lat,lng = getLatLong(url)
        objects.update(latitude=lat,longitude=lng)
    except Exception as e:
        print(e)
        
def getLatLongURL(name):
    try:
        driver = webdriver.Chrome(executable_path=webdriver_path, options=options,chrome_options=chrome_options)
        driver.get('https://www.google.com.tw/maps') 
        driver.find_element_by_id('searchboxinput').send_keys(name)
        driver.find_element_by_id('searchbox-searchbutton').click()

        while True: 
            if driver.current_url != 'https://www.google.com.tw/maps':
                break

        url = driver.current_url
        driver.close()
    except Exception as e:
        print(e)
    return url

def getLatLong(url):
    try:
        regex = re.compile('@(.*),1[0-9]+z')
        match = regex.search(url)
        latlng = match.group(1).split(',')
        lat = latlng[0]
        lng = latlng[1]
    except Exception as e:
        print(e)
    
    return lat, lng