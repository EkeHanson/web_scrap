from undetected_chromedriver import ChromeOptions, Chrome
import random

# Import modules for Selenium WebDriverWait and expected conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

options = ChromeOptions()

# Customize options as needed  
options.add_argument("--headless")

driver = Chrome(options=options)

proxies = [
    "187.95.229.112:8080",
    "181.177.93.3:30309",
]

proxy = random.choice(proxies)
options.add_argument(f"--proxy-server={proxy}")

user_agents = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
]

user_agent = random.choice(user_agents)
options.add_argument(f"user-agent={user_agent}")

# Navigate to Deezer website
driver.get('https://www.deezer.com/en/channels/explore/')

# Wait for the privacy 'Accept' pop-up button to be visible
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, "gdpr-btn-accept-all")))

# Find and click the 'Accept' button on the privacy pop-up
agree_button = driver.find_element(By.XPATH, "//button[text()='Accept']")
agree_button.click()

# Scrape channel categories
categories = driver.find_elements(By.CLASS_NAME, 'picture-img')

# Print the text of each non-empty category
[print(category.text) for category in categories if category.text]

# Close the browser window after scraping
driver.quit()