from selenium import webdriver
import time
#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj=Service("D:\AUTOM\Course\Selenium Python Automation Testing from Scratch and Frameworks\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
#get() responsible for hit the urls in the browser
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client")

driver.find_element(By.LINK_TEXT,"Forgot password?").click()

driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("yousufhasanrakib@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("YGDMjdE*k46UgC")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("YGDMjdE*k46UgC")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()
# YGDMjdE*k46UgC
input_key=input("press Enter To close the browser..")
if input_key=='q':
    driver.quit()