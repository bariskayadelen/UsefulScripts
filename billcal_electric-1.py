# Calculate Bill

# Up to 210kWh consumption 1kWh = 1.37 TL
# After 210kWh consumption 1kWh = 2.055 TL
tarif = 1.37
limit = 210

# Bill Function
def ftr(a,b) :
    if a <= limit :
        c = a * b
        return c
    else :
        c = (limit * b) + ((a - limit) * b * 1.5)
        return c 

inp_ilk = input('\nEnter first meter value: ')
try :
    ilk = float(inp_ilk)
except :
    print('\n!!! Please enter numerical value!\n')
    quit()

inp_son = input('Enter last meter value: ')
try :
    son = float(inp_son)
except :
    print('\n!!! Please enter numerical value!\n')
    quit()

tuketim = son - ilk
fatura =  round(ftr(tuketim,tarif),2)

if tuketim >= 0 :
    print('\nConsumption amount:',tuketim,'kWh and your bill is', fatura,'TL. \n')
else :
    print('\nError!!! The last reading can not be smaller than the first reading. Please check your values!\n')