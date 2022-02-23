# Ithal Elektrikli Arac Vergi ve Toplam Maliyetini Hesaplama

while True :

# Motor gucunden OTV orani hesaplama    
    def mtrgc(a,b) :
        if a < 1600 and b < 92000 :
            c = 45
            return c
        elif a < 1600 and 92000 <= b < 150000 :
            c = 50
            return c
        elif a < 1600 and 150000 <= b :
            c = 80
            return c
        elif 1600 <= a < 2000 and b < 170000 :
            c = 130
            return c
        elif 1600 <= a < 2000 and 170000 <= b :
            c = 150
            return c
        else :
            c = 220
            return c

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

    tbl_gen_dis = 70
    tbl_gen_1 = 40
    print(f"\n{' İthal Araç Vergisi Hesaplama ':=^{tbl_gen_dis}}")
    print("\nLütfen yapmak istediğiniz işlemi numarasını giriniz:")
    inp_ilksorgu = input("\n[1] Yeni araç vergisi hesapla\n[2] Programdan Çık\n\nTercih: ")
    try :
        if inp_ilksorgu == "1" :
            print(f"\n{' Araç Bilgi Girişi ':-^{tbl_gen_dis}}")
        elif inp_ilksorgu == "2" :
            print(f"\n{' İyi günler. ':=^{tbl_gen_dis}}\n")
            break
        elif inp_ilksorgu == "666" :
            print(f"\n{' You touch my Tralala. My ding ding DONG!!! ':=^{tbl_gen_dis}}\n")
            break
        else :
            print(f"\n{' !!!!! ':-^{tbl_gen_dis}}\n")
            print("!!! Lütfen seçenek numarasını doğru giriniz.")
            continue
    except :
        print('Lütfen bir seçenek numarasını doğru giriniz.\n') 
        continue

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

    inp_motorgucu = input('\nAracın motor hacmini cc olarak giriniz: ')
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
    otv_orani = mtrgc(motorgucu,satisfiyati)
    kdv_orani = 18

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


    print(f"\n{' Araç Bilgisi ':=^{tbl_gen_dis}}\n")
    print(f"{'Aracın Vergisiz Satış Bedeli':<{tbl_gen_1}} : {satisfiyati:.2f}₺")
    print(f"{'Aracın Motor Hacmi':<{tbl_gen_1}} : {motorgucu}cc")
    print(f"{'Aracın Yaşı':<{tbl_gen_1}} :", aracyasi)
    print(f"{'Araca Uygulanacak Amortisman':<{tbl_gen_1}} : {aracyasi + 1}. Kademe %{amrtsmn(aracyasi)} Amortisman")
    print(f"{'Amortisman Sonrası Araç Bedeli':<{tbl_gen_1}} : {cif:.2f}₺")
    print(f"\n{' Vergiler ':=^{tbl_gen_dis}}\n")
    print(f"{'Navlun, Sigorta ve Sair Masraf Bedeli':<{tbl_gen_1}} : {navlun_sigorta + sair_masraf:{tplm_uz}.2f}₺")
    print(f"{'Araca Uygulanacak ÖTV Bedeli ve Oranı':<{tbl_gen_1}} : {otv:{tplm_uz}.2f}₺ (%{otv_orani})")
    print(f"{'Araca Uygulanacak KDV Bedeli ve Oranı':<{tbl_gen_1}} : {kdv:{tplm_uz}.2f}₺ (%{kdv_orani})")
    print(f"{'':-^{tbl_gen_1}}")
    print(f"{'Aracın ÖTV ve KDV Bedeli Toplamı':<{tbl_gen_1}} : {vergi_toplami:{tplm_uz}.2f}₺")
    print(f"\n{'Ruhsat, TRT Bandrol, TÜV, vs Bedeli':<{tbl_gen_1}} : {diger_bedeller:{tplm_uz}.2f}₺")
    print(f"{'Anahtar Teslim Hizmet Bedeli':<{tbl_gen_1}} : {hizmet_bedeli:{tplm_uz}.2f}₺")
    print(f"{'':-^{tbl_gen_1}}")
    print(f"{'Aracın Türkiyedeki Toplam Masrafı':<{tbl_gen_1}} : {turkiye_masrafi:{tplm_uz}.2f}₺")
    print(f"\n{'':=^{tbl_gen_dis}}")
    print(f"\n{'Aracın Toplam Satınalma Maliyeti':<{tbl_gen_1}} : {toplam:{tplm_uz}.2f}₺")
    print(f"\n{'':=^{tbl_gen_dis}}\n")
    continue
