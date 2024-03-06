from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from  colorama import Fore
import time

magenta = Fore.MAGENTA
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--enable-logging")

driver = webdriver.Chrome(options=chrome_options)

driver.get('http://localhost:3000/')

access = driver.find_element(By.XPATH, value='//*[@id="root"]/div/div/div[1]/div/div/div[2]/a')

access.click()

email = driver.find_element(By.XPATH, value='//*[@id="root"]/div/div/div/div/div/form/div[2]/div[1]/input')
email.send_keys("admin@app.com")

password = driver.find_element(By.XPATH, value='//*[@id="root"]/div/div/div/div/div/form/div[2]/div[2]/input')
password.send_keys("qwertyqwerty")

loggin = driver.find_element(By.XPATH, value='//*[@id="root"]/div/div/div/div/div/form/div[2]/div[3]/button')
loggin.click()

# time.sleep(10)
# establishment = driver.find_element(By.XPATH, value='//*[@id="root"]/div/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[2]')
# print(establishment.text)

time.sleep(10)
establishments = driver.find_elements(By.CSS_SELECTOR, value='div.container .position-absolute')
est = []

for establishment in establishments:
    # print(establishment.text)
    if establishment.text != "":
        est.append(establishment.text)
print(est)
driver.quit()
