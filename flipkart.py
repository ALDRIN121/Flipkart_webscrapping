from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
PATH = "C:\webdriver\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
products=[]
rate = []
driver.get("https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&sort=recency_desc&wid=1.productCard.PMU_V2_1")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True,attrs={'class':'_31qSD5'}):
    name = a.find('div',attrs={'class':'_3wU53n'}).text
    price = a.find('div',attrs={'class':'_1vC4OE _2rQ-NK'}).text.replace('₹','')
    
    products.append(name)
    rate.append(price)
    
    
df = pd.DataFrame({'PRODUCT NAME':products,'PRICE':rate })
print(df)
df.to_csv(r'C:\Users\Aldrin\Documents\web scrapping\flipkart webscrapping\flipkart.csv',index=False,encoding='utf-8')

    