from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Selenium WebDriver (make sure you have the appropriate driver installed, e.g., chromedriver for Chrome)
driver = webdriver.Chrome()

# Load the webpage containing the iframe
driver.get("https://www.sportybet.com/ng/sportygames/lobby")

# Wait for the iframe to be present and switch to it
iframe_locator = (By.ID, "games-lobby")
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(iframe_locator))

# Now execute JavaScript within the iframe to print out its contents
script = """
var elements = document.querySelectorAll('*');
for (var i = 0; i < elements.length; i++) {
    console.log(elements[i]);
}
"""
driver.execute_script(script)

# Once you're done, you may want to switch back to the main frame
driver.switch_to.default_content()

# Don't forget to close the browser when done
driver.quit()
