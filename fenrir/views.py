from datetime import datetime
from django.shortcuts import render
import requests
import re
from bs4 import BeautifulSoup
from .models import Rate

def home(request):
    return render(request, 'fenrir/fenrir.html', {
        'rate_list': getTaiwanBankRate(),
    })

class ExchangeRate:
    country = ""           #國家
    cashRateBuy = 0         #現金買入
    cashRateSell = 0        #現金賣出
    realtimeRateBuy = 0     #即期買入
    realtimeRateSell = 0    #即期賣出
    def __init__(self, country="", cashRateBuy=0, cashRateSell=0, realtimeRateBuy=0, realtimeRateSell=0):
        self.country = country
        self.cashRateBuy = cashRateBuy
        self.cashRateSell = cashRateSell
        self.realtimeRateBuy = realtimeRateBuy
        self.realtimeRateSell = realtimeRateSell

def getTaiwanBankRate():
    url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
    req = requests.get(url)
    req.encoding = 'utf8'

    soup = BeautifulSoup(req.text, "html.parser")
    countryCoins = soup.select("td.currency.phone-small-font")  #取得幣別
    countrys = []
    
    countCountry = 0
    for countryCoin in countryCoins:
        country = countryCoin.select("div.hidden-phone.print_show")
        countrys.append(country[0].text.strip())
        countCountry = countCountry + 1

    CashRates = soup.select("td.rate-content-cash.text-right.print_hide")  #取得現金匯率
    RealtimeRates = soup.select(
        "td.rate-content-sight.text-right.print_hide")  #取得即期匯率

    cashRateBuy, cashRateSell = getRateResult(CashRates)

    realtimeRateBuy, realtimeRateSell = getRateResult(RealtimeRates)

    rate_list = []
    for i in range(len(countrys)):
        rate_obj = ExchangeRate(countrys[i],cashRateBuy[i],cashRateSell[i],realtimeRateBuy[i],realtimeRateSell[i])
        rate_list.append(rate_obj)
        # Rate.objects.create(country=countrys[i],cash_rate_buy=cashRateBuy[i],cash_rate_sell=cashRateSell[i],realtime_rate_buy=realtimeRateBuy[i],realtime_rate_sell=realtimeRateSell[i])
    
    return rate_list

def getRateResult(resRates):
    tmpBuy = []
    tmpSell = []

    status = 0

    for rate in resRates:
        if status == 0:
            tmpBuy.append(rate.text.strip())
            status = 1
            continue
        if status == 1:
            tmpSell.append(rate.text.strip())
            status = 0
            continue
    return tmpBuy, tmpSell

