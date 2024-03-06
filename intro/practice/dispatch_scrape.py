from bs4 import BeautifulSoup
import requests

response = requests.get("http://localhost:3000/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

# print(soup)
# print(soup.prettify())

anchors = soup.find_all(name="a")

print(anchors)