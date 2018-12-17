# =============================================================================
# from requests import get
# from bs4 import BeautifulSoup
# import pandas as pd
# import urllib.request
# import json
# from selenium.webdriver.common.keys import Keys
# =============================================================================

from selenium import webdriver
from selenium.webdriver.support.ui import Select

url = 'https://www.nseindia.com/products/content/equities/equities/eq_security.htm'

#chromedriver path
chrome_drive_path= "D:\\somefolder\\****\\chromedriver.exe"

# =============================================================================
# for chrome
driver = webdriver.Chrome(chrome_drive_path)
driver.maximize_window()
driver.get(url)

# =============================================================================
'''
# for firefox
driver = webdriver.Firefox()
driver.get(url)
# =============================================================================
'''

#to fill the "Enter Symbol"
elem = driver.find_element_by_id("symbol")
elem.clear()
elem.send_keys("AXISBANK")


#to select date range
select = Select(driver.find_element_by_id("dateRange"))
select.select_by_visible_text("24 Months")

# to click the get button
button = driver.find_element_by_id("get")
button.click()






