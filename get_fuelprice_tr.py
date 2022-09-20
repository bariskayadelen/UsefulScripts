from datetime import datetime
import requests
from bs4 import BeautifulSoup as soup

company = "Aytemiz Petrol"
url = "https://www.aytemiz.com.tr/"
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

req = requests.get(url, headers=header)
page_soup = soup(req.content.decode('utf-8','ignore').encode("utf-8"), 'html5lib')
fuel_price = page_soup.find_all('div', {"class":"fuel-price"})[0].text.strip().strip('TL/LT')
diesel_price = page_soup.find_all('div', {"class":"fuel-price"})[1].text.strip().strip('TL/LT')
lpg_price = page_soup.find_all('div', {"class":"fuel-price"})[3].text.strip().strip('TL/LT')

def price(inp):
    if inp == 'fuel':
        return fuel_price
    elif inp == 'diesel':
        return diesel_price
    elif inp == 'lpg':
        return lpg_price
    elif inp == 'all':
        return fuel_price, diesel_price, lpg_price

# Main function
def main():
    # Table Width
    tbl_len_out = 74
    tbl_len_in = 24

    # Date and Time
    now = datetime.now()
    today = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    
    # Print Currencies and rates
    print(f"\n{' Akaryakıt Fiyatları ':=^{tbl_len_out}}")
    print(f"\n{' Kaynak':<{tbl_len_in}} : {company}")
    print(f"{' Tarih':<{tbl_len_in}} : {today}")
    print(f"{' Zaman':<{tbl_len_in}} : {time}")
    print(f"\n{' Benzin':<{tbl_len_in}} : {fuel_price} ₺")
    print(f"{' Motorin':<{tbl_len_in}} : {diesel_price} ₺")
    print(f"{' LPG':<{tbl_len_in}} : {lpg_price} ₺")
    print(f"\n{'':=^{tbl_len_out}}\n")

if __name__ == "__main__":
    main()