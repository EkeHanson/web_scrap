from undetected_chromedriver import ChromeOptions, Chrome
import random
from colorama import Fore

# Import modules for Selenium WebDriverWait and expected conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

options = ChromeOptions()

# Customize options as needed 
magenta, green, red = Fore.MAGENTA, Fore.GREEN, Fore.RED 
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
driver.get('https://www.sportybet.com/ng/games')

def logging():

    print('{magenta}About to send Phone')
    email = driver.find_element(By.XPATH, value='//*[@id="j_page_header"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/input')
    email.send_keys("8146955393")
    print(f"{green} Phone Number logged")


    password = driver.find_element(By.XPATH, value='//*[@id="j_page_header"]/div[1]/div/div[1]/div[1]/div[2]/div[3]/div[1]/input')
    password.send_keys("123@Abraham@123")
    print(f"{red} Password logged")

    loggin = driver.find_element(By.XPATH, value='//*[@id="j_page_header"]/div[1]/div/div[1]/div[1]/div[2]/div[3]/div[1]/button')
    loggin.click()
    print(f"{red} Login Successful")

user_agent = random.choice(user_agents)
options.add_argument(f"user-agent={user_agent}")


logging()

# Wait for the privacy 'Accept' pop-up button to be visible
wait = WebDriverWait(driver, 20)
wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="game_item19"]/div/div/div/div[3]/div[2]/img')))

# Find and click the 'Accept' button on the privacy pop-up
aviator_button = driver.find_element(By.XPATH,'//*[@id="game_item19"]/div/div/div/div[3]/div[2]/img')
aviator_button.click()


# driver.quit()