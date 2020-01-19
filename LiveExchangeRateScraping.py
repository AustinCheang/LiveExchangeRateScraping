import bs4 
from bs4 import BeautifulSoup
import requests
import datetime

rates = [0]

def exchangeRate():
    r = requests.get("https://uk.finance.yahoo.com/quote/GBPHKD=X?p=GBPHKD=X") 
    soup = bs4.BeautifulSoup(r.text, "lxml")
    rate = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    now = datetime.datetime.now().isoformat()
    
    if rates[-1] != rate:
        rates.append(rate)
        print("Time: " + now + "      " + "Exchange Rate:  " + rate + "\n")
        f= open("ExchangeRateRecord.txt","a+")
        f.write("Time: " + now + "      " + "Exchange Rate:  " + rate + "\n")
    
        f.close()


while True:
        exchangeRate()
    
