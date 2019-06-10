import requests
from bs4 import BeautifulSoup

url = input("Enter a URL: ")
print("You just entered this url: {0}".format(url))
try:
    result = requests.get(url)
except:
    print("You have provided an incorrect URL, please re-run the script providing a valid URL (perhaps prepend https://)")
    exit()
data = result.text
soup = BeautifulSoup(data, 'html.parser')
print (soup.prettify)
# price = soup.find("span", id="priceblock_ourprice")
# print("The price is {0}".format(price.text))
