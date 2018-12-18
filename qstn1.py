import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time




# =============================================================================
# weekly = "https://finance.yahoo.com/quote/AAPL/history?period1=1387305000&period2=1545071400&interval=1wk&filter=history&frequency=1wk"
# monthly = "https://finance.yahoo.com/quote/AAPL/history?period1=1387305000&period2=1545071400&interval=1mo&filter=history&frequency=1mo"
# daily = "https://finance.yahoo.com/quote/"+ele+"/history?period1=1387305000&period2=1545071400&interval=1d&filter=history&frequency=1d"
# 
# =============================================================================

def scroll2(driver):
    arr = ["window.scrollTo(0,508);","window.scrollTo(0,3811.199951171875);","window.scrollTo(0,7573.60009765625);","window.scrollTo(0,11355.2001953125);","window.scrollTo(0,15122.400390625);","window.scrollTo(0,18894.400390625);","window.scrollTo(0,22667.19921875);","window.scrollTo(0,26431.19921875);","window.scrollTo(0,30195.19921875);","window.scrollTo(0,33976.80078125);","window.scrollTo(0,37733.6015625);","window.scrollTo(0,41507.19921875);","window.scrollTo(0,45293.6015625);"]
    
    for x in arr:
        print("scr: "+ x )
        driver.execute_script(x)

def scroll(driver):
    SCROLL_PAUSE_TIME = 2

    # Get scroll height
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        print("scrolling")
        # Scroll down to bottom
        for _ in range(20):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
    
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height



option = webdriver.ChromeOptions()
option.add_argument("--incognito")
#browser = webdriver.Chrome("D:\chromedriver\chromedriver.exe")
data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
table = data[0]
#print(table.head())

sliced_table = table[1:]
header = table.iloc[0]


corrected_table = sliced_table.rename(columns=header)
#print(corrected_table)

tickers = corrected_table['Symbol'].tolist()
gics = corrected_table['GICS Sector'].tolist()

companies_list = pd.concat([pd.DataFrame(tickers), pd.DataFrame(gics)], axis=1, sort=False)
companies_list.to_csv("Company.csv")
#print (tickers)

dict={}
i=0
for ele in tickers[1:10]:
    print(i)
    print(ele)
    try:
        #day wise
        browser_driver_array = webdriver.Chrome("C:\\Users\\****\\AppData\\Local\\conda\\chromedriver_win32\\chromedriver.exe")
        browser_driver_array.get("https://finance.yahoo.com/quote/"+ele+"/history?period1=1387305000&period2=1545071400&interval=1d&filter=history&frequency=1d")
        titles_element = browser_driver_array.find_elements_by_xpath(".//span[@class='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)']")
        #scroll2(browser_driver_array)
        #browser_driver_array.execute_script("window.scrollTo(0,3811.199951171875);")
        #browser_driver_array.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        x = browser_driver_array.find_elements_by_xpath(".//tr[@class='BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)']")
        data = [y.text for y in x]
        
        data2 =  []
        
        for a in data:
            if "Dividend" not in a:
                data2.append(a)
        dates = [[z[:12]] for z in data2]
        data = [z[12:].strip().split(" ") for z in data2]
        result = pd.concat([pd.DataFrame(dates), pd.DataFrame(data)], axis=1, sort=False)
        result.columns = ["Date","Open","	High"	,"Low"	,"Close",	"Adj Close",	"Volume"]
        result.head(10)
        result.to_csv(ele + "_daily.csv")
        browser_driver_array.quit()


        #week wise
        browser_driver_array = webdriver.Chrome("C:\\Users\\****\\AppData\\Local\\conda\\chromedriver_win32\\chromedriver.exe")
        browser_driver_array.get("https://finance.yahoo.com/quote/"+ele+"/history?period1=1387305000&period2=1545071400&interval=1wk&filter=history&frequency=1wk")
        titles_element = browser_driver_array.find_elements_by_xpath(".//span[@class='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)']")
        #scroll2(browser_driver_array)
        #browser_driver_array.execute_script("window.scrollTo(0,3811.199951171875);")
        #browser_driver_array.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        x = browser_driver_array.find_elements_by_xpath(".//tr[@class='BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)']")
        data = [y.text for y in x]
        
        data2 =  []
        
        for a in data:
            if "Dividend" not in a:
                data2.append(a)
        dates = [[z[:12]] for z in data2]
        data = [z[12:].strip().split(" ") for z in data2]
        result = pd.concat([pd.DataFrame(dates), pd.DataFrame(data)], axis=1, sort=False)
        result.columns = ["Date","Open","	High"	,"Low"	,"Close",	"Adj Close",	"Volume"]
        result.head(10)
        result.to_csv(ele + "_weekly.csv")
        browser_driver_array.quit()



        #week wise
        browser_driver_array = webdriver.Chrome("C:\\Users\\****\\AppData\\Local\\conda\\chromedriver_win32\\chromedriver.exe")
        browser_driver_array.get("https://finance.yahoo.com/quote/"+ele+"/history?period1=1387305000&period2=1545071400&interval=1mo&filter=history&frequency=1mo")
        titles_element = browser_driver_array.find_elements_by_xpath(".//span[@class='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)']")
        #scroll2(browser_driver_array)
        #browser_driver_array.execute_script("window.scrollTo(0,3811.199951171875);")
        #browser_driver_array.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        x = browser_driver_array.find_elements_by_xpath(".//tr[@class='BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)']")
        data = [y.text for y in x]
        
        data2 =  []
        
        for a in data:
            if "Dividend" not in a:
                data2.append(a)
        dates = [[z[:12]] for z in data2]
        data = [z[12:].strip().split(" ") for z in data2]
        result = pd.concat([pd.DataFrame(dates), pd.DataFrame(data)], axis=1, sort=False)
        result.columns = ["Date","Open","	High"	,"Low"	,"Close",	"Adj Close",	"Volume"]
        result.head(10)
        result.to_csv(ele + "_monthly.csv")
        browser_driver_array.quit()


        i=i+1
        time.sleep(2)
    except Exception as e:
        print(e)
