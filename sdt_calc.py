# Hız/Mesafe/Zaman Hesaplama Programı
from os import system, name
# from time import sleep

# Define clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def f_time(dist,speed):
    if (dist / speed) < 1:
        minute = round((dist/speed) * 60)
        return (f"{dist} km yolu {speed} km/h hızla {minute} dakikada gidersiniz.")
    elif (dist % speed) == 0 and (dist / speed) < 24:
        hour = int(dist / speed)
        return (f"{dist} km yolu {speed} km/h hızla {hour} saatte gidersiniz.")
    elif (dist % speed) == 0 and (dist / speed) >= 24:
        day = int(int(dist / speed) / 24)
        hour = (int(dist / speed) - (day*24))
        return (f"{dist} km yolu {speed} km/h hızla {day} gün {hour} saatte gidersiniz.")
    elif (dist / speed) >= 24:
        day = int(int(dist / speed) / 24)
        hour = (int(dist / speed) - (day*24))
        minute = round(((dist / speed) - (day*24) - hour) * 60)
        return (f"{dist} km yolu {speed} km/h hızla {day} gün {hour} saat {minute} dakikada gidersiniz.")
    else:
        hour = int(dist / speed)
        minute = round(((dist / speed)-hour) * 60)
        return (f"{dist} km yolu {speed} km/h hızla {hour} saat {minute} dakikada gidersiniz.")

def f_speed(dist,hour,minute):
    total_time = hour + (minute/60)
    speed = round(dist / total_time, 2)
    return (f"{dist} km yolu {hour} saat {minute} dakikada gidersiniz hiziniz {speed} km/h'dir.")

def f_distance(speed,hour,minute):
    total_time = hour + (minute/60)
    dist = speed * total_time
    return (f"{speed} km/h hızla {hour} saat {minute} dakikada {dist} km yol gidersiniz.")

def menu_bottom():
    while True:
        inp = input(f"\n [A] Ana menüye dön | [Q] Programdan Çık | Tercih: ")
        if inp.lower() == "q":
            print(f"\n{' İyi Günler ':=^{tbl_len_out}}\n")
            return "break"
        elif inp.lower() == "a":
            return "continue"
        else:
            clear()
            print(f"\n{' Hız/Mesafe/Zaman Hesaplama Programı ':=^{tbl_len_out}}")
            # print(f"\n{'':-^{tbl_len_out}}")
            print(f"\n Hata!!! Girmiş olduğunuz '{inp}' değeri menüde mevcut değildir.")
            print(f"\n Lütfen menü seçeneğini doğru giriniz!")
        continue

def check_speed(inp):
    while True:
        try:
            result = float(inp)
            return result
        except:
            clear()
            print(f"\n{' Hız/Mesafe/Zaman Hesaplama Programı ':=^{tbl_len_out}}")
            print(f"\n Hata!!! Girmiş olduğunuz '{inp}' değeri sayisal bir değer değildir.")
            print("\n Lütfen sayısal bir değer giriniz.")
            inp = input(f"\n{' Ortalama hızınızı km/h olarak giriniz':{tbl_len_in}}: ") 
            continue

def check_time(inp):
    while True:
        try:
            hour = int(inp.rsplit(':')[0])
            minute = int(inp.rsplit(':')[1])
            return hour, minute
        except:
            clear()
            print(f"\n{' Hız/Mesafe/Zaman Hesaplama Programı ':=^{tbl_len_out}}")
            print(f"\n Hata!!! Girmiş olduğunuz '{inp}' değeri bir zaman değeri değildir.")
            print("\n Lütfen sizden istendiği şekilde bir değer giriniz.")
            inp = input(f"\n{' Zamanı saat:dakika olarak giriniz':{tbl_len_in}}: ")
            continue
        
def check_dist(inp):
    while True:
        try:
            result = float(inp)
            return result
        except:
            clear()
            print(f"\n{' Hız/Mesafe/Zaman Hesaplama Programı ':=^{tbl_len_out}}")
            print(f"\n Hata!!! Girmiş olduğunuz '{inp}' değeri sayisal bir değer değildir.")
            print("\n Lütfen sayısal bir değer giriniz.")
            inp = input(f"\n{' Mesafeyi km olarak giriniz':{tbl_len_in}}: ") 
            continue

tbl_len_out = 78
tbl_len_in = 40

while True:
    clear()
    print(f"\n{' Hız/Mesafe/Zaman Hesaplama Programı ':=^{tbl_len_out}}")
    print(f"\n Lütfen yapmak istediğiniz işlemi menüden seçiniz.")
    print(f"\n [1] Hız Hesapla ")
    print(f" [2] Mesafe Hesapla")
    print(f" [3] Zaman Hesapla")
    print(f"\n [Q] Programdan Çık")
    inp_choice = input("\nTercih : ")

    if inp_choice.lower() == "q":
        print(f"\n{' İyi Günler ':=^{tbl_len_out}}\n")
        break

    # Speed Calc
    elif inp_choice == "1":
        clear()
        print(f"\n{' Hız/Mesafe/Zaman Hesaplama Programı ':=^{tbl_len_out}}")
        mesafe = check_dist(input(f"\n{' Mesafeyi km olarak giriniz':{tbl_len_in}}: ") )
        zaman = check_time(input(f"\n{' Zamanı saat:dakika olarak giriniz':{tbl_len_in}}: "))
        clear()
        print(f"\n{' Hız/Mesafe/Zaman Hesaplama Programı ':=^{tbl_len_out}}")
        print("\n",f_speed(mesafe,zaman[0],zaman[1]))
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    # Distance Calc
    elif inp_choice == "2":
        clear()
        print(f"\n{' Hız/Mesafe/Zaman Hesaplama Programı ':=^{tbl_len_out}}")
        hiz = check_speed(input(f"\n{' Ortalama hızınızı km/h olarak giriniz':{tbl_len_in}}: "))
        zaman = check_time(input(f"\n{' Zamanı saat:dakika olarak giriniz':{tbl_len_in}}: "))
        clear()
        print(f"\n{' Hız/Mesafe/Zaman Hesaplama Programı ':=^{tbl_len_out}}")
        print("\n",f_distance(hiz,zaman[0],zaman[1]))
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    # Time Calc
    elif inp_choice == "3":
        clear()
        print(f"\n{' Hız/Mesafe/Zaman Hesaplama Programı ':=^{tbl_len_out}}")
        hiz = check_speed(input(f"\n{' Ortalama hızınızı km/h olarak giriniz':{tbl_len_in}}: "))
        mesafe = check_dist(input(f"\n{' Mesafeyi km olarak giriniz':{tbl_len_in}}: "))
        clear()
        print(f"\n{' Hız/Mesafe/Zaman Hesaplama Programı ':=^{tbl_len_out}}")
        print("\n",f_time(mesafe,hiz))
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    else:
        clear()
        print(f"\n{' Hız/Mesafe/Zaman Hesaplama Programı ':=^{tbl_len_out}}")
        print(f"\n Hata!!! Girmiş olduğunuz {inp_choice} değeri menüde mevcut değildir.")
        print(f"\n Lütfen menü seçeneğini doğru giriniz!")
        if menu_bottom() == "break": break
    continue
