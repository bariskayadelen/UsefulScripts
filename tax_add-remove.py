# Tax Remover and Adder Python Script

from unicodedata import numeric

while True :
    # Tablo Width
    tbl_gen_dis = 70
    tbl_gen_ic = 40
    print(f"\n{' Tax Adder and Remover Script ':=^{tbl_gen_dis}}")
    print("\nPlease choose your option:")
    inp_choice = input("\n[1] Add Tax\n[2] Remove Tax\n\n[3] Exit\n\nChoice: ")

    price = None
    
    try :
        if inp_choice == "1" :
            print(f"\n{' Tax Adder ':-^{tbl_gen_dis}}\n")
            # Tax Remover

            inp_price = input(f"{'Enter item price':<{tbl_gen_ic}} : ")
            try :
                if inp_price.isnumeric :
                    price = float(inp_price)
            except :
                print(f"\nError!!! {inp_price} is not numeric data. Please enter numerical value!")
                continue

            inp_rate = input(f"{'Enter tax rate %':<{tbl_gen_ic}} : ")
            try :
                rate = float(inp_rate)
            except :
                print(f"\nError!!! {inp_price} is not numeric data. Please enter numerical value!")
                continue

            tax = round(price * rate/100, 2)

            total = price + tax

            print(f"{'':-^{tbl_gen_ic}}")
            print(f"{'Price without tax:':<{tbl_gen_ic}} : {price:.2f}")
            print(f"{'Tax:':<{tbl_gen_ic}} : {tax:.2f} ({rate:.2f}%)")
            print(f"{'Price included tax:':<{tbl_gen_ic}} : {total:.2f}")


        elif inp_choice == "2" :
            print(f"\n{' Tax Remover ':-^{tbl_gen_dis}}\n")
            
            inp_price = input(f"{'Enter item price':<{tbl_gen_ic}} : ")
            try :
                if inp_price.isnumeric :
                    price = float(inp_price)
            except :
                print(f"\nError!!! {inp_price} is not numeric data. Please enter numerical value!")
                continue

            inp_rate = input(f"{'Enter tax rate %':<{tbl_gen_ic}} : ")
            try :
                rate = float(inp_rate)
            except :
                print(f"\nError!!! {inp_price} is not numeric data. Please enter numerical value!")
                continue

            item =  round((price * 100) / (100 + rate), 2)

            tax =  round((price - item),2)

            print(f"{'':-^{tbl_gen_ic}}")
            print(f"{'Price included tax:':<{tbl_gen_ic}} : {price:.2f}")
            print(f"{'Tax:':<{tbl_gen_ic}} : {tax:.2f} ({rate:.2f}%)")
            print(f"{'Price without tax:':<{tbl_gen_ic}} : {item:.2f}")
            

        elif inp_choice == "3" :
            print(f"\n{' Good bye ':=^{tbl_gen_dis}}\n")
            break
        else :
            print(f"\n{' !!!!! ':-^{tbl_gen_dis}}\n")
            print(f"!!! {inp_choice} is not an option. Please enter the correct option number.")
    except :
        print(f"\n{' !!!!! ':-^{tbl_gen_dis}}\n")
        print("!!! Please enter the correct option number.")

    continue
