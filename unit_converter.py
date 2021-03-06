# Unit Converter

from unicodedata import numeric

# Definition Main Menu
#list_title = {1:Area}
list_menu = {
    1:'Area', 
    2:'Fuel Consumption', 
    3:'Length', 
    4:'Temperature', 
    5:'Weight', 
    6:'Volume'}
def menu_main(unit):
    return list_menu[unit]

# Definition Area
# Units: km²:Square kilometre, ha:Hectare, daa:Decare, a:Are, m²:Square metre, mm²:Square millimetre, mi²:Square mile, yd²:Square yard, ft²:Square foot, in²:Square inch, acre:Acre")
list_area = {
    1:'km²', 
    2:'ha', 
    3:'daa', 
    4:'a', 
    5:'m²', 
    6:'mm²', 
    7:'mi²', 
    8:'yd²', 
    9:'ft²', 
    10:'in²', 
    11:'acre'}
def menu_area(unit):
    return list_area[unit]

def convert_area(val, unit_in, unit_out):
    UL = {
        'km²':1000000.0, 
        'ha':10000.0, 
        'daa':1000.0, 
        'a':100.0, 
        'm²':1.0, 
        'mm²':0.000001, 
        'mi²':2589988.11, 
        'yd²':0.836127, 
        'ft²':0.092903, 
        'in²':0.0006451593, 
        'acre':4046.8564224}
    return val*UL[unit_in]/UL[unit_out]

# Definition Fuel Consumption
# Units: L/100km:Liters per 100 km, mpg(US):Miles per gallon (US), mpg(Imp):Miles per gallon (Imp)
list_fuel = {
    1:'L/100km', 
    2:'mpg(US)', 
    3:'mpg(Imp)'}
def menu_fuel(unit):
    return list_fuel[unit]

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

# Definition Lenght
# Units: km:Kilometre, m:Meter, cm:Centimeter, mm:Milimetre, μm:Micrometre, nm:Nanometre, mi:Mile, yd:Yard, ft:Foot, in:Inch
list_lenght = {
    1:'km', 
    2:'m', 
    3:'cm', 
    4:'mm', 
    5:'μm', 
    6:'nm', 
    7:'mi', 
    8:'yd', 
    9:'ft', 
    10:'in'}
def menu_lenght(unit):
    return list_lenght[unit]

def convert_lenght(val, unit_in, unit_out):
    UL = {
        'km':1000.0, 
        'm':1.0, 
        'cm':0.01, 
        'mm':0.001, 
        'μm':0.000001, 
        'nm':0.000000001, 
        'mi':1609.344, 
        'yd':0.9144, 
        'ft':0.3048, 
        'in':0.0254,}
    return val*UL[unit_in]/UL[unit_out]

# Definition Temperature
# Units: °C:Celsius, °F:Fahrenheit, K:Kelvin, °R:Rankine
list_temperature = {
    1:'°C', 
    2:'°F', 
    3:'K', 
    4:'°R'}
def menu_temperature(unit):
    return list_temperature[unit]

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

# Definition Weight
# Units t:Ton, kg:Kilogram, g:Gram, mg:Milligram, µg:Microgram, t(imp):Ton(imperial), t(US):Ton(US), st:Stone, lb:Pound, oz:Ounce
list_weight = {
    1:'T', 
    2:'kg', 
    3:'g', 
    4:'mg', 
    5:'µg', 
    6:'t(imp)', 
    7:'t(US)', 
    8:'st', 
    9:'lb', 
    10:'oz'}
def menu_weight(unit):
    return list_weight[unit]

def convert_weight(val, unit_in, unit_out):
    UL = {
        'T':1000000.0, 
        'kg':1000.0, 
        'g':1.0, 
        'mg':0.001, 
        'µg':0.000001, 
        't(imp)':0.9463529460, 
        't(US)':1.13652, 
        'st':0.473176, 
        'lb':0.568261, 
        'oz':28.3168}
    return val*UL[unit_in]/UL[unit_out]

# Definition Volume
# Units m³:Cubic meter, L:Litre, mL:Millilitre, gal(US): US gallon, gal(imp):Imperial gallon, qt(US):US quart, qt(imp):Imperial quart, pt(US):US pint, pt(imp):Imperial pint, ft³:Cubic Foot, in³:Cubic inch
list_volume = {
    1:'m³', 
    2:'L', 
    3:'mL', 
    4:'gal(US)', 
    5:'gal(imp)', 
    6:'qt(US)', 
    7:'qt(imp)', 
    8:'pt(US)', 
    9:'pt(imp)', 
    10:'ft³', 
    11:'in³'}
def menu_volume(unit):
    return list_volume[unit]

def convert_volume(val, unit_in, unit_out):
    UL = {
        'm³':1000.0, 
        'L':1.0, 'mL':0.001, 
        'gal(US)':3.785411784, 
        'gal(imp)':4.54609, 
        'qt(US)':0.9463529460, 
        'qt(imp)':1.13652, 
        'pt(US)':0.473176, 
        'pt(imp)':0.568261, 
        'ft³':28.3168, 
        'in³':0.0163871}
    return val*UL[unit_in]/UL[unit_out]

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

    if inp_choice == "1" :
        print(f"\n{' Area Converter ':-^{tbl_len_out}}")
        print(f"\nUnits: [1]km², [2]ha, [3]daa, [4]a, [5]m², [6]mm², [7]mi², [8]yd², [9]ft², [10]in², [11]acre")
        # print(f"\nUnits: {list_area.keys}")

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
        print(f"\nUnits: [1]t, [2]kg, [3]g, [4]mg, [5]µg, [6]t(imp), [7]t(US), [8]st, [9]lb, [10]oz")

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

        calc = round(convert_weight(val, menu_weight(opt1), menu_weight(opt2)),4)
        print(f"\n{'':-^{tbl_len_out}}")
        print(f"\n{inp_val} {menu_weight(opt1)} is equal to {calc} {menu_weight(opt2)}")

    # Volume Converter
    elif inp_choice == "6" :
        print(f"\n{' Volume Converter ':-^{tbl_len_out}}")
        print(f"\nUnits: [1]m³, [2]L, [3]mL, [4]gal(US), [5]gal(imp), [6]qt(US), [7]qt(imp), [8]pt(US), [9]pt(imp), [10]ft³, [11]in³")

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

        calc = round(convert_volume(val, menu_volume(opt1), menu_volume(opt2)),4)
        print(f"\n{'':-^{tbl_len_out}}")
        print(f"\n{inp_val} {menu_volume(opt1)} is equal to {calc} {menu_volume(opt2)}")

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