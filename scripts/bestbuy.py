# imports
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

# search query
query = "500GB+hdd"
# bestbuy url
#                                                        high to low flag
url = "https://www.bestbuy.com/site/searchpage.jsp?st={}&sp=-currentprice+skuidsaasst".format(query)

# disable location access popups in the browser
fp = webdriver.FirefoxProfile()
fp.set_preference('geo.enabled', False)
fp.set_preference('geo.prompt.testing', False)
fp.set_preference('geo.prompt.testing.allow', False)
# enable headless mode
options = Options()
options.headless = True
# initialise the browser
print('starting firefox')
browser = webdriver.Firefox(fp, options=options)
# open the url
print('opening bestbuy homepage')
browser.get("https://bestbuy.com/?intl=nosplash")
print('opening {}'.format(url))
browser.get(url)
try:
    category = browser.find_element_by_css_selector('div[class*="facet-option-container"] a')
    print('filtering search for HDDs')
    browser.get(category.get_attribute("href"))
except:
    pass

# select 'High to Low' in drop down box
print('waiting for 2 seconds')
time.sleep(2)
print('sorting')
dropdownmenu = browser.find_element_by_css_selector('select[id*="sort-by-select"]')
select = Select(dropdownmenu)
time.sleep(2)
select.select_by_visible_text('Price High to Low')
time.sleep(2)

# parse the results
print('parsing')
soup = BeautifulSoup(browser.page_source, 'html.parser')
browser.close()
results = soup.find_all('li', {'class':'sku-item'})
top_result = str(results[0])
soup = BeautifulSoup(top_result, 'html.parser')
heading = soup.find_all('h4', {'class':'sku-header'})
price = soup.find_all('div', {'class':'priceView-customer-price'})
print("--x--")
print(heading[0].text)
print(price[0].text.split(" ")[-1])
