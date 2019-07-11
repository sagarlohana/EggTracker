import requests
import re
from bs4 import BeautifulSoup

# url = input("Enter a URL: ")

# url = "https://www.amazon.ca/dp/B0749WPNHM/ref=ods_gw_ha_H1_d_rr_dinner_tall_ca_061619_en?pf_rd_p=633d60bd-7787-4eb3-88fa-a07caff66213&pf_rd_r=NMCP7WHB6PFJ74B4TVXK"
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
if(desired_price > float(result)):
    print("Yes you can purchase it")
else:
    print("No not in your price range")

# output = str(soup.prettify)
# print(output)
# file = open('sample.txt', 'w')
# file.write(output)
# file.close()

# print (soup.prettify)
# price = soup.find("span", id="priceblock_ourprice")
# print("The price is {0}".format(price.text))
