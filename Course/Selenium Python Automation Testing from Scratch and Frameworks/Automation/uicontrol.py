from selenium import webdriver
import time
#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj=Service("D:\AUTOM\Course\Selenium Python Automation Testing from Scratch and Frameworks\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break
    
    
radiobuttons=driver.find_elements(By.CSS_SELECTOR,".radioButton")
radiobuttons[2].click()

assert radiobuttons[2].is_selected()


assert driver.find_element(By.ID,"displayed-text").is_displayed()


driver.find_element(By.ID,"hide-textbox").click()


assert  driver.find_element(By.ID,"displayed-text").is_displayed()


time.sleep(5)





