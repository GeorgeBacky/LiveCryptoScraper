import random
import bs4
import requests
import time

# Console Colors 
W  = '\033[0m'  # white (normal)
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan

my_color = [W, G, O, B, P,C]
    


def PriceTrackerBTC():
    url = 'https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD'
    response = requests.get(url)
    html = response.content

    soup = bs4.BeautifulSoup(html,"html.parser")
    price = soup.find('div',{'class':'D(ib) smartphone_Mb(10px) W(70%) W(100%)--mobp smartphone_Mt(6px)'}).find('span').text
    time.sleep(0.1)
    return price

def PriceTrackerXMR():
    xmr_url = 'https://finance.yahoo.com/quote/XMR-USD?p=XMR-USD'
    xmr_response = requests.get(xmr_url)
    html_xmr = xmr_response.content

    soup = bs4.BeautifulSoup(html_xmr,"html.parser")
    price_xmr = soup.find('div',{'class':'D(ib) smartphone_Mb(10px) W(70%) W(100%)--mobp smartphone_Mt(6px)'}).find('span').text
    time.sleep(0.1)
    return price_xmr
    
print ("Welcome to live cryptocurrency price scraper")
print(55*'-')
user_starting = input('Do you want to start the service?(Y/N):').capitalize()

if user_starting == "Y":
    print("Service trying to connect..")
    print(55*'-')
    time.sleep(3.5)
    while True:
        # print(45*"-")
        print(time.ctime(),random.choice(my_color),"BTC-USD Price is :",PriceTrackerBTC(),'$')
        print(45*'#')
        print(time.ctime(),random.choice(my_color),"XMR-USD Price is :",PriceTrackerXMR(),'$')

else:
    print("Quiting Service..")