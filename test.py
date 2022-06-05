# ELEKTRİK FATURASI VEYA TÜKETİMİ HESAPLAYICI PROGRAM
# Tüketim miktarından gelecek olan yaklaşık fatura miktarını veya
# Faturadan tüketim miktarını hesaplayabilirsiniz.

# Copyright (C) 2022  Baris Kayadelen

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep
from unicodedata import digit

# import pandas
import pandas as pd

# import numeric to check digits
from unicodedata import numeric

import csv

# Table
tbl_len_out = 78
tbl_len_in = 38

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# def menu_electric():
#     # get data from csv file
#     df_csv = pd.read_csv('tr_elektrik_tarifesi.csv', 
#         index_col = 'Seçenek',
#         # if you don't have header column you can tag it 
#         # names=['Seçenek','Abone Grubu','Tarife','Tarife Bedeli','Dağıtım Bedeli']
#         usecols = ['Seçenek','Abone Grubu','Tarife'])
#     return(df_csv)

def menu_electric():
    with open('tr_elektrik_tarifesi.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f' {", ".join(row["Seçenek"])}')
                line_count += 1
            print(f' [{row["Seçenek"]}] {row["Abone Grubu"]} - {row["Tarife"]}')
            line_count += 1
        # print(f'Processed {line_count} lines.')

def electric_tarif(a,b):

    return a, b

while True :

    clear()
    inp_choice = None
    inp_opt1 = None
    inp_opt2 = None

    print(f"\n{' Elektrik Faturası Hesaplama Programı ':=^{tbl_len_out}}")
    print(f"\nLütfen aşağıdaki menüden abone grubunuza göre tarifenizi seçiniz:\n")
    menu_electric()
    # print(f"\n{' [1] Area ':{tbl_len_in}}  {' [4] Temperature ':{tbl_len_in}}")
    # print(f"{' [2] Fuel Consumption ':{tbl_len_in}}  {' [5] Weight ':{tbl_len_in}}")
    # print(f"{' [3] Length ':{tbl_len_in}}  {' [6] Volume  ':{tbl_len_in}}")
    inp_choice = input(f"\n{' [Q] Çıkış ':{tbl_len_in}}  {'  ':{tbl_len_in}} \n\nSeçenek: ")

    if inp_choice == "1" :
        clear()
        print(f"\n{' Elektrik Faturası Hesaplama Programı ':=^{tbl_len_out}}")
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

    # Program Exit
    elif inp_choice == "Q":
        print(f"\n{' Hoşçakalın ':=^{tbl_len_out}}\n")
        break
    elif inp_choice == "q":
        print(f"\n{' Hoşçakalın ':=^{tbl_len_out}}\n")
        break
    else :
        clear()
        print(f"\n{' Elektrik Faturası Hesaplama Programı ':=^{tbl_len_out}}")
        # print(f"\n{' !!!!! ':-^{tbl_len_out}}")
        print("\n!!!!! Lütfen seçenek numarasını doğru giriniz.")
        print(f"\n{'':-^{tbl_len_out}}\n")
        sleep(4)
    
    continue