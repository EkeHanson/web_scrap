import requests
from bs4 import BeautifulSoup

# URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
URL = "https://www.jumia.com.ng/electronics/"

headers = {'Accept-Language' : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

response = requests.get(URL, headers=headers)
website_html = response.text


soup = BeautifulSoup(website_html, "html.parser")

# print(soup.title)
# print(soup.title.string)
# print(soup.title.name)
# print(soup.select(".prc"))
# print(soup.select_one(".prc").getText())
# print(soup.find_all(name="span", class_"a-price-whole"))


# print(soup.find_all(class_="prc")[0].getText())

all_product= soup.find_all(name="div", class_="prc")

product_price = [price.getText() for price in all_product]

for price in product_price:
    print(price)