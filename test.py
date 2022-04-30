# Importing the modules
import tkinter as tk
from tkinter.constants import UNITS
import tkinter.font as font
from functools import partial
from tkinter import StringVar, messagebox
from tkinter import ttk

# Creating the window
window  =tk.Tk()
window.geometry('500x600')
window.title('Unit Converter')
window.configure(bg = 'peach puff2')

# Creating the fonts
font1 = font.Font(family = 'helvetica',size = '30')
font2 = font.Font(family = 'helvetica',size = '10')
font3 = font.Font(family = 'helvetica',size = '20')

# The textvariables
number_from = StringVar()

# All the functions
# Fromfunc function
def fromfunc(event):
    global result_from
    result_from = event.widget.get()

# Tofunc function
def tofunc(event):
    global result_to
    result_to = event.widget.get()


# The answer function
def answer(n1):
    num1 = n1.get()
    try:
        number1 = int(num1)
    except:
        messagebox.showerror('Error','Term not recognised')

    # Length
    if result_from == 'Cubic meters' and result_to == 'Cubic meters':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic meters' and result_to == 'Cubic foot':
        calculate = number1*35.3147
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic meters' and result_to == 'Liters':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic meters' and result_to == 'Gallons':
        calculate = number1*264.172
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic meters' and result_to == 'Cubic centimeters':
        calculate = number1*1000000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic foot' and result_to == 'Cubic meters':
        calculate = number1*0.02831
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic foot' and result_to == 'Cubic foot':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic foot' and result_to == 'Liters':
        calculate = number1*28.31679
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic foot' and result_to == 'Gallons':
        calculate = number1*7.4805
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic foot' and result_to == 'Cubic centimeters':
        calculate = number1*28316.8
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Liters' and result_to == 'Cubic meters':
        calculate = number1*0.000999
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Liters' and result_to == 'Cubic foot':
        calculate = number1*0.0353146
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Liters' and result_to == 'Liters':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Liters' and result_to == 'Gallons':
        calculate = number1*0.26417
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Liters' and result_to == 'Cubic centimeters':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Gallons' and result_to == 'Cubic meters':
        calculate = number1*0.003785
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Gallons' and result_to == 'Cubic foot':
        calculate = number1*0.13368
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Gallons' and result_to == 'Liters':
        calculate = number1*3.7854
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Gallons' and result_to == 'Gallons':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Gallons' and result_to == 'Cubic centimeters':
        calculate = number1*3786.41
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Cubic meters':
        calculate = number1*9.99999
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Cubic foot':
        calculate = number1*3.53146
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Cubic centimeters' and result_to == 'Liters':
        calculate = number1*0.000999
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Cubic meters':
        calculate = number1*9.9999
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Liters':
        calculate = number1*0.00099999
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Gallons':
        calculate = number1*0.00026417
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Cubic centimeters':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

# Selected function
def selected(event):
    unit = event.widget.get()
    if unit == 'Volume':
        fromdd['values'] = ('Cubic meters',
                            'Cubic foot',
                            'Liters',
                            'Gallons',
                            'Cubic centimeters')

        todd['values'] = ('Cubic meters',
                            'Cubic foot',
                            'Liters',
                            'Gallons',
                            'Cubic centimeters')

    elif unit == 'Length':
        fromdd['values'] = ('Millimeters',
                            'Centimeters',
                            'Decimeters',
                            'Meters',
                            'Kilometers')

        todd['values'] = ('Millimeters',
                            'Centimeters',
                            'Decimeters',
                            'Meters',
                            'Kilometers')

    elif unit == 'Mass':
        fromdd['values'] = ('Milligrams',
                            'Centigrams',
                            'Grams',
                            'Decigrams',
                            'Kilograms')

        todd['values'] = ('Milligrams', 'Centigrams', 'Grams', 'Decigrams', 'Kilograms')
    


# Creating the unit converter label
main = tk.Label(window,text = 'Unit Converter',bg = 'peach puff2',fg = 'blue')
main['font'] = font1
main.place(relx = '0.48',rely = '0.1',anchor = 'center')

# Creating the unit label
unit = tk.Label(window,text = 'Unit -:',bg = 'peach puff2')
unit['font'] = font2
unit.place(relx = '0.25',rely = '0.28')

# Creating the main combobox
n = StringVar()
unitdd = ttk.Combobox(window,width = '35',textvariable = n)

# Values
unitdd['values'] = ('Volume', 'Length', 'Mass')

unitdd.place(relx = '0.57',rely = '0.3',anchor = 'center')
unitdd.current()
unitdd.bind('<<ComboboxSelected>>',selected)

# Creating the from label
label_from = tk.Label(window,text = 'From -:',bg = 'peach puff2')
label_from['font'] = font2
label_from.place(relx = '0.238',rely = '0.37')

# Creating the fromdd
f = StringVar()
fromdd = ttk.Combobox(window,width = '35',textvariable = f)

fromdd.place(relx = '0.57',rely = '0.39',anchor = 'center')
fromdd.current()
fromdd.bind('<<ComboboxSelected>>',fromfunc)

# Creating the num_from entry
num_from = tk.Entry(window,width = 10,textvariable = number_from)
num_from.place(relx = '0.82',rely = '0.37')

answer = partial(answer,num_from)

# Creating the to label
to = tk.Label(window,text = 'To -:',bg = 'peach puff2')
to['font'] = font2
to.place(relx = '0.268',rely = '0.45')

# Creating the to drop down
t = StringVar()
todd = ttk.Combobox(window,width = 35,textvariable = t)

todd.place(relx = '0.57',rely = '0.47',anchor = 'center')
todd.current()
todd.bind('<<ComboboxSelected>>',tofunc)

# Creting the result label
result = tk.Label(window,text = '',bg= 'white',width = 20)
result['font'] = font3
result.place(relx = '0.21',rely = '0.6')

# Creating the get answer button
get_answer = tk.Button(window,text = 'Get Answer',bg = 'cyan2',command = answer)
get_answer['font'] = font2
get_answer.place(relx = '0.46',rely = '0.7')

# Creating the art label
art = tk.Label(window,text = 'The Art Of Programming',bg= 'peach puff2',fg = 'blue')
art['font'] = font3
art.place(relx = '0.21',rely = '0.9')

# Creating the mainloop
window.mainloop()