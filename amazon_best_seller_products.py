import numpy as np
import pandas as pd 
import requests 
from bs4 import BeautifulSoup

#Amazon Categories
categories = ["electronics","baby-products","computers","home","books"]
products=[]
for i in range(0,len(categories)):

    url = 'https://www.amazon.com.tr/gp/bestsellers/' + categories[i] + '/ref=zg_bs_nav_0'

    soup = BeautifulSoup((requests.get(url).text),'lxml')

    df = soup.find_all('li', class_ = 'zg-item-immersion')

    #Product Name & Price scrapping

    for k in range(0,len(df)):
        product_name =df[k].a.div.find('img', alt=True)['alt']
        price =df[k].find('span', class_ = 'p13n-sc-price').text
        try:
            price = float(price.partition(' TL')[0].replace('.','').replace(',','.'))
        except:
            price = 0
        products.append({'product_name':product_name, 'price':price,'categories':categories[i]})

amazon_best_seller_products = pd.DataFrame(products)
