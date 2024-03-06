from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Chrome()


driver.get("https://dispatch-app-react-v1.vercel.app/")

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')


elements = soup.select('div.container-fluid.login a.reg-btn')
access = soup.select('div.container-fluid.login a.log-btn')

for acces in access:
    print(acces.getText())

# for element in elements:
#     print(element.get_text())

driver.quit()
