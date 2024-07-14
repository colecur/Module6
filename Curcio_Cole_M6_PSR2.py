import tkinter as tk
from tkinter import *
import random

window_one = Tk()
window_one.geometry("350x230")

class window_two(tk.Toplevel):
    def open_Toplevel():
        window_two = Toplevel()
        window_two.title('Your guessed bill')
        l2 = Label(window_two, text='You guess the right calculation for the bill!')
        l2.pack()
        window_two.geometry("350x570")
        def exit():
            window_two.destroy()

l = Label(window_one, text='The Calculation of the Steak Joint')
l.pack()

total_price = Label(text='The total price is: $')

# Display the list of five dinners and prices.
tables = ['Dinner 1 ', 'Dinner 2 ', 'Dinner 3 ', 'Dinner 4 ', 'Dinner 5 ']
price = [35.52, 27.13, 41.71, 39.95, 48.20]

# Allow the user to select the dinners and quantities.
dinner = ['Dinner 1 ', 'Dinner 2 ', 'Dinner 3 ', 'Dinner 4 ', 'Dinner 5 ']
print(random.choice(dinner))
price = [35.52, 27.13, 41.71, 39.95, 48.20]
print(random.choice(price))

def buttonFunction():
    print(random.choice(price))

b1 = Button(window_one, text='Select the bill as your guess', 
                                        command = window_two)
b1.pack(side=TOP)

b2 = Button(window_one, text='Cancel the order', 
                                        command=exit)
b2.pack(side=LEFT)
def stop():
    window_one.destroy()

b3 = Button(window_one, text='Close', 
                                command=exit)
b3.pack(side=BOTTOM)
def exit():
    window_one.destroy()

window_one.mainloop()
window_two.open_Toplevel()