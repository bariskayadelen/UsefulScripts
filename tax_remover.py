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

item =  round((100 * price) / (100 + rate), 2)

tax =  round((price - item),2)

print('\nPrice included tax: ', price)
print('Tax (%',rate,'):', tax)
print('Price without tax: ', item, '\n')