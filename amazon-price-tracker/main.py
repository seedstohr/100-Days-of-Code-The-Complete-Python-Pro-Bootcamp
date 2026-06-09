import os
import smtplib
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

PRODUCT_URL = "https://www.amazon.com/Fanttik-F2-Master-Accessories-Polishing/dp/B0DN1GBTDG/?_encoding=UTF8&pd_rd_w=c5Gsv&content-id=amzn1.sym.11f23f75-49f9-427b-b8bd-7ba3d113eed4&pf_rd_p=11f23f75-49f9-427b-b8bd-7ba3d113eed4&pf_rd_r=12460A3Y8C76JTCHG5ME&pd_rd_wg=hyAmc&pd_rd_r=6feb6df5-1102-4020-a36b-2a4ed3c99c65&ref_=pd_hp_d_r_btf_dealz_dotda_t1_hxwDSD_sspa_dk_gateway&ie=UTF8&sloctc=1&sp_csd=d2lkZ2V0TmFtZT1zcF9ob21lcGFnZV9ibGVuZGVk&th=1"

PRICE_TARGET = 100.00

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
MY_EMAIL = os.getenv("MY_EMAIL")
EMAIL_AUTH = os.getenv("EMAIL_AUTH")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36", # Mimics a real browser
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/", # Useful for initial requests
    "DNT": "1",
    "Connection": "keep-alive"
}

url_request = requests.get(PRODUCT_URL, headers=headers)

url_soup = BeautifulSoup(url_request.content, "html.parser")

product_name = (url_soup.find("span", id="productTitle", class_="a-size-large product-title-word-break").getText()
                ).encode('ascii', 'ignore').decode('ascii')


current_price = float(
    url_soup.find("span", id="apex-pricetopay-accessibility-label").getText().strip().split()[0]
    .replace("$", ""))

if current_price < PRICE_TARGET:
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_AUTH)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Amazon Price Alert\n\n"
                f"{product_name} is now {current_price}.")