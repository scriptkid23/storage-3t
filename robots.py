from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import key
driver = webdriver.Firefox(executable_path="D:\\code\\venv\\geckodriver.exe")
driver.get("https://facebook.com")

email       = "email"
password    = "pass"
login       = "loginbutton"

emailElement = driver.find_element_by_name(email)
passElement = driver.find_element_by_name(password)

emailElement.send_keys(key.username)
passElement.send_keys(key.password)

loginElement = driver.find_element_by_id(login)
loginElement.click()

driver.get("https://www.facebook.com/profile.php?id=100025689443100")
searchElement = driver.find_element_by_xpath("//input[@class='_1frb']")

searchButtonElement.click()
postbutton.click()




