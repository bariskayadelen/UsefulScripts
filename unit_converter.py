# Unit Converter

from unicodedata import numeric

# Definition Area
# Units: km²:Square kilometre, ha:Hectare, daa:Decare, a:Are, m²:Square metre, mm²:Square millimetre, mi²:Square mile, yd²:Square yard, ft²:Square foot, in²:Square inch, acre:Acre")
def menu_area(x):
    if x == 1 : return 'km²'
    elif x == 2 : return 'ha'
    elif x == 3 : return 'daa'
    elif x == 4 : return 'a'
    elif x == 5 : return 'm²'
    elif x == 6 : return 'mm²'
    elif x == 7 : return 'mi²'
    elif x == 8 : return 'yd²'
    elif x == 9 : return 'ft²'
    elif x == 10 : return 'in²'
    elif x == 11 : return 'acre'
    else : return 'Error!!!'

def convert_area(val, unit_in, unit_out):
    UL = {'km²':1000000.0, 'ha':10000.0, 'daa':1000.0, 'a':100.0, 'm²':1.0, 'mm²':0.000001, 'mi²':2589988.11, 'yd²':0.836127, 'ft²':0.092903, 'in²':0.0006451593, 'acre':4046.8564224}
    return val*UL[unit_in]/UL[unit_out]

# Definition Lenght
# km:Kilometre, m:Meter, cm:Centimeter, mm:Milimetre, μm:Micrometre, nm:Nanometre, mi:Mile, yd:Yard, ft:Foot, in:Inch
def menu_lenght(x):
    if x == 1 : return 'km'
    elif x == 2 : return 'm'
    elif x == 3 : return 'cm'
    elif x == 4 : return 'mm'
    elif x == 5 : return 'μm'
    elif x == 6 : return 'nm'
    elif x == 7 : return 'mi'
    elif x == 8 : return 'yd'
    elif x == 9 : return 'ft'
    elif x == 10 : return 'in'
    else : return 'Error!!!'
    # MN = {'1':'km', '2':'m', '3':'cm', '4':'mm', '5':'μm', '6':'nm', '7':'mi', '8':'yd', '9':'ft', '10':'in'}

def convert_lenght(val, unit_in, unit_out):
    UL = {'km':1000.0, 'm':1.0, 'cm':0.01, 'mm':0.001, 'μm':0.000001, 'nm':0.000000001, 'mi':1609.344, 'yd':0.9144, 'ft':0.3048, 'in':0.0254,}
    return val*UL[unit_in]/UL[unit_out]

# Definition Fuel Consumption
# L/100km:Liters per 100 km, mpg (US):Miles per gallon (US), mpg (Imp):Miles per gallon (Imp)
def menu_fuel(x):
    if x == 1 : return 'L/100km'
    elif x == 2 : return 'mpg(US)'
    elif x == 3 : return 'mpg(Imp)'
    else : return 'Error!!!'

def convert_fuel(val, unit_in, unit_out):
    if unit_in == unit_out:
        return val
    elif unit_in == 1 and unit_out == 2:
        y = (235.215 / val)
        return y
    elif unit_in == 1 and unit_out == 3:
        y = (282,481 / val)
        return y
    elif unit_in == 2 and unit_out == 1:
        y = (235.215 / val)
        return y
    elif unit_in == 2 and unit_out == 3:
        y = val * 1.20095
        return y
    elif unit_in == 3 and unit_out == 1:
        y = (235.215 / val)
        return y
    elif unit_in == 3 and unit_out == 2:
        y = (val / 1.20095)
        return y
    else :
        return 'Error!!! '    


# Definition Temperature
# °C:Celsius, °F:Fahrenheit, K:Kelvin, °R:Rankine
def menu_temperature(x):
    if x == 1 : return '°C'
    elif x == 2 : return '°F'
    elif x == 3 : return 'K'
    elif x == 4 : return '°R'
    else : return 'X'

def convert_temperature(val, unit_in, unit_out):
    if unit_in == unit_out:
        return val
    elif unit_in == 1 and unit_out == 2:
        y = (val * 9 / 5 ) + 32
        return y
    elif unit_in == 1 and unit_out == 3:
        y = (val + 273.15 )
        return y
    elif unit_in == 2 and unit_out == 1:
        y = (val - 32) * 5 / 9 
        return y
    elif unit_in == 2 and unit_out == 3:
        y = ((val - 32) * 5 / 9) + 273.15
        return y
    elif unit_in == 3 and unit_out == 1:
        y = (val - 273.15 )
        return y
    elif unit_in == 3 and unit_out == 2:
        y = ((val - 273.15 ) * 9 / 5) + 32
        return y
    else :
        return 'Error!!! '

# Table
tbl_len_out = 78
tbl_len_in = 38

while True :

    inp_choice = None
    inp_opt1 = None
    inp_opt2 = None

    print(f"\n{' Unit Converter ':=^{tbl_len_out}}")
    print(f"\nWhich category would you like to convert:")
    print(f"\n{' [1] Area ':{tbl_len_in}}  {' [4] Temperature ':{tbl_len_in}}")
    print(f"{' [2] Fuel Consumption ':{tbl_len_in}}  {' [5] Weight ':{tbl_len_in}}")
    print(f"{' [3] Length ':{tbl_len_in}}  {' [6] Volume  ':{tbl_len_in}}")
    inp_choice = input(f"\n{' [Q] Quit ':{tbl_len_in}}  {'  ':{tbl_len_in}} \n\nChoice: ")

    # Area Converter
    if inp_choice == "1" :
        print(f"\n{' Area Converter ':-^{tbl_len_out}}")
        print(f"\nUnits: [1]km², [2]ha, [3]daa, [4]a, [5]m², [6]mm², [7]mi², [8]yd², [9]ft², [10]in², [11]acre")

        inp_opt1 = input("\nChoose your input unit: ")
        try :
            opt1 = int(inp_opt1)
        except :
            print(f"\n{' !!!!! ':-^{tbl_len_out}}")
            print(f"\nError!!! {inp_opt1} is not numeric data. Please enter numerical value!")
            continue

        inp_opt2 = input("\nChoose your output unit: ")
        try :
            opt2 = int(inp_opt2)
        except :
            print(f"\n{' !!!!! ':-^{tbl_len_out}}")
            print(f"\nError!!! {inp_opt2} is not numeric data. Please enter numerical value!")
            continue

        inp_val = input("\nEnter your value: ")
        try :
            val = float(inp_val)
        except :
            print(f"\n{' !!!!! ':-^{tbl_len_out}}")
            print(f"\nError!!! {inp_val} is not numeric data. Please enter numerical value!")
            continue

        calc = round(convert_area(val, menu_area(opt1), menu_area(opt2)),4)
        print(f"\n{'':-^{tbl_len_out}}")
        print(f"\n{inp_val} {menu_area(opt1)} is equal to {calc} {menu_area(opt2)}")

    # Fuel Consumption Converter
    elif inp_choice == "2" :
        print(f"\n{' Fuel Consumption Converter ':-^{tbl_len_out}}") 
        print(f"\nUnits: [1] L/100km, [2] mpg(US) [3] mpg(Imp)")

        inp_opt1 = input("\nChoose your input unit: ")
        try :
            opt1 = int(inp_opt1)
        except :
            print(f"\n{' !!!!! ':-^{tbl_len_out}}")
            print(f"\nError!!! {inp_opt1} is not numeric data. Please enter numerical value!")
            continue

        inp_opt2 = input("\nChoose your output unit: ")
        try :
            opt2 = int(inp_opt2)
        except :
            print(f"\n{' !!!!! ':-^{tbl_len_out}}")
            print(f"\nError!!! {inp_opt2} is not numeric data. Please enter numerical value!")
            continue

        inp_val = input("\nEnter your value: ")
        try :
            val = float(inp_val)
        except :
            print(f"\n{' !!!!! ':-^{tbl_len_out}}")
            print(f"\nError!!! {inp_val} is not numeric data. Please enter numerical value!")
            continue

        calc = round(convert_fuel(val, opt1, opt2),2)
        print(f"\n{'':-^{tbl_len_out}}")
        print(f"\n{inp_val} {menu_fuel(opt1)} is equal to {calc} {menu_fuel(opt2)}")

    # Length Converter
    elif inp_choice == "3" :
        print(f"\n{' Length Converter ':-^{tbl_len_out}}")
        print(f"\nUnits: [1]km, [2]m, [3]cm, [4]mm, [5]μm, [6]nm, [7]mi, [8]yd, [9]ft, [10]in")

        inp_opt1 = input("\nChoose your input unit: ")
        try :
            opt1 = int(inp_opt1)
        except :
            print(f"\n{' !!!!! ':-^{tbl_len_out}}")
            print(f"\nError!!! {inp_opt1} is not numeric data. Please enter numerical value!")
            continue

        inp_opt2 = input("\nChoose your output unit: ")
        try :
            opt2 = int(inp_opt2)
        except :
            print(f"\n{' !!!!! ':-^{tbl_len_out}}")
            print(f"\nError!!! {inp_opt2} is not numeric data. Please enter numerical value!")
            continue

        inp_val = input("\nEnter your value: ")
        try :
            val = float(inp_val)
        except :
            print(f"\n{' !!!!! ':-^{tbl_len_out}}")
            print(f"\nError!!! {inp_val} is not numeric data. Please enter numerical value!")
            continue

        calc = convert_lenght(val, menu_lenght(opt1), menu_lenght(opt2))
        print(f"\n{'':-^{tbl_len_out}}")
        print(f"\n{inp_val} {menu_lenght(opt1)} is equal to {calc} {menu_lenght(opt2)}")

    # Temperature Converter
    elif inp_choice == "4" :
        print(f"\n{' Temperature Converter ':-^{tbl_len_out}}")
        print(f"\nUnits: [1] Celsius [2] Fahrenheit [3] Kelvin ")

        inp_opt1 = input("\nChoose your input unit: ")
        try :
            opt1 = int(inp_opt1)
        except :
            print(f"\n{' !!!!! ':-^{tbl_len_out}}")
            print(f"\nError!!! {inp_opt1} is not numeric data. Please enter numerical value!")
            continue

        inp_opt2 = input("\nChoose your output unit: ")
        try :
            opt2 = int(inp_opt2)
        except :
            print(f"\n{' !!!!! ':-^{tbl_len_out}}")
            print(f"\nError!!! {inp_opt2} is not numeric data. Please enter numerical value!")
            continue

        inp_val = input("\nEnter your value: ")
        try :
            val = float(inp_val)
        except :
            print(f"\n{' !!!!! ':-^{tbl_len_out}}")
            print(f"\nError!!! {inp_val} is not numeric data. Please enter numerical value!")
            continue

        calc = round(convert_temperature(val, opt1, opt2),2)
        print(f"\n{'':-^{tbl_len_out}}")
        print(f"\n{inp_val}{menu_temperature(opt1)} is equal to {calc}{menu_temperature(opt2)}")

    # Weight Converter
    elif inp_choice == "5" :
        print(f"\n{' Weight Converter ':-^{tbl_len_out}}") 

    # Volume Converter
    elif inp_choice == "6" :
        print(f"\n{' Volume Converter ':-^{tbl_len_out}}")

    # Program Exit
    elif inp_choice == "Q":
        print(f"\n{' Good Bye ':=^{tbl_len_out}}\n")
        break
    elif inp_choice == "q":
        print(f"\n{' Good Bye ':=^{tbl_len_out}}\n")
        break
    else :
        print(f"\n{' !!!!! ':-^{tbl_len_out}}\n")
        print("!!! Please enter the correct option number.")

    continue