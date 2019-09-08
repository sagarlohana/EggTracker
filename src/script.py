import grequests
import requests
import re
from bs4 import BeautifulSoup

def track(url_list, thumbnail_lst, actual_prices_lst, can_buy):

    # Asynchronous response retrieval using grequests
    reqs = [grequests.get(url.url) for url in url_list]
    responses = grequests.map(reqs)

    for i in range(len(responses)):
        soup = BeautifulSoup(responses[i].text, 'html.parser')

        # Outputs the result of the soup in out.txt
        # with open('out.txt', 'w') as f:
        #     print (soup.prettify, file=f)

        # Find current product price
        current_price = soup.find('meta', {'itemprop': 'price'})['content']
        
        # Add current price to list
        actual_prices_lst += [current_price]

        # Find thumbnail of product
        img_object = soup.find('a', {'onfocus': re.compile('swapProductImageWithLoadding2011.*')})['onfocus']
        pattern = re.compile('c1\.neweggimages\.com/NeweggImage/ProductImage/.*\.jpg')
        result = pattern.search(img_object)
        thumbnail = result.group(0).split(',')[0][:-1]

        # Add thumbnail source URL to list
        thumbnail_lst += [thumbnail]
        
        # Add purchasability to list
        if current_price <= url_list[i].price:
            can_buy += [True]
        else:
            can_buy += [False]
