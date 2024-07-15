from selenium import webdriver
import time
#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

service_obj=Service("D:\AUTOM\Course\Selenium Python Automation Testing from Scratch and Frameworks\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice")

wait = WebDriverWait(driver, 10)
table = wait.until(EC.presence_of_element_located((By.ID, 'product')))
headers=table.find_elements(By.TAG_NAME,'th')

header_texts=[header.text for header in headers]
    
    
rows=table.find_elements(By.TAG_NAME,'tr')
print(len(rows))

with open('course.csv','w',newline='') as file:
    writter=csv.writer(file)
    writter.writerow(header_texts)
    for row in rows[1:]:
        data=[cell.text for cell in row.find_elements(By.TAG_NAME,'td')]
        writter.writerow(data)
       







