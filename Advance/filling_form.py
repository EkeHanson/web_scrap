from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from colorama import Fore


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

cyan = Fore.CYAN

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

#Find element by Link text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

#FInd the Search <input> element by name
search = driver.find_element(By.NAME, value = "search")
search.send_keys("Python", Keys.ENTER)

# driver.quit()