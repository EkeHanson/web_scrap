from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from colorama import Fore
from fake_useragent import UserAgent  # Import UserAgent class for User-Agent rotation
magenta, green, red = Fore.MAGENTA, Fore.GREEN, Fore.RED

user_agent = UserAgent()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--enable-logging")

chrome_options.add_argument(f"user-agent={user_agent.random}")

driver = webdriver.Chrome(options=chrome_options)
driver.get('www.sportybet.com/ng/sportygames/lobby')

def main():
    click_aviator()

def click_aviator():
    print(f'The current URL: {driver.current_url}')

    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div/div/div/div[4]/div/div[1]/div/span')))
        print("Aviator Element found within the iframe:", element.text)
        print(f"{green}About to click the Aviator  Element")
        element.click()
        print(f"{green}Aviator  Element clicked")

    except NoSuchElementException:
        print('iframe element not found')
    except TimeoutException:
        print('Timeout: Times elapsed for element to be found')
    except StaleElementReferenceException:
        print('Stale Element Reference: The aviator element is no longer attached to the DOM')


if __name__ == "__main__":
    click_aviator()
