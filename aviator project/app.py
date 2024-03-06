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
driver.get('https://www.sportybet.com/ng/games')

YOUR_PASSWORD = "123@Abraham@123"
YOUR_PHONE = "8146955393"

def main():
    logging()
    print("About to click the  Casino button")
    click_casino()
    print("About to click Aviators")
    click_aviator()

def logging():
    print(f'{magenta} About to send Phone')
    email = driver.find_element(By.XPATH, value='//*[@id="j_page_header"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/input')
    email.send_keys(f"{YOUR_PHONE}")
    print(f"{green} Phone Number logged")

    password = driver.find_element(By.XPATH, value='//*[@id="j_page_header"]/div[1]/div/div[1]/div[1]/div[2]/div[3]/div[1]/input')
    password.send_keys(f"{YOUR_PASSWORD}")
    print(f"{red} Password logged")

    loggin = driver.find_element(By.XPATH, value='//*[@id="j_page_header"]/div[1]/div/div[1]/div[1]/div[2]/div[3]/div[1]/button')
    loggin.click()
    print(f"{red} Login Successful")

def click_casino():
    casino_locator = (By.XPATH, '//*[@id="header_nav_games"]')
    click_object(driver, casino_locator)
    print('Casino Clicked Successful')

def click_object(driver, locator, timeout=60):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
    element.click()


def click_aviator():
    print(f'The current URL: {driver.current_url}')
    try:
        # iframe = driver.find_element(By.ID, "games-lobby")
        # driver.switch_to.frame(iframe)
        iframe_locator = (By.ID, "games-lobby")
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(iframe_locator))

        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="game_item19"]/div/div/div/div[3]/div[2]/img')))
            print("Element found within the iframe:", element.text)
            element.click()
            print(f"{green}Element clicked")
        except:
            print("Element not found within the iframe")

        # Switch back to the default content
        driver.switch_to.default_content()
    except NoSuchElementException:
        print('Aviator element not found')
    except TimeoutException:
        print('Timeout: Times elapsed for element to be found')
    except StaleElementReferenceException:
        print('Stale Element Reference: The aviator element is no longer attached to the DOM')


if __name__ == "__main__":
    main()
