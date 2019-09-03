import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/gp/cart/view.html?ref_=nav_cart'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

def check_price(): 
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    # print(title.strip())

    price = soup.find(id="priceblock_ourprice").get_text()

    # need float value of price
    converted_price = float(price[0:5])
    # print(converted_price)

    desiredPrice = converted_price - 1; 

    if(converted_price <= desiredPrice):
        send_mail()

def send_mail(): 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('shyamp1204@utexas.edu', '***********') #password hidden for github
    subject = 'The Price of Your Desired Item Fell!!!'
    body = 'Check your amazon account and get the cheaper item at ' + URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'shyamp1204@utexas.edu'
        'shyamp1204@utexas.edu'
        msg
    )

    print("email has been sent")

    server.quit()

    while(True):
        check_price()
        time.sleep(60*60*24)
    
    
