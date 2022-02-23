# Calculate Consumption

# Up to 210kWh consumption 1kWh = 1.37 TL
# After 210kWh consumption 1kWh = 2.055 TL
tarif = 1.37
limit = 210

# Fatura fonksiyonu
def tktm(a) :
    if a < (tarif * limit) :
        a = a / 1.37
        return a
    else :
        b = limit + ((a - (tarif * limit)) / (tarif * 1.5))
        return b

inp_ftr = input('\nEnter the invoice amount: ')
try :
    ftr = float(inp_ftr)
except :
    print('\n!!! Please enter numerical value!\n')
    quit()

tuketim = round(tktm(ftr))
print('\nConsumption amaount is ',tuketim,'kWh.\n')
