# def calculate_discount(item):
#     match item:
#         case "apple":
#             discount = 0.1
#         case "banana":
#             discount = 0.15
#         case "orange":
#             discount = 0.2
#         case _:
#             discount = 0 # default case
#     return discount

# item_name = input("Item name : ")
# discount_rate = calculate_discount(item_name)
# print (f"The discount rate for {item_name} is {discount_rate * 100}%")

from os import system, name
import requests
from bs4 import BeautifulSoup as soup

# Ekranı Temizleme 
def clear():
    # windows için
    if name == 'nt':
        _ = system('cls')
    # mac, linux vb. için
    else:
        _ = system('clear')

def exchange(inp, amount):
    url = "https://www.isbank.com.tr/en/foreign-exchange-rates"
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    req = requests.get(url, headers=header)
    page_soup = soup(req.content.decode('utf-8','ignore').encode("utf-8"), 'html5lib')

    if inp == "USD":
        # US Dollar
        table_usd = page_soup.find_all('tr', {"id":"ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl00_fxItem"})[0]
        usd_sell = table_usd.find_all('td')[2].text.strip().replace(",",".")
        total = float(usd_sell) * amount
        return total
    elif inp == "EUR":
        # Euro
        table_eur = page_soup.find_all('tr', {"id":"ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl01_fxItem"})[0]
        eur_sell = table_eur.find_all('td')[2].text.strip().replace(",",".")
        total = float(eur_sell) * amount
        return total

# ÖTV, Özel Tüketim Vergisi hesaplama
def otv_hesapla(motor_tipi, motor_gucu, motor_hacmi, satis_fiyati):
    # Benzinli/Dizel Motor gucunden OTV orani hesaplama
    if motor_tipi == 1:
        if motor_hacmi < 1600 and satis_fiyati < 184000:
            return 45
        elif motor_hacmi < 1600 and 184000 <= satis_fiyati < 220000:
            return 50
        elif motor_hacmi < 1600 and 220000 <= satis_fiyati < 250000:
            return 60
        elif motor_hacmi < 1600 and 250000 <= satis_fiyati < 280000:
            return 70
        elif motor_hacmi < 1600 and 280000 <= satis_fiyati:
            return 80
        elif 1600 <= motor_hacmi < 2000 and satis_fiyati < 170000:
            return 130
        elif 1600 <= motor_hacmi < 2000 and 170000 <= satis_fiyati:
            return 150    
        else:
            return 220
    # Hibrit Motor gucunden OTV orani hesaplama
    elif motor_tipi == 2:
        if 50 < motor_gucu and motor_hacmi < 1800 and satis_fiyati < 228000 :
            return 45
        elif 50 < motor_gucu and motor_hacmi < 1800 and 228000 <= satis_fiyati < 350000 :
            return 50
        elif 50 < motor_gucu and motor_hacmi < 1800 and 3500000 <= satis_fiyati :
            return 80
        elif 100 < motor_gucu and 2000 <= motor_hacmi < 2500 and satis_fiyati < 170000 :
            return 130
        elif 100 < motor_gucu and motor_hacmi < 2500 and 170000 <= satis_fiyati :
            return 150
        else :
            return 220
    # Elektrikli Motor gucunden OTV orani hesaplama 
    else:
        if motor_gucu < 160 and satis_fiyati < 1250000:
            return 10
        elif motor_gucu < 160:
            return 40
        elif 160 < motor_gucu and satis_fiyati < 1350000:
            return 50
        else:
            return 60

def menu_alt(inp):
    while True:
        # inp = input(f"\n [A] Ana menüye dön | [Q] Programdan Çık | Tercih: ")
        if inp.lower() == "q":
            print(f"\n{' İyi Günler ':=^{tbl_gen_dis}}\n")
            return "break"
        elif inp.lower() == "a":
            return "continue"
        else:
            # clear()
            # print(menu_title())
            print(f"\n Hata!!! Girmiş olduğunuz '{inp}' değeri menüde mevcut değildir.")
            print(f"\n Lütfen menü seçeneğini doğru giriniz!")
            print(f"\n{'':-^{tbl_gen_dis}}")
        continue

# Navlun ve Sigorta Bedeli 200 Euro
# navlun_sigorta = exchange('EUR', float(200))

# Sair Masraf Bedeli 150 Euro
# sair_masraf = exchange('EUR', float(150))

# Diger Bedeller Toplami 500 Euro
# diger_bedeller = exchange('EUR', float(500))

# Hizmet Bedeli 500 Euro
# hizmet_bedeli = exchange('EUR', float(500))

# KDV Orani
kdv_orani = 20

# Car Age
arac_yasi = lambda x,y : y-x if x<=y else print("Aracın üretim ve satış yıllarını kontrol ediniz.")

# Amortisman
amortisman_orani = lambda x : 0 if x == 0 else (20 if x == 1 else (30 if x == 2 else (40 if x == 3 else (50 if x == 4 else 60))))
amortisman_yuzdesi = amortisman_orani(arac_yasi) / 100

list_arac_durumu = {1:'Sıfır Araç',2:'İkinci El Araç'}
list_motor_tipi = {1:'Benzinli/Diesel',2:'Hibrit',3:'Elekrikli'}

# Tablo Genisligi
tbl_gen_dis = 72
tbl_gen_ic = 40

menu_title = f"\n{' Araç İthalatı Hesaplayıcısı ':=^{tbl_gen_dis}}"

# for a,b in motor_dict.items():
#     print(f"[{a}]", b)

# motor_tipi = input('\nMotor Tipi : ')
# otv = otv_hesapla(int(motor_tipi),0,1477,850000)
# print(f"\n{motor_dict[int(motor_tipi)]} motor tipi için ÖTV oranı %{otv}\n")

while True :
    inp_tercih = None
    inp_satin_alma_yili = None
    inp_yurda_giris_yili = None
    inp_motorgucu = None
    inp_motorhacmi = None
    inp_satisfiyati = None

    # Araç Durumu
    clear()
    print(menu_title)
    print(f"\nİthal etmek istediğiniz aracın durumunu seçiniz.\n")
    for a,b in list_arac_durumu.items():
        print(f"[{a}]", b)
    print(f"\n{'':-^{tbl_gen_dis}}")
    inp_arac_durumu = input(f"\n[Q] Programdan Çık | Tercih: ")
    # if menu_alt(inp_arac_durumu) == "break": break
    # Motor Tipi
    clear()
    print(menu_title)
    print(f"\nAraç motor tipini seçiniz.\n")
    for a,b in list_motor_tipi.items():
        print(f"[{a}]", b)
    print(f"\n{'':-^{tbl_gen_dis}}")
    inp_motor_tipi = input(f"\n[Q] Programdan Çık | Tercih: ")
    # if menu_alt(inp_motor_tipi) == "break": break
    # Motor Gücü ve/veya Hacmi
    # Araç Yaşı
    # Satın Alma Fiyatı
    clear()
    print(menu_title)
    print(f"\n{' Araç Bilgisi ':-^{tbl_gen_dis}}\n")
    print(f"{' Araç Durumu':<{tbl_gen_ic}} :", list_arac_durumu[int(inp_arac_durumu)])
    print(f"{' Motor Tipi':<{tbl_gen_ic}} :", list_motor_tipi[int(inp_motor_tipi)])
    if list_motor_tipi == 1:
        print(f"{' Motor Hacmi':<{tbl_gen_ic}} :", list_motor_tipi[int(inp_motor_tipi)])
    elif list_motor_tipi == 2:
        print(f"{' 2Motor Gücü':<{tbl_gen_ic}} :", list_motor_tipi[int(inp_motor_tipi)])
        print(f"{' Motor Hacmi':<{tbl_gen_ic}} :", list_motor_tipi[int(inp_motor_tipi)])
    else:
        print(f"{' Motor Gücü':<{tbl_gen_ic}} :", list_motor_tipi[int(inp_motor_tipi)])
    print(f"{' Aracın Satın Alma Yılı':<{tbl_gen_ic}} :", inp_motor_tipi)
    print(f"{' Aracın Türkiye Giriş Yılı':<{tbl_gen_ic}} :", inp_motor_tipi)
    print(f"{' Aracın Yaşı':<{tbl_gen_ic}} :", inp_motor_tipi)
    # print(f"{'Araca Uygulanacak Amortisman':<{tbl_gen_ic}} : {arac_yasi + 1}. Kademe %{amortisman_orani(arac_yasi)} Amortisman")
    # print(f"{'Amortisman Sonrası Araç Bedeli':<{tbl_gen_ic}} : {cif:{tplm_uz}.2f}₺")
    print(f"\n{' Vergiler ':-^{tbl_gen_dis}}\n")
    # print(f"{'Navlun, Sigorta ve Sair Masraf Bedeli':<{tbl_gen_ic}} : {navlun_sigorta + sair_masraf:{tplm_uz}.2f}₺")
    # print(f"{'Araca Uygulanacak ÖTV Bedeli ve Oranı':<{tbl_gen_ic}} : {otv:{tplm_uz}.2f}₺ (%{otv_orani})")
    # print(f"{'Araca Uygulanacak KDV Bedeli ve Oranı':<{tbl_gen_ic}} : {kdv:{tplm_uz}.2f}₺ (%{kdv_orani})")
    print(f"{'':-^{tbl_gen_ic}}")
    # print(f"{'Aracın ÖTV ve KDV Bedeli Toplamı':<{tbl_gen_ic}} : {vergi_toplami:{tplm_uz}.2f}₺")
    # print(f"\n{'Ruhsat, TRT Bandrol, TÜV, vs Bedeli':<{tbl_gen_ic}} : {diger_bedeller:{tplm_uz}.2f}₺")
    # print(f"{'Anahtar Teslim Hizmet Bedeli':<{tbl_gen_ic}} : {hizmet_bedeli:{tplm_uz}.2f}₺")
    print(f"{'':-^{tbl_gen_ic}}")
    # print(f"{'Aracın Türkiyedeki Toplam Masrafı':<{tbl_gen_ic}} : {turkiye_masrafi:{tplm_uz}.2f}₺")
    print(f"\n{'':-^{tbl_gen_dis}}")
    # print(f"\n{'Aracın Toplam Satınalma Maliyeti':<{tbl_gen_ic}} : {toplam:{tplm_uz}.2f}₺")
    print(f"\n{'':-^{tbl_gen_dis}}")
    inp_arac_durumu = input(f"\n[Q] Programdan Çık | Tercih: ")
    continue