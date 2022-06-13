# Tax Remover and Adder Python Script

from unicodedata import numeric
from os import system, name

# Define clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def menu_main():
    print(f"\n{' Project Devrim DB Manager ':=^{tbl_len_out}}")
    print(f"\nLütfen yapmak istediğiniz işlemi aşağıdaki menüden seçiniz:\n")
    print(f" [1] Araç tüketim bilgisi hesapla")
    print(f" [2] Tüm araçların bilgisini göster")
    print(f" [3] Akaryakıt fiyat bilgisini göster")
    print(f" [41] Elektrik fiyat bilgisini göster")
    print(f" [42] Elektrik fiyat bilgisini güncelle")
    print(f" [43] Elektrik fiyat bilgisini sil")

# Table dimentions
tbl_len_out = 78
tbl_len_in = 38

while True:
    # clear()
    print(f"\n{' Tax Adder and Remover Script ':=^{tbl_len_out}}")
    print("\nPlease choose your option:")
    inp_choice = input("\n[1] Add Tax\n[2] Remove Tax\n\n[3] Exit\n\nChoice: ")

    price = None
    
    if inp_choice == "3":
        print(f"\n{' Good bye ':=^{tbl_len_out}}\n")
        break
    
    elif inp_choice == "1":
        clear()
        print(f"\n{' Tax Adder ':=^{tbl_len_out}}\n")
        # Tax Remover

        inp_price = input(f"{'Enter item price':<{tbl_len_in}} : ")
        try :
            if inp_price.isnumeric :
                price = float(inp_price)
        except :
            print(f"\nError!!! {inp_price} is not numeric data. Please enter numerical value!")
            continue

        inp_rate = input(f"{'Enter tax rate %':<{tbl_len_in}} : ")
        try :
            rate = float(inp_rate)
        except :
            print(f"\nError!!! {inp_price} is not numeric data. Please enter numerical value!")
            continue

        tax = round(price * rate/100, 2)

        total = price + tax

        print(f"{'':-^{tbl_len_in}}")
        print(f"{'Price without tax:':<{tbl_len_in}} : {price:.2f}")
        print(f"{'Tax:':<{tbl_len_in}} : {tax:.2f} ({rate:.2f}%)")
        print(f"{'Price included tax:':<{tbl_len_in}} : {total:.2f}")


    elif inp_choice == "2" :
        clear()
        print(f"\n{' Tax Remover ':=^{tbl_len_out}}\n")
        
        inp_price = input(f"{'Enter item price':<{tbl_len_in}} : ")
        try :
            if inp_price.isnumeric :
                price = float(inp_price)
        except :
            print(f"\nError!!! {inp_price} is not numeric data. Please enter numerical value!")
            continue

        inp_rate = input(f"{'Enter tax rate %':<{tbl_len_in}} : ")
        try :
            rate = float(inp_rate)
        except :
            print(f"\nError!!! {inp_price} is not numeric data. Please enter numerical value!")
            continue

        item =  round((price * 100) / (100 + rate), 2)

        tax =  round((price - item),2)

        print(f"{'':-^{tbl_len_in}}")
        print(f"{'Price included tax:':<{tbl_len_in}} : {price:.2f}")
        print(f"{'Tax:':<{tbl_len_in}} : {tax:.2f} ({rate:.2f}%)")
        print(f"{'Price without tax:':<{tbl_len_in}} : {item:.2f}")
        
    else:
        print(f"\n{' !!!!! ':-^{tbl_len_out}}\n")
        print(f"!!! {inp_choice} is not an option. Please enter the correct option number.")

    # continue
