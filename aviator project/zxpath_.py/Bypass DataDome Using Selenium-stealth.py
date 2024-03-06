from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

# Create a ChromeOptions object
custom_options = webdriver.ChromeOptions()

# Run in headless mode
custom_options.add_argument("--headless")
# Disable the AutomationControlled feature of Blink rendering engine
custom_options.add_argument('--disable-blink-features=AutomationControlled')
# Disable pop-up blocking
custom_options.add_argument('--disable-popup-blocking')
# Start the browser window in maximized mode
custom_options.add_argument('--start-maximized')
# Disable extensions
custom_options.add_argument('--disable-extensions')
# Disable sandbox mode
custom_options.add_argument('--no-sandbox')
# Disable shared memory usage
custom_options.add_argument('--disable-dev-shm-usage')

# Initialize the ChromeDriver with the appropriate service and custom options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=custom_options)

# Change the property value of the navigator for webdriver to undefined
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# Step 3: Rotate user agents
custom_user_agents = [
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
]

# Select a random user agent
custom_user_agent = random.choice(custom_user_agents)

# Pass in the selected user agent as an argument
custom_options.add_argument(f'user-agent={custom_user_agent}')

# Set user agent using execute_cpd_cmd
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": custom_user_agent})

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

# Navigate to Deezer website
driver.get('https://www.deezer.com/en/channels/explore/')

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
