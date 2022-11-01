from tkinter import *
from tkinter import messagebox

def get_height():
    height = float(ENTRY2.get())
    return height

def get_weight():
    weight = float(ENTRY1.get())
    return weight

def calculate_bmi():
    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        messagebox.showinfo("Info", "Height")
    except ValueError:
        messagebox.showinfo("Info", "Invalid Input!!")
    else:
        messagebox.showinfo("Your BMI is : ", bmi)

if __name__ == '__main__':
    TOP = Tk()
    TOP.bind("<Return>", calculate_bmi)

    TOP.geometry("400x400")

    TOP.title("BMI Calculator")
    TOP.resizable(width=False, height=False)
    LABLE = Label(TOP, text="BMI Calculator", font=("Helvetica", 15, "bold"), pady=10)
    LABLE.place(x=55, y=0)
    LABLE1 = Label(TOP, text="Weight (Unit as kg):", bd=6, font=("Helvetica", 12, "bold"), pady=5)
    LABLE1.place(x=55, y=60)
    ENTRY1 = Entry(TOP, width=10)
    ENTRY1.place(x=240, y=60)
    LABLE2 = Label(TOP, text="Height (Unit as cm):", bd=6, font=("Helvetica", 12, "bold"), pady=5)
    LABLE2.place(x=55, y=121)
    ENTRY2 = Entry(TOP, width=10)
    ENTRY2.place(x=240, y=121)
    BUTTON = Button(bd=12, text="BMI", padx=33, pady=10, command=calculate_bmi, font=("Helvetica", 20, "bold"))
    BUTTON.grid(row=5, column=0, sticky=W)
    BUTTON.place(x=115, y=250)
    TOP.mainloop()
