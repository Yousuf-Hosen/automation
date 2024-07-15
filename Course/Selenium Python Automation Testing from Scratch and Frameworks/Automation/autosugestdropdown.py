from selenium import webdriver
import time
#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj=Service("D:\AUTOM\Course\Selenium Python Automation Testing from Scratch and Frameworks\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise")
driver.find_element(By.ID,'autosuggest').send_keys('ind')
time.sleep(2)
 
countries=driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")

for country in countries:
    if country.text == "india":
        country.click()
        break
    
