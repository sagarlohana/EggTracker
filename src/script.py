import grequests
import requests
import re
from bs4 import BeautifulSoup

def track(url_list, thumbnail_lst, actual_prices_lst, can_buy):

    num_products = 0

    # Asynchronous response retrieval using grequests
    if len(url_list) > 1:
        reqs = [grequests.get(url.url) for url in url_list]
        responses = grequests.map(reqs)
    else:
        responses = [requests.get(url_list[0].url)]

    for i in range(len(responses)):
        soup = BeautifulSoup(responses[i].text, 'html.parser')

        # Outputs the result of the soup in out.txt
        # with open('out.txt', 'w') as f:
        #     print (soup.prettify, file=f)

        # Find current product price
        current_price = soup.find('meta', {'itemprop': 'price'})['content']
        
        # Add current price to list
        actual_prices_lst += [current_price]

        # Find thumbnail of product, thumbnail may not exist
        thumbnail = soup.find('meta', {'property': 'og:image'})["content"]

        # Add thumbnail source URL to list
        thumbnail_lst += [thumbnail]
        
        # Add purchasability to list
        if float(current_price) <= url_list[i].price:
            can_buy += [True]
            num_products += 1
        else:
            can_buy += [False]
    return num_products