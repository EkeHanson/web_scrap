from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

#Find element by Link text
first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("EKene-onwon")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Abraham")

email = driver.find_element(By.NAME, value="email")
email.send_keys("ekenehanson@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()




driver.quit()