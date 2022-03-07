inp_price = input('\nEnter item price: ')
try :
    price = float(inp_price)
except :
    print('\n!!! Please enter numerical value!\n')
    quit()

inp_rate = input('Enter tax rate: %')
try :
    rate = float(inp_rate)
except :
    print('\n!!! Please enter numerical value!\n')
    quit()

tax = round(price * rate/100, 2)

total = price + tax

print('\nPrice without tax: ', price)
print('Tax (%',rate,'):', tax)
print('Price included tax: ', total, '\n')