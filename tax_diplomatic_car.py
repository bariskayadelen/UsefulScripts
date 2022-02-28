# Diplomatik aracın Türkiye'ye getirildiğinde ödeyeceği vergiyi hesaplayıcı program

from unicodedata import numeric

while True :

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

    # Elektrikli Motor gucunden OTV orani hesaplama
    def mtrgc_elktrk(a) :
        if a < 85 :
            b = 10
            return b
        elif 85 <= a < 120 :
            b = 25
            return b
        else :
            b = 60
            return b

    # Hibrit Motor gucunden OTV orani hesaplama
    def mtrgc_hbrt(a,b) :
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

    # Benzinli/Dizel Motor gucunden OTV orani hesaplama
    def mtrgc_bnzn(a,b) :
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
        
    def grd_kntrlt(a) :
        try :
            b = int(a)
            return b
        except :
            print(f"\n{' !!!!! ':-^{tbl_gen_dis}}")
            print(f"\nHata!!! {a} sayısal veri değildir. Lütfen sayısal veri giriniz!")
    
    def girdi_satin_alma_yili() :
        inp_satin_alma_yili = input("\nAraç satın alma yılını giriniz: ")
        try :
            satin_alma_yili = int(inp_satin_alma_yili)
        except :
            print(f"\n{' !!!!! ':-^{tbl_gen_dis}}")
            print(f"\nHata!!! {inp_satin_alma_yili} sayısal veri değildir. Lütfen sayısal veri giriniz!")

    def sonuc_yazdir(a,b) :
        print(f"\n{' Araç Bilgisi ':=^{a}}\n")
        print(f"{'Aracın Vergisiz Satış Bedeli':<{b}} : {satisfiyati:.2f}₺")
        print(f"{'Aracın Motor Hacmi':<{b}} : {motorgucu}cc")
        print(f"{'Aracın Motor Gücü':<{b}} : {motorgucu}kWh")
        print(f"{'Aracın Yaşı':<{b}} :", aracyasi)
        print(f"{'Araca Uygulanacak Amortisman':<{b}} : {aracyasi + 1}. Kademe %{amrtsmn(aracyasi)} Amortisman")
        print(f"{'Amortisman Sonrası Araç Bedeli':<{b}} : {cif:.2f}₺")
        print(f"\n{' Vergiler ':=^{a}}\n")
        print(f"{'Navlun, Sigorta ve Sair Masraf Bedeli':<{b}} : {navlun_sigorta + sair_masraf:{tplm_uz}.2f}₺")
        print(f"{'Araca Uygulanacak ÖTV Bedeli ve Oranı':<{b}} : {otv:{tplm_uz}.2f}₺ (%{otv_orani})")
        print(f"{'Araca Uygulanacak KDV Bedeli ve Oranı':<{b}} : {kdv:{tplm_uz}.2f}₺ (%{kdv_orani})")
        print(f"{'':-^{b}}")
        print(f"{'Aracın ÖTV ve KDV Bedeli Toplamı':<{b}} : {vergi_toplami:{tplm_uz}.2f}₺")
        print(f"\n{'Ruhsat, TRT Bandrol, TÜV, vs Bedeli':<{b}} : {diger_bedeller:{tplm_uz}.2f}₺")
        print(f"{'Anahtar Teslim Hizmet Bedeli':<{b}} : {hizmet_bedeli:{tplm_uz}.2f}₺")
        print(f"{'':-^{b}}")
        print(f"{'Aracın Türkiyedeki Toplam Masrafı':<{b}} : {turkiye_masrafi:{tplm_uz}.2f}₺")
        print(f"\n{'':=^{a}}")
        print(f"\n{'Aracın Toplam Satınalma Maliyeti':<{b}} : {toplam:{tplm_uz}.2f}₺")
        print(f"\n{'':=^{a}}\n")

    # KDV Orani
    kdv_orani = 18

    # Navlun ve Sigorta Bedeli 200 Euro
    navlun_sigorta = float(2076.56)
    
    # Sair Masraf Bedeli 150 Euro
    sair_masraf = float(1557.42)

    # Diger Bedeller Toplami 400 Euro
    diger_bedeller = float(4153.11)

    # Hizmet Bedeli 450 Euro
    hizmet_bedeli = float(4672.25)

    # Tablo Genisligi
    tbl_gen_dis = 70
    tbl_gen_ic = 40

    print(f"\n{' Diplomatik Araç Vergisi Hesaplama ':=^{tbl_gen_dis}}")
    print("\nHesaplama için aracın türünü giriniz:")
    inp_tercih = input("\n[1] Elektrikli araç vergisi hesapla\n[2] Hibrit araç vergisi hesapla\n[3] Benzinli/Dizel araç vergisi hesapla\n\n[9] Programdan çık\n\nTercih: ")

    try :
        # Elektrikli Araç vergisi Hesaplama
        if inp_tercih == "1" :
            print(f"\n{' Elektrikli Araç ':-^{tbl_gen_dis}}")

            inp_satin_alma_yili = input("\nAraç satın alma yılını giriniz: ")
#            grd_kntrlt(inp_satin_alma_yili)
            try :
                satin_alma_yili = int(inp_satin_alma_yili)
            except :
                print(f"\n{' !!!!! ':-^{tbl_gen_dis}}")
                print(f"\nHata!!! {inp_satin_alma_yili} sayısal veri değildir. Lütfen sayısal veri giriniz!")
                continue

            inp_yurda_giris_yili = input("\nAracın Türkiye\'ye giriş yılını giriniz: ")
            try :
                yurda_giris_yili = int(inp_yurda_giris_yili)
            except :
                print(f"\n{' !!!!! ':-^{tbl_gen_dis}}")
                print(f"\nHata!!! {inp_yurda_giris_yili} sayısal veri değildir. Lütfen sayısal veri giriniz!")
                continue

            inp_motorgucu = input("\nAracın motor gücünü kWh olarak giriniz: ")
            try :
                motorgucu = int(inp_motorgucu)
            except :
                print(f"\n{' !!!!! ':-^{tbl_gen_dis}}")
                print(f"\nHata!!! {inp_motorgucu} sayısal veri değildir. Lütfen sayısal veri giriniz!")
                continue

            inp_satisfiyati = input("\nAracın vergisiz satın alma bedelini ₺ olarak giriniz: ")
            try :
                satisfiyati = float(inp_satisfiyati)
            except :
                print(f"\n{' !!!!! ':-^{tbl_gen_dis}}")
                print(f"\nHata!!! {inp_satisfiyati} sayısal veri değildir. Lütfen sayısal veri giriniz!")
                continue

            aracyasi = yurda_giris_yili - satin_alma_yili
            otv_orani = mtrgc_elktrk(motorgucu)
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

            print(f"\n{' Araç Bilgisi ':=^{tbl_gen_dis}}\n")
            print(f"{'Aracın Vergisiz Satış Bedeli':<{tbl_gen_ic}} : {satisfiyati:.2f}₺")
            print(f"{'Aracın Motor Gücü':<{tbl_gen_ic}} : {motorgucu}kWh")
            print(f"{'Aracın Yaşı':<{tbl_gen_ic}} :", aracyasi)
            print(f"{'Araca Uygulanacak Amortisman':<{tbl_gen_ic}} : {aracyasi + 1}. Kademe %{amrtsmn(aracyasi)} Amortisman")
            print(f"{'Amortisman Sonrası Araç Bedeli':<{tbl_gen_ic}} : {cif:.2f}₺")
            print(f"\n{' Vergiler ':=^{tbl_gen_dis}}\n")
            print(f"{'Navlun, Sigorta ve Sair Masraf Bedeli':<{tbl_gen_ic}} : {navlun_sigorta + sair_masraf:{tplm_uz}.2f}₺")
            print(f"{'Araca Uygulanacak ÖTV Bedeli ve Oranı':<{tbl_gen_ic}} : {otv:{tplm_uz}.2f}₺ (%{otv_orani})")
            print(f"{'Araca Uygulanacak KDV Bedeli ve Oranı':<{tbl_gen_ic}} : {kdv:{tplm_uz}.2f}₺ (%{kdv_orani})")
            print(f"{'':-^{tbl_gen_ic}}")
            print(f"{'Aracın ÖTV ve KDV Bedeli Toplamı':<{tbl_gen_ic}} : {vergi_toplami:{tplm_uz}.2f}₺")
            print(f"\n{'Ruhsat, TRT Bandrol, TÜV, vs Bedeli':<{tbl_gen_ic}} : {diger_bedeller:{tplm_uz}.2f}₺")
            print(f"{'Anahtar Teslim Hizmet Bedeli':<{tbl_gen_ic}} : {hizmet_bedeli:{tplm_uz}.2f}₺")
            print(f"{'':-^{tbl_gen_ic}}")
            print(f"{'Aracın Türkiyedeki Toplam Masrafı':<{tbl_gen_ic}} : {turkiye_masrafi:{tplm_uz}.2f}₺")
            print(f"\n{'':=^{tbl_gen_dis}}")
            print(f"\n{'Aracın Toplam Satınalma Maliyeti':<{tbl_gen_ic}} : {toplam:{tplm_uz}.2f}₺")
            print(f"\n{'':=^{tbl_gen_dis}}\n")

        # Hibrit Araç Vergisi Hesaplama
        elif inp_tercih == "2" :
            print(f"\n{' Hibrit Araç ':-^{tbl_gen_dis}}")

            inp_satin_alma_yili = input("\nAraç satın alma yılını giriniz: ")
            grd_kntrlt(inp_satin_alma_yili)
            try :
                satin_alma_yili = int(inp_satin_alma_yili)
            except :
                print(f"\n{' !!!!! ':-^{tbl_gen_dis}}")
                print(f"\nHata!!! {inp_satin_alma_yili} sayısal veri değildir. Lütfen sayısal veri giriniz!")
                continue

            inp_yurda_giris_yili = input("\nAracın Türkiye\'ye giriş yılını giriniz: ")
            try :
                yurda_giris_yili = int(inp_yurda_giris_yili)
            except :
                print(f"\n{' !!!!! ':-^{tbl_gen_dis}}")
                print(f"\nHata!!! {inp_yurda_giris_yili} sayısal veri değildir. Lütfen sayısal veri giriniz!")
                continue

            inp_motorgucu = input("\nAracın motor hacmini cc olarak giriniz: ")
            try :
                motorgucu = int(inp_motorgucu)
            except :
                print(f"\n{' !!!!! ':-^{tbl_gen_dis}}")
                print(f"\nHata!!! {inp_motorgucu} sayısal veri değildir. Lütfen sayısal veri giriniz!")
                continue

            inp_satisfiyati = input("\nAracın vergisiz satın alma bedelini ₺ olarak giriniz: ")
            try :
                satisfiyati = float(inp_satisfiyati)
            except :
                print(f"\n{' !!!!! ':-^{tbl_gen_dis}}")
                print(f"\nHata!!! {inp_satisfiyati} sayısal veri değildir. Lütfen sayısal veri giriniz!")
                continue

            aracyasi = yurda_giris_yili - satin_alma_yili
            otv_orani = mtrgc_hbrt(motorgucu)
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

            print(f"\n{' Araç Bilgisi ':=^{tbl_gen_dis}}\n")
            print(f"{'Aracın Vergisiz Satış Bedeli':<{tbl_gen_ic}} : {satisfiyati:.2f}₺")
            print(f"{'Aracın Motor Hacmi':<{tbl_gen_ic}} : {motorgucu}cc")
            print(f"{'Aracın Yaşı':<{tbl_gen_ic}} :", aracyasi)
            print(f"{'Araca Uygulanacak Amortisman':<{tbl_gen_ic}} : {aracyasi + 1}. Kademe %{amrtsmn(aracyasi)} Amortisman")
            print(f"{'Amortisman Sonrası Araç Bedeli':<{tbl_gen_ic}} : {cif:.2f}₺")
            print(f"\n{' Vergiler ':=^{tbl_gen_dis}}\n")
            print(f"{'Navlun, Sigorta ve Sair Masraf Bedeli':<{tbl_gen_ic}} : {navlun_sigorta + sair_masraf:{tplm_uz}.2f}₺")
            print(f"{'Araca Uygulanacak ÖTV Bedeli ve Oranı':<{tbl_gen_ic}} : {otv:{tplm_uz}.2f}₺ (%{otv_orani})")
            print(f"{'Araca Uygulanacak KDV Bedeli ve Oranı':<{tbl_gen_ic}} : {kdv:{tplm_uz}.2f}₺ (%{kdv_orani})")
            print(f"{'':-^{tbl_gen_ic}}")
            print(f"{'Aracın ÖTV ve KDV Bedeli Toplamı':<{tbl_gen_ic}} : {vergi_toplami:{tplm_uz}.2f}₺")
            print(f"\n{'Ruhsat, TRT Bandrol, TÜV, vs Bedeli':<{tbl_gen_ic}} : {diger_bedeller:{tplm_uz}.2f}₺")
            print(f"{'Anahtar Teslim Hizmet Bedeli':<{tbl_gen_ic}} : {hizmet_bedeli:{tplm_uz}.2f}₺")
            print(f"{'':-^{tbl_gen_ic}}")
            print(f"{'Aracın Türkiyedeki Toplam Masrafı':<{tbl_gen_ic}} : {turkiye_masrafi:{tplm_uz}.2f}₺")
            print(f"\n{'':=^{tbl_gen_dis}}")
            print(f"\n{'Aracın Toplam Satınalma Maliyeti':<{tbl_gen_ic}} : {toplam:{tplm_uz}.2f}₺")
            print(f"\n{'':=^{tbl_gen_dis}}\n")

        # Benzinli/Dizel Araç Vergisi Hesaplama
        elif inp_tercih == "3" :
            print(f"\n{' Benzinli/Dizel Araç ':-^{tbl_gen_dis}}")
            inp_satin_alma_yili = input("\nAraç satın alma yılını giriniz: ")
#            grd_kntrlt(inp_satin_alma_yili)
            try :
                satin_alma_yili = int(inp_satin_alma_yili)
            except :
                print(f"\n{' !!!!! ':-^{tbl_gen_dis}}")
                print(f"\nHata!!! {inp_satin_alma_yili} sayısal veri değildir. Lütfen sayısal veri giriniz!")
                continue

            inp_yurda_giris_yili = input("\nAracın Türkiye\'ye giriş yılını giriniz: ")
            try :
                yurda_giris_yili = int(inp_yurda_giris_yili)
            except :
                print(f"\n{' !!!!! ':-^{tbl_gen_dis}}")
                print(f"\nHata!!! {inp_yurda_giris_yili} sayısal veri değildir. Lütfen sayısal veri giriniz!")
                continue

            inp_motorgucu = input("\nAracın motor hacmini cc olarak giriniz: ")
            try :
                motorgucu = int(inp_motorgucu)
            except :
                print(f"\n{' !!!!! ':-^{tbl_gen_dis}}")
                print(f"\nHata!!! {inp_motorgucu} sayısal veri değildir. Lütfen sayısal veri giriniz!")
                continue

            inp_satisfiyati = input("\nAracın vergisiz satın alma bedelini ₺ olarak giriniz: ")
            try :
                satisfiyati = float(inp_satisfiyati)
            except :
                print(f"\n{' !!!!! ':-^{tbl_gen_dis}}")
                print(f"\nHata!!! {inp_satisfiyati} sayısal veri değildir. Lütfen sayısal veri giriniz!")
                continue

            aracyasi = yurda_giris_yili - satin_alma_yili
            otv_orani = mtrgc_bnzn(motorgucu)
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

            print(f"\n{' Araç Bilgisi ':=^{tbl_gen_dis}}\n")
            print(f"{'Aracın Vergisiz Satış Bedeli':<{tbl_gen_ic}} : {satisfiyati:.2f}₺")
            print(f"{'Aracın Motor Hacmi':<{tbl_gen_ic}} : {motorgucu}cc")
            print(f"{'Aracın Yaşı':<{tbl_gen_ic}} :", aracyasi)
            print(f"{'Araca Uygulanacak Amortisman':<{tbl_gen_ic}} : {aracyasi + 1}. Kademe %{amrtsmn(aracyasi)} Amortisman")
            print(f"{'Amortisman Sonrası Araç Bedeli':<{tbl_gen_ic}} : {cif:.2f}₺")
            print(f"\n{' Vergiler ':=^{tbl_gen_dis}}\n")
            print(f"{'Navlun, Sigorta ve Sair Masraf Bedeli':<{tbl_gen_ic}} : {navlun_sigorta + sair_masraf:{tplm_uz}.2f}₺")
            print(f"{'Araca Uygulanacak ÖTV Bedeli ve Oranı':<{tbl_gen_ic}} : {otv:{tplm_uz}.2f}₺ (%{otv_orani})")
            print(f"{'Araca Uygulanacak KDV Bedeli ve Oranı':<{tbl_gen_ic}} : {kdv:{tplm_uz}.2f}₺ (%{kdv_orani})")
            print(f"{'':-^{tbl_gen_ic}}")
            print(f"{'Aracın ÖTV ve KDV Bedeli Toplamı':<{tbl_gen_ic}} : {vergi_toplami:{tplm_uz}.2f}₺")
            print(f"\n{'Ruhsat, TRT Bandrol, TÜV, vs Bedeli':<{tbl_gen_ic}} : {diger_bedeller:{tplm_uz}.2f}₺")
            print(f"{'Anahtar Teslim Hizmet Bedeli':<{tbl_gen_ic}} : {hizmet_bedeli:{tplm_uz}.2f}₺")
            print(f"{'':-^{tbl_gen_ic}}")
            print(f"{'Aracın Türkiyedeki Toplam Masrafı':<{tbl_gen_ic}} : {turkiye_masrafi:{tplm_uz}.2f}₺")
            print(f"\n{'':=^{tbl_gen_dis}}")
            print(f"\n{'Aracın Toplam Satınalma Maliyeti':<{tbl_gen_ic}} : {toplam:{tplm_uz}.2f}₺")
            print(f"\n{'':=^{tbl_gen_dis}}\n")

        # Programdan Çıkış
        elif inp_tercih == "9" :
            print(f"\n{' İyi Günler ':=^{tbl_gen_dis}}\n")
            break
        else :
            print(f"\n{' !!!!! ':-^{tbl_gen_dis}}\n")
            print("Lütfen seçenek numarasını doğru giriniz. 11")
    except :
        print(f"\n{' !!!!! ':-^{tbl_gen_dis}}\n")
        print("Lütfen seçenek numarasını doğru giriniz. 22")

    continue