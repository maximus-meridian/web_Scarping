from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# example option: add 'incognito' command line arg to options
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# create new instance of chrome in incognito mode
browser = webdriver.Chrome("C:\\Users\\devar\\AppData\\Local\\conda\\chromedriver_win32\\chromedriver.exe")

# go to website of interest
browser.get("http://finance.yahoo.com/q/hp?s=XEL+Historical+Prices")

# wait up to 10 seconds for page to load
#timeout = 10
#try:
#    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='Pos(r) Bgc($bg-content) Miw(1007px) Maw(1260px) tablet_Miw(600px)--noRightRail Bxz(bb) Bdstartc(t) Bdstartw(20px) Bdendc(t) Bdends(s) Bdendw(20px) Bdstarts(s) Mx(a)']")))
#except TimeoutException:
#    print("Timed out waiting for page to load")
#    browser.quit()


# get all of the titles for the financial values
titles_element = browser.find_elements_by_xpath(".//span[@class='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)']")
print(titles_element[0].text)
browser.quit()