# ELEKTRİK FATURASI VEYA TÜKETİMİ HESAPLAYICI PROGRAM
# Tüketim miktarından gelecek olan yaklaşık fatura miktarını veya
# Faturadan tüketim miktarını hesaplayabilirsiniz.

# 210kWh'a kadar elektrik tüketimi bedeli = 1.37 TL
# 210kWh'den sonra elektrik tüketimi bedeli = 2.055 TL

from unicodedata import numeric

tarif = 1.37
limit = 210

while True :
    # Tablo genişliği
    tbl_gen_dis = 70
    tbl_gen_ic = 40
    print(f"\n{' Fatura veya Tüketim Hesaplayıcı ':=^{tbl_gen_dis}}")
    print("\nLütfen yapmak istediğiniz işlemi numarasını giriniz:")
    inp_tercih = input("\n[1] Tüketimden fatura hesapla\n[2] Faturadan tüketim hesapla\n[3] Programdan çık\n\nTercih: ")
    try :
        if inp_tercih == "1" :
            print(f"\n{' Tüketimden Fatura Hesaplama ':-^{tbl_gen_dis}}")

            # Tüketim fonksiyonu
            tuketim = None
            def ftr(a,b) :
                if a <= limit :
                    c = a * b
                    return c
                else :
                    c = (limit * b) + ((a - limit) * b * 1.5)
                    return c 
            inp_ilk = input('\nLütfen ilk sayaç verisini giriniz: ')
            try :
                if inp_ilk.isnumeric :
                    ilk = float(inp_ilk)
            except :
                print(f"\nHata!!! {inp_ilk} sayısal veri değildir. Lütfen sayısal veri giriniz!")
                continue
            
            inp_son = input('\nLütfen son sayaç verisini giriniz: ')
            try :
                if inp_son.isnumeric :
                    son = float(inp_son)
            except :
                print(f"\n{' !!!!! ':-^{tbl_gen_dis}}")
                print(f"\nHata!!! {inp_son} sayısal veri değildir. Lütfen sayısal veri giriniz!")
                continue
            
            tuketim = son - ilk
            fatura =  round(ftr(tuketim,tarif),2)

            if tuketim >= 0 :
                print(f"\nTüketim miktarınız {tuketim} kWh ve yaklaşık faturanız {fatura}₺'dir.\n")
            else :
                print(f"\n{' !!!!! ':-^{tbl_gen_dis}}")
                print(f"\nHata!!! Son sayaç verisi ilk sayaç verisinden küçük olamaz. Girilen değerleri kontrol ederek yeniden giriniz!")

        elif inp_tercih == "2" :
            print(f"\n{' Faturadan Tüketim Hesaplama ':-^{tbl_gen_dis}}")
            
            tuketim = None

            # Fatura fonksiyonu
            def tktm(a) :
                if a < (tarif * limit) :
                    a = a / 1.37
                    return a
                else :
                    b = limit + ((a - (tarif * limit)) / (tarif * 1.5))
                return b

            inp_ftr = input('\nLütfen faturanızı giriniz: ')
            try :
                if inp_ftr.isnumeric :
                    ftr = float(inp_ftr)
                    tuketim = round(tktm(ftr))
                    print(f"\nTüketim miktarınız {tuketim} kWh'dir.")
            except :                
                print(f"\n{' !!!!! ':-^{tbl_gen_dis}}")
                print(f"\nHata!!! {inp_ftr} sayısal veri değildir. Lütfen sayısal veri giriniz!")

        elif inp_tercih == "3" :
            print(f"\n{' İyi Günler ':=^{tbl_gen_dis}}\n")
            break
        else :
            print(f"\n{' !!!!! ':-^{tbl_gen_dis}}\n")
            print("!!! Lütfen seçenek numarasını doğru giriniz.")
    except :
        print(f"\n{' !!!!! ':-^{tbl_gen_dis}}\n")
        print("!!! Lütfen seçenek numarasını doğru giriniz.")

    continue