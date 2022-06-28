# Web sayfasından otomatik akaryakıt fiyatlarını alan script

from datetime import datetime
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

now = datetime.now()
today = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

url = "https://www.isbank.com.tr/en/foreign-exchange-rates"
company = "Türkiye İş Bankası"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
uClient = urllib.request.urlopen(req)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html.decode('utf-8','ignore').encode("utf-8"), 'html5lib')
# US Dollar
table_usd = page_soup.find_all('tr', {"id":"ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl00_fxItem"})[0]
usd_buy = table_usd.find_all('td')[1].text.strip()
usd_sell = table_usd.find_all('td')[2].text.strip()
# Euro
table_eur = page_soup.find_all('tr', {"id":"ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl01_fxItem"})[0]
eur_buy = table_eur.find_all('td')[1].text.strip()
eur_sell = table_eur.find_all('td')[2].text.strip()
# GB Pound
table_gbp = page_soup.find_all('tr', {"id":"ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl02_fxItem"})[0]
gbp_buy = table_gbp.find_all('td')[1].text.strip()
gbp_sell = table_gbp.find_all('td')[2].text.strip()
# Australian Dollar
table_aud = page_soup.find_all('tr', {"id":"ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl03_fxItem"})[0]
aud_buy = table_aud.find_all('td')[1].text.strip()
aud_sell = table_aud.find_all('td')[2].text.strip()
# Canadian Dollar
table_cad = page_soup.find_all('tr', {"id":"ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl04_fxItem"})[0]
cad_buy = table_cad.find_all('td')[1].text.strip()
cad_sell = table_cad.find_all('td')[2].text.strip()
# Danish Krone
table_dkk = page_soup.find_all('tr', {"id":"ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl05_fxItem"})[0]
dkk_buy = table_dkk.find_all('td')[1].text.strip()
dkk_sell = table_dkk.find_all('td')[2].text.strip()
# Japanese Yen
table_jpy = page_soup.find_all('tr', {"id":"ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl06_fxItem"})[0]
jpy_buy = table_jpy.find_all('td')[1].text.strip()
jpy_sell = table_jpy.find_all('td')[2].text.strip()
# Kuwait Dinar
table_kwd = page_soup.find_all('tr', {"id":"ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl07_fxItem"})[0]
kwd_buy = table_kwd.find_all('td')[1].text.strip()
kwd_sell = table_kwd.find_all('td')[2].text.strip()
# Norwegian Krone
table_nok = page_soup.find_all('tr', {"id":"ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl08_fxItem"})[0]
nok_buy = table_nok.find_all('td')[1].text.strip()
nok_sell = table_nok.find_all('td')[2].text.strip()
# Saudi Riyal
table_sar = page_soup.find_all('tr', {"id":"ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl09_fxItem"})[0]
sar_buy = table_sar.find_all('td')[1].text.strip()
sar_sell = table_sar.find_all('td')[2].text.strip()
# Swedish Krona
table_sek = page_soup.find_all('tr', {"id":"ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl10_fxItem"})[0]
sek_buy = table_sek.find_all('td')[1].text.strip()
sek_sell = table_sek.find_all('td')[2].text.strip()
# Swiss Franc
table_chf = page_soup.find_all('tr', {"id":"ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl11_fxItem"})[0]
chf_buy = table_chf.find_all('td')[1].text.strip()
chf_sell = table_chf.find_all('td')[2].text.strip()

clear()
print(f"\n{' Döviz Kurları ':=^{tbl_len_out}}")
print(f"\n{' Kaynak':<{tbl_len_in}} : {company}")
print(f"{' Tarih':<{tbl_len_in}} : {today}")
print(f"{' Zaman':<{tbl_len_in}} : {time}")

print(f"\n{' Döviz':<{tbl_len_in}} : Alış\tSatış")
print(f" {'':-^{tbl_len_in}}  {'':-^{10}} {'':-^{10}}")
print(f"{' US Dolar':<{tbl_len_in}} : {usd_buy} \t{usd_sell}")
print(f"{' Euro':<{tbl_len_in}} : {eur_buy} \t{eur_sell}")
print(f"{' GB Pound':<{tbl_len_in}} : {gbp_buy} \t{gbp_sell}")
print(f"{' Australian Dollar':<{tbl_len_in}} : {aud_buy} \t{aud_sell}")
print(f"{' Canadian Dollar':<{tbl_len_in}} : {cad_buy} \t{cad_sell}")
print(f"{' Danish Krone':<{tbl_len_in}} : {dkk_buy} \t{dkk_sell}")
print(f"{' Japanese Yen':<{tbl_len_in}} : {jpy_buy} \t{jpy_sell}")
print(f"{' Kuwait Dinar':<{tbl_len_in}} : {kwd_buy} \t{kwd_sell}")
print(f"{' Norwegian Krone':<{tbl_len_in}} : {nok_buy} \t{nok_sell}")
print(f"{' Saudi Riyal':<{tbl_len_in}} : {sar_buy} \t{sar_sell}")
print(f"{' Swedish Krona':<{tbl_len_in}} : {sek_buy} \t{sek_sell}")
print(f"{' Swiss Franc':<{tbl_len_in}} : {chf_buy} \t{chf_sell}")
print(f"\n{'':=^{tbl_len_out}}\n")