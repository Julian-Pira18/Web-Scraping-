from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


url = 'https://www.linkedin.com/in/rey-sergio/' 

# enable headless mode in Selenium
options = Options()
options.add_argument('--headless=new')

driver = webdriver.Chrome(
    options=options, 
)

driver.get(url) 

exercise_cards = driver.find_element(By.XPATH, '//*[@id="public_profile_contextual-sign-in"]/div/section/div/div/img')


print("Link Image:",exercise_cards.get_attribute('src'))

# print(driver.page_source)

