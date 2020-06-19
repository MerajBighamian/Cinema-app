import re
import requests
from bs4 import BeautifulSoup
a=1
for i in range(1,4):
    response = requests.get("https://divar.ir/s/isfahan/mobile-phones?page={}".format(i))
    soup = BeautifulSoup(response.text,'html.parser')
    name = soup.find_all('div',attrs={'class':'post-card__title'})
    price = soup.find_all('div',attrs={'class':'post-card__description'})

    name_phone=[]
    for phone in name :
        phone_about= phone.text
        phone_about = phone_about.strip()
        name_phone.append(phone_about)

    price_phone = []

    for one_price in price:
        price_p = one_price.text
        price_p = price_p.strip()
        price_phone.append(price_p)

    result =list(zip(price_phone,name_phone))
    
    for price,mobile in result:
        print("{2}--model mobile is {0:>30s} and price is {1:<23s} .".format(mobile,price,a))
        a+=1


