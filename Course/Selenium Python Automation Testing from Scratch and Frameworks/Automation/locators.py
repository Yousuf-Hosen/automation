from selenium import webdriver
import time
#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
service_obj=Service("D:\AUTOM\Course\Selenium Python Automation Testing from Scratch and Frameworks\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
#get() responsible for hit the urls in the browser
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

""" Locators
ID,XPath,CSSSelector,classname,LineText, 

"""

driver.find_element(By.NAME,"email").send_keys("Hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("HelloPassword")
driver.find_element(By.ID,"exampleCheck1").click()


# XPath creation
#//tagsname[@attribute='value']
driver.find_element(By.XPATH,"//input[@type='submit']").click()

message=driver.find_element(By.CLASS_NAME,"alert-success").text

#CSS Selector --> tagname[attribute='value'],#id,.classname

driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Yousuf")
print(message)
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

#Static dropdown
dropdrown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
 # index start from 0
dropdrown.select_by_visible_text("Female")
dropdrown.select_by_index(0)
#dropdrown.select_by_value()


driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("hello again")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
assert "Success" in message

input_key=input("press Enter To close the browser..")
if input_key=='quit':
    driver.quit()
    




