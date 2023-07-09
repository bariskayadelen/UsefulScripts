# Diplomatik aracın Türkiye'ye getirildiğinde ödeyeceği vergiyi hesaplayıcı program

from unicodedata import numeric
from os import system, name
# from datetime import datetime
import requests
from bs4 import BeautifulSoup as soup

# Define clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def exchange(inp, amount):
    company = "Türkiye İş Bankası"
    url = "https://www.isbank.com.tr/en/foreign-exchange-rates"
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    req = requests.get(url, headers=header)
    page_soup = soup(req.content.decode('utf-8','ignore').encode("utf-8"), 'html5lib')

    if inp == "USD":
        # US Dollar
        table_usd = page_soup.find_all('tr', {"id":"ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl00_fxItem"})[0]
        # usd_buy = table_usd.find_all('td')[1].text.strip().replace(",",".")
        usd_sell = table_usd.find_all('td')[2].text.strip().replace(",",".")
        total = float(usd_sell) * amount
        return total
    elif inp == "EUR":
        # Euro
        table_eur = page_soup.find_all('tr', {"id":"ctl00_ctl18_g_6e26f0d7_7521_4191_b169_6f6bb7e95edc_ctl00_FxRatesRepeater_ctl01_fxItem"})[0]
        # eur_buy = table_eur.find_all('td')[1].text.strip().replace(",",".")
        eur_sell = table_eur.find_all('td')[2].text.strip().replace(",",".")
        total = float(eur_sell) * amount
        return total

# Araç Yaşından Amortisman Oranını Hesaplama
def amrtsmn(a) :
    if a == 0 :
        b = 0
        return b
    elif a == 1 :
        b = 20
        return b
    elif a == 2 :
        b = 30
        return b
    elif a == 3 :
        b = 40
        return b
    elif a == 4 :
        b = 50
        return b
    else :
        b = 60
        return b

# Elektrikli Motor gucunden OTV orani hesaplama 
# (a:Elektrik motor gucu, c:Satis fiyati)
def mtrgc_elktrk(a,c) :
    if a < 160 and c < 1250000 :
        d = 10
        return d
    elif a < 160 :
        d = 40
        return d
    elif 160 < a and c < 1350000 :
        d = 50
        return d
    else :
        d = 60
        return d

# Hibrit Motor gucunden OTV orani hesaplama 
# (a:Elektrik motor gucu, b:Motor hacmi, c:Satis fiyati)
# Kaynak: https://www.resmigazete.gov.tr/eskiler/2022/01/20220113-2.pdf
def mtrgc_hbrt(a,b,c) :
    if 50 < a and b < 1800 and c < 228000 :
        d = 45
        return d
    elif 50 < a and b < 1800 and 228000 <= b < 350000 :
        d = 50
        return d
    elif 50 < a and b < 1800 and 3500000 <= c :
        d = 80
        return d
    elif 100 < a and 2000 <= b < 2500 and c < 170000 :
        d = 130
        return d
    elif 100 < a and b < 2500 and 170000 <= c :
        d = 150
        return d
    else :
        d = 220
        return d

# Benzinli/Dizel Motor gucunden OTV orani hesaplama
# (a:Motor hacmi b:Satis fiyati)
# Kaynak: https://www.resmigazete.gov.tr/eskiler/2022/01/20220113-2.pdf
def mtrgc_bnzn(a,b) :
    if a < 1600 and b < 184000 :
        d = 45
        return d
    elif a < 1600 and 184000 <= b < 220000 :
        d = 50
        return d
    elif a < 1600 and 220000 <= b < 250000 :
        d = 60
        return d
    elif a < 1600 and 250000 <= b < 280000 :
        d = 70
        return d
    elif a < 1600 and 280000 <= b :
        d = 80
        return d
    elif 1600 <= a < 2000 and b < 170000 :
        d = 130
        return d
    elif 1600 <= a < 2000 and 170000 <= b :
        d = 150
        return d
    else :
        d = 220
        return d

def menu_title():
    return (f"\n{' Diplomatik Araç Vergisi Hesaplama ':=^{tbl_gen_dis}}")

def main_menu():
    print(menu_title())
    print(f"\nLütfen yapmak istediğiniz işlemi aşağıdaki menüden seçiniz:")
    print(f"\n [1] Elektrikli araç vergisi hesapla")
    print(f" [2] Hibrit araç vergisi hesapla")
    print(f" [3] Benzinli/Dizel araç vergisi hesapla")

def arac_satin_alma_yili():
    while True:
        inp = input("\n Araç satın alma yılını giriniz: ")
        try:
            satin_alma_yili = int(inp)
            return satin_alma_yili
        except:
            clear()
            print(menu_title())
            print(f"\n Hata!!! {inp} sayısal veri değildir. Lütfen sayısal veri giriniz!")
        continue

def menu_alt():
    while True:
        inp = input(f"\n [A] Ana menüye dön | [Q] Programdan Çık | Tercih: ")
        if inp.lower() == "q":
            print(f"\n{' İyi Günler ':=^{tbl_gen_dis}}\n")
            return "break"
        elif inp.lower() == "a":
            return "continue"
        else:
            clear()
            print(menu_title())
            print(f"\n Hata!!! Girmiş olduğunuz '{inp}' değeri menüde mevcut değildir.")
            print(f"\n Lütfen menü seçeneğini doğru giriniz!")
            print(f"\n{'':-^{tbl_gen_dis}}")
        continue

def arac_yurda_giris_yili():
    while True:
        inp = input("\n Aracın Türkiye\'ye giriş yılını giriniz: ")
        try:
            yurda_giris_yili = int(inp)
            return yurda_giris_yili
        except:
            clear()
            print(menu_title())
            print(f"\n Hata!!! {inp} sayısal veri değildir. Lütfen sayısal veri giriniz!")
        continue

def arac_motorgucu():
    while True:
        inp = input("\n Aracın motor gücünü kWh olarak giriniz: ")
        try:
            motorgucu = int(inp)
            return motorgucu
        except:
            clear()
            print(menu_title())
            print(f"\n Hata!!! {inp} sayısal veri değildir. Lütfen sayısal veri giriniz!")
        continue

def arac_motorhacmi():
    while True:
        inp = input("\n Aracın motor hacmini cc olarak giriniz: ")
        try:
            motorhacmi = int(inp)
            return motorhacmi
        except:
            clear()
            print(menu_title())
            print(f"\n Hata!!! {inp} sayısal veri değildir. Lütfen sayısal veri giriniz!")
        continue

def arac_satisfiyati():
    while True:
        inp = input("\n Aracın vergisiz satın alma bedelini ₺ olarak giriniz: ")
        try:
            satisfiyati = int(inp)
            return satisfiyati
        except:
            clear()
            print(menu_title())
            print(f"\n Hata!!! {inp} sayısal veri değildir. Lütfen sayısal veri giriniz!")
        continue

# KDV Orani
kdv_orani = 20

# Navlun ve Sigorta Bedeli 200 Euro
navlun_sigorta = exchange('EUR', float(200))

# Sair Masraf Bedeli 150 Euro
sair_masraf = exchange('EUR', float(150))

# Diger Bedeller Toplami 500 Euro
diger_bedeller = exchange('EUR', float(500))

# Hizmet Bedeli 500 Euro
hizmet_bedeli = exchange('EUR', float(500))

# Tablo Genisligi
tbl_gen_dis = 72
tbl_gen_ic = 40

while True :
    inp_tercih = None
    inp_satin_alma_yili = None
    inp_yurda_giris_yili = None
    inp_motorgucu = None
    inp_motorhacmi = None
    inp_satisfiyati = None

    clear()
    main_menu()
    print(f"\n{'':-^{tbl_gen_dis}}")
    inp_menu = input(f"\n[Q] Programdan Çık | Tercih: ")

    # Programdan Çıkış
    if inp_menu.lower() == "q":
        print(f"\n{' İyi Günler ':=^{tbl_gen_dis}}\n")
        break

    # Elektrikli Araç vergisi Hesaplama
    elif inp_menu == "1" :
        clear()
        print(menu_title())
        print(f"\n Elektrikli araç hesapla")
        yil_1 = arac_satin_alma_yili()
        yil_2 = arac_yurda_giris_yili()
        motorgucu = arac_motorgucu()
        satisfiyati = arac_satisfiyati()
        
        if yil_2 >= yil_1 :
            aracyasi = yil_2 - yil_1
        else :
            print(f"\n{' !!!!! ':-^{tbl_gen_dis}}")
            print(f"\n{'Satın alma tarihi Yurda giriş tarihinden küçük olmamaz.':^{tbl_gen_dis}}")
            print(f"\n{'Lütfen girdiğiniz değerleri kontrol ediniz!':^{tbl_gen_dis}}")
            print(f"\n{'':=^{tbl_gen_dis}}\n")
            continue
        
        otv_orani = mtrgc_elktrk(motorgucu,satisfiyati)
        aracyasi = yil_2 - yil_1

        amortisman_yuzdesi = amrtsmn(aracyasi) / 100

        # Vergiye Esas Bedel
        cif = round((satisfiyati * (100 - amrtsmn(aracyasi)) / 100) + navlun_sigorta,2)

        # OTV
        otv_matrahi = round(cif + sair_masraf,2)
        otv = round(cif * otv_orani / 100, 2)

        # KDV
        kdv_matrahi = round(otv_matrahi + otv,2)
        kdv = round(kdv_matrahi * kdv_orani / 100, 2)

        vergi_toplami = round(otv + kdv, 2)

        # Turkiye Masrafi
        turkiye_masrafi = vergi_toplami + diger_bedeller + hizmet_bedeli
        toplam = round(satisfiyati + turkiye_masrafi,2)
        tplm_uz = len(str(toplam))

        clear()
        print(menu_title())
        print(f"\n{' Araç Bilgisi ':-^{tbl_gen_dis}}\n")
        print(f"{'Aracın Vergisiz Satış Bedeli':<{tbl_gen_ic}} : {satisfiyati:{tplm_uz}.2f}₺")
        print(f"{' Aracın Motor Tipi':<{tbl_gen_ic}} : Elektrikli")
        print(f"{'Aracın Motor Gücü':<{tbl_gen_ic}} : {motorgucu}kWh")
        print(f"{' Aracın Satın Alma Yılı':<{tbl_gen_ic}} :", yil_1)
        print(f"{' Aracın Türkiye Giriş Yılı':<{tbl_gen_ic}} :", yil_2)
        print(f"{'Aracın Yaşı':<{tbl_gen_ic}} :", aracyasi)
        print(f"{'Araca Uygulanacak Amortisman':<{tbl_gen_ic}} : {aracyasi + 1}. Kademe %{amrtsmn(aracyasi)} Amortisman")
        print(f"{'Amortisman Sonrası Araç Bedeli':<{tbl_gen_ic}} : {cif:{tplm_uz}.2f}₺")
        print(f"\n{' Vergiler ':-^{tbl_gen_dis}}\n")
        print(f"{'Navlun, Sigorta ve Sair Masraf Bedeli':<{tbl_gen_ic}} : {navlun_sigorta + sair_masraf:{tplm_uz}.2f}₺")
        print(f"{'Araca Uygulanacak ÖTV Bedeli ve Oranı':<{tbl_gen_ic}} : {otv:{tplm_uz}.2f}₺ (%{otv_orani})")
        print(f"{'Araca Uygulanacak KDV Bedeli ve Oranı':<{tbl_gen_ic}} : {kdv:{tplm_uz}.2f}₺ (%{kdv_orani})")
        print(f"{'':-^{tbl_gen_ic}}")
        print(f"{'Aracın ÖTV ve KDV Bedeli Toplamı':<{tbl_gen_ic}} : {vergi_toplami:{tplm_uz}.2f}₺")
        print(f"\n{'Ruhsat, TRT Bandrol, TÜV, vs Bedeli':<{tbl_gen_ic}} : {diger_bedeller:{tplm_uz}.2f}₺")
        print(f"{'Anahtar Teslim Hizmet Bedeli':<{tbl_gen_ic}} : {hizmet_bedeli:{tplm_uz}.2f}₺")
        print(f"{'':-^{tbl_gen_ic}}")
        print(f"{'Aracın Türkiyedeki Toplam Masrafı':<{tbl_gen_ic}} : {turkiye_masrafi:{tplm_uz}.2f}₺")
        print(f"\n{'':-^{tbl_gen_dis}}")
        print(f"\n{'Aracın Toplam Satınalma Maliyeti':<{tbl_gen_ic}} : {toplam:{tplm_uz}.2f}₺")
        print(f"\n{'':-^{tbl_gen_dis}}")
        if menu_alt() == "break": break


    # Hibrit Araç Vergisi Hesaplama
    elif inp_menu == "2" :
        clear()
        print(menu_title())
        print(f"\n Hibrit araç hesapla")
        yil_1 = arac_satin_alma_yili()
        yil_2 = arac_yurda_giris_yili()
        motorhacmi = arac_motorhacmi()
        motorgucu = arac_motorgucu()
        satisfiyati = arac_satisfiyati()

        if yil_2 >= yil_1 :
            aracyasi = yil_2 - yil_1
        else :
            print(f"\n{' !!!!! ':-^{tbl_gen_dis}}")
            print(f"\n{'Satın alma tarihi Yurda giriş tarihinden küçük olmamaz.':^{tbl_gen_dis}}")
            print(f"\n{'Lütfen girdiğiniz değerleri kontrol ediniz!':^{tbl_gen_dis}}")
            print(f"\n{'':=^{tbl_gen_dis}}\n")
            continue

        # Amortisman yuzdesi hesaplama
        amortisman_yuzdesi = amrtsmn(aracyasi) / 100
        
        # Vergiye Esas Bedel
        cif = round((satisfiyati * (100 - amrtsmn(aracyasi)) / 100) + navlun_sigorta,2)

        # OTV
        otv_matrahi = round(cif + sair_masraf,2)
        otv_orani = mtrgc_hbrt(motorgucu, motorhacmi, satisfiyati)
        otv = round(cif * otv_orani / 100, 2)

        # KDV
        kdv_matrahi = round(otv_matrahi + otv,2)
        kdv = round(kdv_matrahi * kdv_orani / 100, 2)

        vergi_toplami = round(otv + kdv, 2)

        # Turkiye Masrafi
        turkiye_masrafi = vergi_toplami + diger_bedeller + hizmet_bedeli
        toplam = round(satisfiyati + turkiye_masrafi,2)
        tplm_uz = len(str(toplam))

        clear()
        print(menu_title())
        print(f"\n{' Araç Bilgisi ':-^{tbl_gen_dis}}\n")
        print(f"{'Aracın Vergisiz Satış Bedeli':<{tbl_gen_ic}} : {satisfiyati:{tplm_uz}.2f}₺")
        print(f"{' Aracın Motor Tipi':<{tbl_gen_ic}} : Hibrit")
        print(f"{'Aracın Motor Hacmi':<{tbl_gen_ic}} : {motorhacmi}cc")
        print(f"{'Aracın Elektrik Motoru Gücü':<{tbl_gen_ic}} : {motorgucu}kWh")
        print(f"{' Aracın Satın Alma Yılı':<{tbl_gen_ic}} :", yil_1)
        print(f"{' Aracın Türkiye Giriş Yılı':<{tbl_gen_ic}} :", yil_2)
        print(f"{'Aracın Yaşı':<{tbl_gen_ic}} :", aracyasi)
        print(f"{'Araca Uygulanacak Amortisman':<{tbl_gen_ic}} : {aracyasi + 1}. Kademe %{amrtsmn(aracyasi)} Amortisman")
        print(f"{'Amortisman Sonrası Araç Bedeli':<{tbl_gen_ic}} : {cif:{tplm_uz}.2f}₺")
        print(f"\n{' Vergiler ':-^{tbl_gen_dis}}\n")
        print(f"{'Navlun, Sigorta ve Sair Masraf Bedeli':<{tbl_gen_ic}} : {navlun_sigorta + sair_masraf:{tplm_uz}.2f}₺")
        print(f"{'Araca Uygulanacak ÖTV Bedeli ve Oranı':<{tbl_gen_ic}} : {otv:{tplm_uz}.2f}₺ (%{otv_orani})")
        print(f"{'Araca Uygulanacak KDV Bedeli ve Oranı':<{tbl_gen_ic}} : {kdv:{tplm_uz}.2f}₺ (%{kdv_orani})")
        print(f"{'':-^{tbl_gen_ic}}")
        print(f"{'Aracın ÖTV ve KDV Bedeli Toplamı':<{tbl_gen_ic}} : {vergi_toplami:{tplm_uz}.2f}₺")
        print(f"\n{'Ruhsat, TRT Bandrol, TÜV, vs Bedeli':<{tbl_gen_ic}} : {diger_bedeller:{tplm_uz}.2f}₺")
        print(f"{'Anahtar Teslim Hizmet Bedeli':<{tbl_gen_ic}} : {hizmet_bedeli:{tplm_uz}.2f}₺")
        print(f"{'':-^{tbl_gen_ic}}")
        print(f"{'Aracın Türkiyedeki Toplam Masrafı':<{tbl_gen_ic}} : {turkiye_masrafi:{tplm_uz}.2f}₺")
        print(f"\n{'':-^{tbl_gen_dis}}")
        print(f"\n{'Aracın Toplam Satınalma Maliyeti':<{tbl_gen_ic}} : {toplam:{tplm_uz}.2f}₺")
        print(f"\n{'':-^{tbl_gen_dis}}")
        if menu_alt() == "break": break

    # Benzinli/Dizel Araç Vergisi Hesaplama
    elif inp_menu == "3" :
        clear()
        print(menu_title())
        print(f"\n Benzinli/Dizel araç hesapla")
        yil_1 = arac_satin_alma_yili()
        yil_2 = arac_yurda_giris_yili()
        motorhacmi = arac_motorhacmi()
        satisfiyati = arac_satisfiyati()

        if yil_2 >= yil_1 :
            aracyasi = yil_2 - yil_1
        else :
            print(f"\n{' !!!!! ':-^{tbl_gen_dis}}")
            print(f"\n{'Satın alma tarihi Yurda giriş tarihinden küçük olmamaz.':^{tbl_gen_dis}}")
            print(f"\n{'Lütfen girdiğiniz değerleri kontrol ediniz!':^{tbl_gen_dis}}")
            print(f"\n{'':=^{tbl_gen_dis}}\n")
            continue
        
        otv_orani = mtrgc_bnzn(motorhacmi, satisfiyati)
        amortisman_yuzdesi = amrtsmn(aracyasi) / 100
        
        # Vergiye Esas Bedel
        cif = round((satisfiyati * (100 - amrtsmn(aracyasi)) / 100) + navlun_sigorta,2)

        # OTV
        otv_matrahi = round(cif + sair_masraf,2)
        otv = round(cif * otv_orani / 100, 2)

        # KDV
        kdv_matrahi = round(otv_matrahi + otv,2)
        kdv = round(kdv_matrahi * kdv_orani / 100, 2)

        vergi_toplami = round(otv + kdv, 2)

        # Turkiye Masrafi
        turkiye_masrafi = vergi_toplami + diger_bedeller + hizmet_bedeli
        toplam = round(satisfiyati + turkiye_masrafi,2)
        tplm_uz = len(str(toplam))

        clear()
        print(menu_title())
        print(f"\n{' Araç Bilgisi ':-^{tbl_gen_dis}}\n")
        print(f"{' Aracın Vergisiz Satış Bedeli':<{tbl_gen_ic}} : {satisfiyati:{tplm_uz}.2f}₺")
        print(f"{' Aracın Motor Tipi':<{tbl_gen_ic}} : Benzinli")
        print(f"{' Aracın Motor Hacmi':<{tbl_gen_ic}} : {motorhacmi}cc")
        print(f"{' Aracın Satın Alma Yılı':<{tbl_gen_ic}} :", yil_1)
        print(f"{' Aracın Türkiye Giriş Yılı':<{tbl_gen_ic}} :", yil_2)
        print(f"{' Aracın Yaşı':<{tbl_gen_ic}} :", aracyasi)
        print(f"{' Araca Uygulanacak Amortisman':<{tbl_gen_ic}} : {aracyasi + 1}. Kademe %{amrtsmn(aracyasi)} Amortisman")
        print(f"{' Amortisman Sonrası Araç Bedeli':<{tbl_gen_ic}} : {cif:{tplm_uz}.2f}₺")
        print(f"\n{' Vergiler ':-^{tbl_gen_dis}}\n")
        print(f"{' Navlun, Sigorta ve Sair Masraf Bedeli':<{tbl_gen_ic}} : {navlun_sigorta + sair_masraf:{tplm_uz}.2f}₺")
        print(f"{' Araca Uygulanacak ÖTV Bedeli ve Oranı':<{tbl_gen_ic}} : {otv:{tplm_uz}.2f}₺ (%{otv_orani})")
        print(f"{' Araca Uygulanacak KDV Bedeli ve Oranı':<{tbl_gen_ic}} : {kdv:{tplm_uz}.2f}₺ (%{kdv_orani})")
        print(f"{'':-^{tbl_gen_ic}}")
        print(f"{' Aracın ÖTV ve KDV Bedeli Toplamı':<{tbl_gen_ic}} : {vergi_toplami:{tplm_uz}.2f}₺")
        print(f"\n{' Ruhsat, TRT Bandrol, TÜV, vs Bedeli':<{tbl_gen_ic}} : {diger_bedeller:{tplm_uz}.2f}₺")
        print(f"{' Anahtar Teslim Hizmet Bedeli':<{tbl_gen_ic}} : {hizmet_bedeli:{tplm_uz}.2f}₺")
        print(f"{'':-^{tbl_gen_ic}}")
        print(f"{' Aracın Türkiyedeki Toplam Masrafı':<{tbl_gen_ic}} : {turkiye_masrafi:{tplm_uz}.2f}₺")
        print(f"\n{'':-^{tbl_gen_dis}}")
        print(f"\n{' Aracın Toplam Satınalma Maliyeti':<{tbl_gen_ic}} : {toplam:{tplm_uz}.2f}₺")
        print(f"\n{'':-^{tbl_gen_dis}}")
        if menu_alt() == "break": break

    else :
        print(f"\n{' !!!!! ':-^{tbl_gen_dis}}\n")
        print("Lütfen seçenek numarasını doğru giriniz.")

    continue