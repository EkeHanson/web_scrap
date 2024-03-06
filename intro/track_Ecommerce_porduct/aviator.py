import requests
from bs4 import BeautifulSoup

URL = "https://www.sportybet.com/ng/games"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

# Find the specific div element with class 'bubble-multiplier' within 'app-bubble-multiplier'
app_bubble_multiplier = soup.find('app-bubble-multiplier', class_='payout')
if app_bubble_multiplier:
    div_element = app_bubble_multiplier.find('div', class_='bubble-multiplier')

    # Extract the text content
    if div_element:
        multiplier = div_element.text.strip()
        print("Multiplier:", multiplier)
    else:
        print("Div element not found")
else:
    print("app-bubble-multiplier element not found")
