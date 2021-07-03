from bs4 import BeautifulSoup, element
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd  



driver = webdriver.Edge('D:/The Stuffs/Project-480/msedgedriver')



req = requests.get("https://prothomalo.com/search")
soup = BeautifulSoup(req.text, "html.parser")
urls = []
for link in soup.find_all('a'):
    urls.append(link.get('href'))
urls = urls[5:]
urls = list(set(urls))

contents = []

titles = []
for url in urls:
    driver.get(url)
    time.sleep(2)
    try:
        a = driver.find_elements_by_css_selector("p")
        txt = ""
        for x in a:
            txt = txt +x.text
        contents.append(txt)
        if txt != "":
            titles.append(driver.title)
    except:
        continue
    print(contents)
print(titles)
print(contents)
dict = {'headline':titles,'content':contents}
df = pd.DataFrame(dict) 
df.to_csv(r'scraped_news.csv')
