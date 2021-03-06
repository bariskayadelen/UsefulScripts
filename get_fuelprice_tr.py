# Web sayfasından otomatik akaryakıt fiyatlarını alan script

import datetime
import urllib.request
from bs4 import BeautifulSoup as soup
from os import system, name

# Define clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Table Width
tbl_len_out = 72
tbl_len_in = 18

today = datetime.date.today()
url = "https://www.aytemiz.com.tr/"
company = "Aytemiz Petrol"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
uClient = urllib.request.urlopen(req)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html.decode('utf-8','ignore').encode("utf-8"), 'html5lib')
fuel_price = page_soup.find_all('div', {"class":"fuel-price"})[0].text.strip().strip('TL/LT')
diesel_price = page_soup.find_all('div', {"class":"fuel-price"})[1].text.strip().strip('TL/LT')
lpg_price = page_soup.find_all('div', {"class":"fuel-price"})[3].text.strip().strip('TL/LT')

clear()
print(f"\n{' Güncel Akaryakıt Fiyatları ':=^{tbl_len_out}}")
print(f"\n Tarih  \tŞirket  \tBenzin Fiyatı\tDizel Fiyatı\tLPG Fiyatı")
print(f" {'':-^{13}}  {'':-^{13}}   {'':-^{13}}   {'':-^{13}}   {'':-^{13}}")
print(f" {today}\t{company}\t{fuel_price}\t\t{diesel_price}\t\t{lpg_price}\n")