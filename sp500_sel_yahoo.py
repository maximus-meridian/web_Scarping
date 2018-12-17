import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

option = webdriver.ChromeOptions()
option.add_argument("--incognito")
#browser = webdriver.Chrome("D:\chromedriver\chromedriver.exe")
data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
table = data[0]
print(table.head())

sliced_table = table[1:]
header = table.iloc[0]


corrected_table = sliced_table.rename(columns=header)
print(corrected_table)

tickers = corrected_table['Symbol'].tolist()
print (tickers)

dict={}
i=0
for ele in tickers:
    print(i)
    print(ele)
    try:
        browser_driver_array = webdriver.Chrome("C:\\Users\\devar\\AppData\\Local\\conda\\chromedriver_win32\\chromedriver.exe")
        browser_driver_array.get("https://finance.yahoo.com/quote/"+ele+"/history?p="+ele+"&.tsrc=fin-srch")
        titles_element = browser_driver_array.find_elements_by_xpath(".//span[@class='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)']")
        print(titles_element[0].text)
        dict[ele]=titles_element[0].text
        browser_driver_array.quit()
        i=i+1
        time.sleep(2)
    except Exception as e:
        print(e)
