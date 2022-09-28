# Exchange Office

from datetime import datetime
import requests
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

def menu_title():
    return (f"\n{' Exchange Office ':=^{tbl_len_out}}")

def menu_bottom():
    while True:
        print(f"\n{'':-^{tbl_len_out}}")
        inp = input(f"\n [A] Ana menüye dön | [Q] Programdan Çık | Tercih: ")
        if inp.lower() == "q":
            print(f"\n{' İyi Günler ':=^{tbl_len_out}}\n")
            return "break"
        elif inp.lower() == "a":
            return "continue"
        else:
            clear()
            print(menu_title())
            print(f"\n Hata!!! Girmiş olduğunuz '{inp}' değeri menüde mevcut değildir.")
            print(f"\n Lütfen menü seçeneğini doğru giriniz!")
        continue

def menu_exchange():
    print(f"\n {'Kod':{3}}   {'Döviz Adı':{17}}  {'Kod':{3}}   {'Döviz Adı':{17}}  {'Kod':{3}}   {'Döviz Adı':{17}}")
    print(f" {'':-^{3}}   {'':-^{17}}  {'':-^{3}}   {'':-^{17}}  {'':-^{3}}   {'':-^{17}}")
    print(f"{' USD : ABD Doları':<{tbl_len_menu}}{' DKK : Danimarka Kronu':<{tbl_len_menu}}{' CAD : Kanada Doları':<{tbl_len_menu}}")
    print(f"{' EUR : Euro':<{tbl_len_menu}}{' JPY : Japon Yeni':<{tbl_len_menu}}{' KWD : Kuveyt Dinarı':<{tbl_len_menu}}")
    print(f"{' GBP : İngiliz Sterlini':<{tbl_len_menu}}{' SEK : İsveç Kronu':<{tbl_len_menu}}{' NOK : Norveç Kronu':<{tbl_len_menu}}")
    print(f"{' AUD : Avustralya Doları':<{tbl_len_menu}}{' CHF : İsviçre Frangı':<{tbl_len_menu}}{' SAR : Suudi Riyali':<{tbl_len_menu}}")

def check_currency(inp):
    while True:
        if inp.upper() == 'USD':
            x = 'USD'
            y = float(usd_buy.replace(",","."))
            z = float(usd_sell.replace(",","."))
            return x, y, z
        elif inp.upper() == 'EUR':
            x = 'EUR'
            y = float(eur_buy.replace(",","."))
            z = float(eur_sell.replace(",","."))
            return x, y, z
        elif inp.upper() == 'GBP':
            x = 'GBP'
            y = float(gbp_buy.replace(",","."))
            z = float(gbp_sell.replace(",","."))
            return x, y, z
        elif inp.upper() == 'AUD':
            x = 'AUD'
            y = float(aud_buy.replace(",","."))
            z = float(aud_sell.replace(",","."))
            return x, y, z
        elif inp.upper() == 'DKK':
            x = 'DKK'
            y = float(dkk_buy.replace(",","."))
            z = float(dkk_sell.replace(",","."))
            return x, y, z
        elif inp.upper() == 'JPY':
            x = 'JPY'
            y = float(jpy_buy.replace(",","."))
            z = float(jpy_sell.replace(",","."))
            return x, y, z
        elif inp.upper() == 'SEK':
            x = 'SEK'
            y = float(sek_buy.replace(",","."))
            z = float(sek_sell.replace(",","."))
            return x, y, z
        elif inp.upper() == 'CHF':
            x = 'CHF'
            y = float(chf_buy.replace(",","."))
            z = float(chf_sell.replace(",","."))
            return x, y, z
        elif inp.upper() == 'CAD':
            x = 'CAD'
            y = float(cad_buy.replace(",","."))
            z = float(cad_sell.replace(",","."))
            return x, y, z
        elif inp.upper() == 'KWD':
            x = 'KWD'
            y = float(kwd_buy.replace(",","."))
            z = float(kwd_sell.replace(",","."))
            return x, y, z
        elif inp.upper() == 'NOK':
            x = 'NOK'
            y = float(nok_buy.replace(",","."))
            z = float(nok_sell.replace(",","."))
            return x, y, z
        elif inp.upper() == 'SAR':
            x = 'SAR'
            y = float(sar_buy.replace(",","."))
            z = float(sar_sell.replace(",","."))
            return x, y, z
        else:
            clear()
            print(menu_title())
            print("\n Satmak istediğiniz döviz cinsinin kodunu ve miktarını giriniz")
            menu_exchange()
            print(f"\n{'':-^{tbl_len_out}}")
            print(f"\n Hata!!! Girmiş olduğunuz '{inp}' değeri menüde mevcut değildir.")
            print(f"\n Lütfen menüdeki bir değeri giriniz!")
            inp = input(f"\n{' Döviz Cinsi ':<{tbl_len_in}}: ")
        continue

def check_amount(inp, currency):
    while True:
        try:
            x = float(inp)
            return x
        except:
            clear()
            print(menu_title())
            print("\n Satmak istediğiniz döviz cinsinin kodunu ve miktarını giriniz")
            menu_exchange()
            print(f"\n{' Döviz Cinsi ':<{tbl_len_in}}: {currency[0]}")
            print(f"\n{'':-^{tbl_len_out}}")
            print(f"\n Hata!!! Girmiş olduğunuz '{inp}' değeri sayısal bir değer değildir.")
            print(f"\n Lütfen sayısal bir değer giriniz!")
            inp = input(f"\n{' Döviz Miktarı ':<{tbl_len_in}}: ")
        continue

# Table Width
tbl_len_out = 74
tbl_len_in = 24
tbl_len_menu = 25

now = datetime.now()
today = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

company = "Türkiye İş Bankası"
url = "https://www.isbank.com.tr/en/foreign-exchange-rates"
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

req = requests.get(url, headers=header)
page_soup = soup(req.content.decode('utf-8','ignore').encode("utf-8"), 'html5lib')

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

while True:
    clear()
    print(menu_title())
    print(f"\n{' Kaynak':<{tbl_len_in}} : {company}")
    print(f"{' Tarih':<{tbl_len_in}} : {today}")
    print(f"{' Zaman':<{tbl_len_in}} : {time}")
    print(f"\n{' Kod  Döviz':<{tbl_len_in}} : Alış\t\tSatış")
    print(f" {'':-^{3}}  {'':-^{tbl_len_in-5}}  {'':-^{9}}    {'':-^{9}}")
    print(f"{' USD  ABD Doları':<{tbl_len_in}} : {usd_buy} \t{usd_sell}")
    print(f"{' EUR  Euro':<{tbl_len_in}} : {eur_buy} \t{eur_sell}")
    print(f"{' GBP  İngiliz Sterlini':<{tbl_len_in}} : {gbp_buy} \t{gbp_sell}")
    print(f"{' AUD  Avustralya Doları':<{tbl_len_in}} : {aud_buy} \t{aud_sell}")
    print(f"{' DKK  Danimarka Kronu':<{tbl_len_in}} : {dkk_buy} \t{dkk_sell}")
    print(f"{' JPY  Japon Yeni':<{tbl_len_in}} : {jpy_buy} \t{jpy_sell}")
    print(f"{' SEK  İsveç Kronu':<{tbl_len_in}} : {sek_buy} \t{sek_sell}")
    print(f"{' CHF  İsviçre Frangı':<{tbl_len_in}} : {chf_buy} \t{chf_sell}")
    print(f"{' CAD  Kanada Doları':<{tbl_len_in}} : {cad_buy} \t{cad_sell}")
    print(f"{' KWD  Kuveyt Dinarı':<{tbl_len_in}} : {kwd_buy} \t{kwd_sell}")
    print(f"{' NOK  Norveç Kronu':<{tbl_len_in}} : {nok_buy} \t{nok_sell}")
    print(f"{' SAR  Suudi Riyali':<{tbl_len_in}} : {sar_buy} \t{sar_sell}")
    print(f"\n{'':-^{tbl_len_out}}")
    print(f"\n Lütfen yapmak istediğiniz işlemi seçiniz.")
    print(f"\n [1] Döviz al")
    print(f" [2] Döviz sat")
    # print(f" [3] Arbitraj yap")
    print(f"\n{'':-^{tbl_len_out}}")
    inp_menu = input(f"\n[Q] Programdan Çık | Tercih: ")

    if inp_menu.lower() == "q":
        print(f"\n{' İyi Günler ':=^{tbl_len_out}}\n")
        break

    elif inp_menu == "1":
        clear()
        print(menu_title())
        print("\n Satın almak istediğiniz döviz cinsini ve miktarını giriniz")
        menu_exchange()
        currency = check_currency(input(f"\n{' Döviz Cinsi ':<{tbl_len_in}}: "))
        amount = check_amount(input(f"{' Döviz Miktarı ':<{tbl_len_in}}: "),currency)
        clear()
        print(menu_title())
        print("\n Satın almak istediğiniz döviz cinsini ve miktarını giriniz")
        menu_exchange()
        print(f"\n{' Döviz Cinsi ':<{tbl_len_in}}: {currency[0]}")
        print(f"{' Döviz Miktarı ':<{tbl_len_in}}: {amount}")
        total = round(amount * currency[2],2)
        print(f"\n {amount} {currency[0]} {total} ₺'ye eşittir. ")
        if menu_bottom() == "break": break

    elif inp_menu == "2":
        clear()
        print(menu_title())
        print("\n Satmak istediğiniz döviz cinsinin kodunu ve miktarını giriniz")
        menu_exchange()
        currency = check_currency(input(f"\n{' Döviz Cinsi ':<{tbl_len_in}}: "))
        amount = check_amount(input(f"{' Döviz Miktarı ':<{tbl_len_in}}: "),currency)
        clear()
        print(menu_title())
        print("\n Satmak istediğiniz döviz cinsinin kodunu ve miktarını giriniz")
        menu_exchange()
        print(f"\n{' Döviz Cinsi ':<{tbl_len_in}}: {currency[0]}")
        print(f"{' Döviz Miktarı ':<{tbl_len_in}}: {amount}")
        total = round(amount * currency[1],2)
        print(f"\n {amount} {currency[0]} {total} ₺'ye eşittir. ")
        if menu_bottom() == "break": break

    # elif inp_menu == "3":
    #     clear()
    #     print(menu_title())
    #     if menu_bottom() == "break": break

    else:
        clear()
        print(menu_title())
        print(f"\n Hata!!! Girmiş olduğunuz '{inp_menu}' değeri menüde mevcut değildir.")
        print(f"\n Lütfen menü seçeneğini doğru giriniz!")
        if menu_bottom() == "break": break
    continue