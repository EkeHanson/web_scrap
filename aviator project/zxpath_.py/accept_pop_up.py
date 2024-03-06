# Import necessary modules for Selenium and ChromeDriver setup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Import modules for Selenium WebDriverWait and expected conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

# Initialize the ChromeDriver with the appropriate service and options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the specified URL
driver.get('https://www.deezer.com/en/channels/explore/')

# Maximize the browser window for better visibility
driver.maximize_window()

# Wait for the privacy 'Accept' pop-up button to be visible
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.ID, "gdpr-btn-accept-all")))

# Find and click the 'Accept' button on the privacy pop-up
agree_button = driver.find_element(By.XPATH, "//button[text()='Accept']")
agree_button.click()

# Scrape channel categories
categories = driver.find_elements(By.CLASS_NAME, 'picture-img')

# Print the text of each non-empty category
[print(category.text) for category in categories if category.text]