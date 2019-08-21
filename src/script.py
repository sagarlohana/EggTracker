import requests
import re
from bs4 import BeautifulSoup

url = "https://www.amazon.ca/Anker-Headphones-Lightweight-Connection-Sweatproof/dp/B01N6DC2ZE/ref=sr_1_1?keywords=bluetooth+headphones&qid=1562557096&s=gateway&sr=8-1"
desired_price = 40.00

print("You just entered this url: {0}".format(url))
try:
    result = requests.get(url)
except:
    print("You have provided an incorrect URL, please re-run the script providing a valid URL (perhaps prepend https://)")
    exit()

data = result.text
soup = BeautifulSoup(data, 'html.parser')

spans = soup.find('span', {'id' : 'priceblock_ourprice'}) # Extracts span containing price from Soup object
price = spans.get_text() # Extracts price out of span
result = re.sub(r"[^\d\.]", "", price) # Uses regex to extract price out of string

print(price)
print(result)

# Pseudo structure for how checking for price feasibility will work
if(desired_price >= float(result)):
    print("Yes you can purchase it")
else:
    print("No not in your price range")
 