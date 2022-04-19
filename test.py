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

list_area = {1:'km²', 2:'ha', 3:'daa', 4:'a', 5:'m²', 6:'mm²', 7:'mi²', 8:'yd²', 9:'ft²', 10:'in²', 11:'acre'}
def menu_area(unit):
    list_area
    return list_area[unit]
