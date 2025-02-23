from bs4 import BeautifulSoup
import requests
import time
from datetime import date
import csv

urls= ["https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch","https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch",
       "https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch","https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"]
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
today = str(date.today()) + ".csv"
csv_file = open(today, "w")
csv_writter=csv.writer(csv_file) # if file not exists it create new one
csv_writter.writerow(['Stock Name','Current Price','Previous Close','Open','Bid','Ask','Day Range','52 Week Range','Volume','Avg. Volume'])
length=len(urls)
task=1
for url in urls:
    stock=[]
    html_page=requests.get(url,headers=headers)
    soup=BeautifulSoup(html_page.content,'lxml')
    header_info=soup.find_all("div",id="quote-header-info")[0]
    stock_title=header_info.find("h1").get_text()
    current_price=header_info.find("div",class_="My(6px) Pos(r) smartphone_Mt(6px) W(100%)").find("fin-streamer").get_text()

    stock.append(stock_title)
    stock.append(current_price)

    table_info=soup.find_all("div", class_="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all("tr")

    for i in range(0,8):
        value=table_info[i].find_all("td")[1].get_text()
        stock.append(value)
    
    csv_writter.writerow(stock)
    if length==0:
        break
    else:
        print(f"Work Done for url {task} ")
        task=task+1
        length=length-1
    time.sleep(5)
    
csv_file.close()

