from datetime import datetime
import requests
from bs4 import BeautifulSoup as soup

# Table Width
tbl_len_out = 80
tbl_len_in = 24

# Date and Time
now = datetime.now()
today = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

company = "Türkiye İş Bankası"
url = "https://www.isbank.com.tr/en/foreign-exchange-rates"
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

req = requests.get(url, headers=header)
page_soup = soup(req.content.decode('utf-8','ignore').encode("utf-8"), 'html5lib')
table_currency = {}

currency_list = {
    "USD": "ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl00_fxItem",
    "EUR": "ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl01_fxItem",
    "GBP": "ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl02_fxItem",
    "AUD": "ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl03_fxItem",
    "CAD": "ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl04_fxItem",
    "DKK": "ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl05_fxItem",
    "JPY": "ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl06_fxItem",
    "KWD": "ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl07_fxItem",
    "NOK": "ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl08_fxItem",
    "SAR": "ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl09_fxItem",
    "SEK": "ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl10_fxItem",
    "CHF": "ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl11_fxItem"}

def get_currency():
    try:
        for (key, val) in currency_list.items():
            # Currency
            bank_currency = page_soup.find_all('tr', {"id":val})[0]
            buy = float(bank_currency.find_all('td')[1].text.strip().replace(",","."))
            sell = float(bank_currency.find_all('td')[2].text.strip().replace(",","."))
            table_currency.setdefault(key, []).append(buy)
            table_currency.setdefault(key, []).append(sell)
    except IndexError:
        return("IndexError")

# Currency Query
def price(inp):
    if req.status_code != 200:
        return(f"Hata : HTTP {req.status_code}")
    else:
        if get_currency() == "IndexError":
            return(f"Hata : Sayfanın kaynak kodunda döviz bilgisi bulunamadı.")
        else:
            for key in table_currency:
                if key == inp:
                    return (inp, table_currency[inp][0], table_currency[inp][1])

# Main function
def main():
    if req.status_code != 200:
        print(f"\n{' Döviz Kurları ':=^{tbl_len_out}}")
        print(f"\n{' Kaynak':<{tbl_len_in}} : {company}")
        print(f"{' Tarih':<{tbl_len_in}} : {today}")
        print(f"{' Zaman':<{tbl_len_in}} : {time}")
        print(f"\n{' Hata':<{tbl_len_in}} : HTTP {req.status_code}")
        print(f"\n{'':=^{tbl_len_out}}\n")
    else:
        print(f"\n{' Döviz Kurları ':=^{tbl_len_out}}")
        print(f"\n{' Kaynak':<{tbl_len_in}} : {company}")
        print(f"{' Tarih':<{tbl_len_in}} : {today}")
        print(f"{' Zaman':<{tbl_len_in}} : {time}")
        if get_currency() == "IndexError":
            print(f"\n{' Hata':<{tbl_len_in}} : Sayfanın kaynak kodunda döviz bilgisi bulunamadı.")
            print(f"{'':<{tbl_len_in}}   Lütfen URL adresini ve yazılım kodunu kontrol ediniz.")
            print(f"\n{'':=^{tbl_len_out}}\n")
        else:
            # Print Currencies and rates
            print(f"\n{' Kod  Döviz':<{tbl_len_in}} : Alış\t\tSatış")
            print(f" {'':-^{3}}  {'':-^{tbl_len_in-5}}  {'':-^{9}}    {'':-^{9}}")
            print(f"{' USD  ABD Doları':<{tbl_len_in}} : {table_currency['USD'][0]}\t{table_currency['USD'][1]}")
            print(f"{' EUR  Euro':<{tbl_len_in}} : {table_currency['EUR'][0]}\t{table_currency['EUR'][1]}")
            print(f"{' GBP  İngiliz Sterlini':<{tbl_len_in}} : {table_currency['GBP'][0]}\t{table_currency['GBP'][1]}")
            print(f"{' AUD  Avustralya Doları':<{tbl_len_in}} : {table_currency['AUD'][0]}\t{table_currency['AUD'][1]}")
            print(f"{' DKK  Danimarka Kronu':<{tbl_len_in}} : {table_currency['DKK'][0]}\t{table_currency['DKK'][1]}")
            print(f"{' JPY  Japon Yeni':<{tbl_len_in}} : {table_currency['JPY'][0]}\t{table_currency['JPY'][1]}")
            print(f"{' SEK  İsveç Kronu':<{tbl_len_in}} : {table_currency['SEK'][0]}\t{table_currency['SEK'][1]}")
            print(f"{' CHF  İsviçre Frangı':<{tbl_len_in}} : {table_currency['CHF'][0]}\t{table_currency['CHF'][1]}")
            print(f"{' CAD  Kanada Doları':<{tbl_len_in}} : {table_currency['CAD'][0]}\t{table_currency['CAD'][1]}")
            print(f"{' KWD  Kuveyt Dinarı':<{tbl_len_in}} : {table_currency['KWD'][0]}\t{table_currency['KWD'][1]}")
            print(f"{' NOK  Norveç Kronu':<{tbl_len_in}} : {table_currency['NOK'][0]}\t{table_currency['NOK'][1]}")
            print(f"{' SAR  Suudi Riyali':<{tbl_len_in}} : {table_currency['SAR'][0]}\t{table_currency['SAR'][1]}")
            print(f"\n{'':=^{tbl_len_out}}\n")

if __name__ == "__main__":
    main()  