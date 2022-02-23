# Ithal Elektrikli Arac Vergi ve Toplam Maliyetini Hesaplama

while True :

# Motor gucunden OTV orani hesaplama    
    def mtrgc(a) :
        if a < 85 :
            b = 10
            return b
        elif 85 <= a < 120 :
            b = 25
            return b
        else :
            b = 60
            return b

# Arac Yasindan Amortisman Hesaplama
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

    inp_satin_alma_yili = input('\nAraç satın alma yılını giriniz: ')
    try :
        satin_alma_yili = int(inp_satin_alma_yili)
    except :
        print('\n!!! Lütfen sayısal değer giriniz!\n')
        quit()
    
    inp_yurda_giris_yili = input('\nAracın Türkiye\'ye giriş yılını giriniz: ')
    try :
        yurda_giris_yili = int(inp_yurda_giris_yili)
    except :
        print('\n!!! Lütfen sayısal değer giriniz!\n')
        quit()

    inp_motorgucu = input('\nAracın motor gücünü kWh olarak giriniz: ')
    try :
        motorgucu = int(inp_motorgucu)
    except :
        print('\n!!! Lütfen sayısal değer giriniz!\n')
        quit()

    inp_satisfiyati = input('\nAracın vergisiz satın alma bedelini TL olarak giriniz: ')
    try :
        satisfiyati = float(inp_satisfiyati)
    except :
        print('\n!!! Lütfen sayısal değer giriniz!\n')
        quit()
    
    aracyasi = yurda_giris_yili - satin_alma_yili
    otv_orani = mtrgc(motorgucu)
    kdv_orani = float(18)

    # Navlun ve Sigorta Bedeli 200 Euro
    navlun_sigorta = float(2076.56)
    # Sair Masraf Bedeli 150 Euro
    sair_masraf = float(1557.42)
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

    # Diger Bedeller Toplami 400 Euro
    diger_bedeller = float(4153.11)
    # Hizmet Bedeli 450 Euro
    hizmet_bedeli = float(4672.25)

    # Turkiye Masrafi
    turkiye_masrafi = vergi_toplami + diger_bedeller + hizmet_bedeli 
    toplam = round(satisfiyati + turkiye_masrafi,2)
    tplm_uz = len(str(toplam))

    print("\n============ Araç Bilgisi =============")
    print(f"Aracın Vergisiz Satış Bedeli          : {satisfiyati:.2f}₺")
    print(f"Aracın Motor Gücü                     : {motorgucu}kWh")
    print(f"Aracın Yaşı                           :", aracyasi)
    print(f"Araca Uygulanacak Amortisman          : {aracyasi + 1}. Kademe %{amrtsmn(aracyasi)} Amortisman")
    print(f"Amortisman Sonrası Araç Bedeli        : {cif:.2f}₺")
    print(f'\n============== Vergiler ==============')
    print(f"Navlun, Sigorta ve Sair Masraf Bedeli : {navlun_sigorta + sair_masraf:{tplm_uz}.2f}₺")
    print(f"Araca Uygulanacak ÖTV Bedeli ve Oranı : {otv:{tplm_uz}.2f}₺ (%{otv_orani})")
    print(f"Araca Uygulanacak KDV Bedeli ve Oranı : {kdv:{tplm_uz}.2f}₺ (%{kdv_orani})")
    print("--------------------------------------")
    print(f"Aracın ÖTV ve KDV Bedeli Toplamı      : {vergi_toplami:{tplm_uz}.2f}₺")
    print(f"\nRuhsat, TRT Bandrol, TÜV, vs Bedeli   : {diger_bedeller:{tplm_uz}.2f}₺")
    print(f"Anahtar Teslim Hizmet Bedeli          : {hizmet_bedeli:{tplm_uz}.2f}₺")
    print("--------------------------------------")
    print(f"Aracın Türkiye\'deki Toplam Masrafı    : {turkiye_masrafi:{tplm_uz}.2f}₺")
    print("======================================")
    print(f"\nAracın Toplam Satınalma Maliyeti      : {toplam:{tplm_uz}.2f}₺")
    print("\n======================================\n")
    quit()
