import requests
from bs4 import BeautifulSoup
import smtplib
import time
import sys

class tracker:
    url = 0
    traget_price = 0
    email = 0
    headers = 0

    def __init__(self):
        self.headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
        self.get_url()
        self.get_target_price()
     

    def get_url(self):
        self.url = input("Product Link: ")

    def get_target_price(self):
        self.target_price = float(input("Your Target price: "))

    def set_email(self, email):
        self.email = email
  
    def check_price(self):

        page = requests.get(self.url, headers = self.headers)

        soup1 = BeautifulSoup(page.content, 'html.parser')
        soup = BeautifulSoup(soup1.prettify(), "html.parser")

        try:
            title = soup.find(id = 'productTitle').get_text().strip()
        except:
            print('no title')

        try:
            price = soup.find(id = 'priceblock_ourprice').get_text()
        except:
            try:
                price = soup.find(id = 'priceblock_dealprice').get_text()
            except:
                print('no price avaliable')
                sys.exit(1)
    
        converted_price = float(price[1:]) 

        print(f'{title.strip()} {converted_price} checking')
        if converted_price < self.target_price :
            self.send_email(title)
            self.url = 0


    def send_email(self, title):
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('apc.2019cunyhackathon@gmail.com', 'CUNYhackathon')  
        
        subject = 'Price fell down!'
        body = "Check: " + self.url

        msg = f'Subject: {subject}\n\n{body}'
            
        
        server.sendmail(
            'sylvia94928@gmail.com',
            self.email,
            msg
        )

        print(f'Price drops\nEmail sent for {title}\n')

        server.quit()
        
   
def main():
    n = int(input('number of items:'))
    item_ls = []
    for i in range(n):
        new_tracker = tracker()
        item_ls.append(new_tracker)

        
    email = input("Your email address: ")
    
    for i in range(n):
        item_ls[i].set_email(email)

    while 1:
        for i in range(n):
            if item_ls[i].url != 0:
                item_ls[i].check_price()
            else:
                continue
            
        time.sleep(5)
    

main()


