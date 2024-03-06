from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://dispatch-app-react-v1.vercel.app/")

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')

# Find and click the button
try:
    # Wait for the button to be clickable
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.container-fluid.login a.reg-btn'))
    )
    # Click the button
    button.click()
    print("Button clicked successfully!")
except Exception as e:
    print("Error clicking the button:", e)


