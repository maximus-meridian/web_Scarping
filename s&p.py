from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
import json

def gain_func(company):
    url3_1 = "https://finance.yahoo.com/quote/"
    url3_2 = "/history?p="
    url3_3 = "&.tsrc=fin-srch"
    response3 = get(url3_1 + company + url3_2 +company + url3_3)
    html_soup3 = BeautifulSoup(response3.text, 'html.parser')
    tbody3 = html_soup3.find('tbody')
    tr3 = tbody3.find_all('tr')
    #print(str(tr[0])[:500])
    close = []
    avg_gain = 0
    for x in tr3:
        td3 = x.find_all('td')
        try:
            y = td3[4].text
            close.append(y.replace(",",""))
        except:
            continue
            close.append(None)
    
    avg_gain = [float(x) for x in close]
    gain = (avg_gain[len(avg_gain)-1] - avg_gain[0])/len(avg_gain)
    return gain


def reven(comp):
    
    response2 = get(url2+comp)
    html_soup2 = BeautifulSoup(response2.text, 'html.parser')
    Revenue = html_soup2.find('table', class_="infobox vcard").tbody
    tr =    Revenue.find_all('tr')
    for x in tr:
        try:
            if x.th.text == "Revenue":
                return(x.td.text)
        except:
            continue
    raise Exception('no revenue found')
    
    
def get_year(x):
    x = x.split("$")

    z = ""
    p = x[1].split('b')
    for y in p[0]:
        if (y.isdigit()) or (y == "."):
            z+=y
        if y == 'b':
            break
    return(z)
    
    
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
url2 = "https://en.wikipedia.org/wiki/"


response = get(url)
#print(response.text[:500])

html_soup = BeautifulSoup(response.text, 'html.parser')
table = html_soup.find_all('table')
tbody = table[0].find('tbody')
tr = tbody.find_all('tr')

sym = []
com_name = []
GICS_Sector = []
Founded = []
Revenue = []
gain = []

for x in tr[1:50]:
    td = x.find_all('td')
    
    
    try :
        response2 = get(url2+td[1].text)
        #print(url2+td[1].text)
        Revenue.append(get_year(reven(td[1].text)))
        sym.append(td[0].text)
        com_name.append(td[1].text)
        GICS_Sector.append(td[3].text)
        Founded.append(td[8].text[:4])
        gain.append(gain_func(td[0].text))
        #print(gain_func(td[1].text))
    except Exception as e: 
        print(url2+td[1].text)
        print(e)        

#print(sym)
#print(com_name)

stock = pd.DataFrame({'sym': sym,
                      'com_name': com_name,
                      'GICS_Sector': GICS_Sector,
                      'Founded': Founded,
                      'Revenue': Revenue,
                      'Gain' : gain })
print(stock.info())
print(stock.head(10))
stock = stock.sort_values('Gain', ascending=False)
print(stock.head(10))
stock.to_csv('yahoo3.csv')






    
    
