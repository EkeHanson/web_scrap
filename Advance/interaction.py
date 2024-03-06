from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from colorama import Fore


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

cyan = Fore.CYAN

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")


number = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
number.click()
print(f"{cyan} wikipedia has {number.text} articles in English")

# driver.quit()