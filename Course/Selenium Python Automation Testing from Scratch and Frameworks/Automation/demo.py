from selenium import webdriver
import time
#Chrome driver
from selenium.webdriver.chrome.service import Service
service_obj=Service("D:\AUTOM\Course\Selenium Python Automation Testing from Scratch and Frameworks\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
#get() responsible for hit the urls in the browser
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
title=driver.title

url=driver.current_url
print(title,url)
driver.get("https://courses.rahulshettyacademy.com/courses/")
# driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()
