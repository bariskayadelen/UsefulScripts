def aa(x):
    MN = {'1':'km', '2':'m', '3':'cm', '4':'mm', '5':'μm', '6':'nm', '7':'mi', '8':'yd', '9':'ft', '10':'in'}
    for x, y in list(MN.items()):
        return y

print(aa(3))