from requests import get
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.nseindia.com/products/dynaContent/equities/indices/historicalindices.jsp?indexType=NIFTY%20500&fromDate=19-11-2017&toDate=18-12-2017'

response = get(url)
#print(response.text[:500])

html_soup = BeautifulSoup(response.text, 'html.parser')
x = html_soup.find_all('tr')

date=[]
Open = []
High = []
Low = []
Close = []
Shares_Traded = []
Turnover_Cr= []

for temp in x:
    if temp.find('td', class_ = 'date')  is not None:
        date.append(temp.find('td', class_ = 'date').text)
        t = temp.find_all('td', class_ = 'number')
        Open.append(t[0].text)
        High.append(t[1].text)
        Low.append(t[2].text)
        Close.append(t[3].text)
        Shares_Traded.append(t[4].text)
        Turnover_Cr.append(t[5].text)
        
        

stock = pd.DataFrame({'date': date,
                      'Open': Open,
                      'High': High,
                      'Low': Low,
                      'Close': Close,
                      'Shares_Traded':Shares_Traded,
                      'Turnover_Cr':Turnover_Cr})
print(stock.info())
print(stock.head(10))
stock.to_csv('stock_1.csv')
