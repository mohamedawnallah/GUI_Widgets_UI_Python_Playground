from tkinter import *
from tokenize import String

from click import command

window = Tk()

def kg_to_units():
    print(kg_e1_value.get())
    kgs = float(kg_e1_value.get())
    # Kg to Grams
    grm_t1.insert(END,str(kgs*1000)+" grams")
    # Kg to Pounds
    pounds_t2.insert(END,str(kgs*2.20462)+" pounds")
    # Kg to Ounces
    ounces_t3.insert(END,str(kgs*35.274)+" ounces")

lb1 = Label(window,text="Kg")
lb1.grid(row=0,column=0)  # The Label is placed in position 0, 0 in the window


kg_e1_value = StringVar() # Create a special StringVar object
kg_e1 = Entry(window,textvariable=kg_e1_value) # Create an Entry box for users to enter the value
kg_e1.grid(row=0, column=1)

# Create a button widget
# The kg_to_units() function is called when the button is pushed
b1 = Button(window,text="Convert",command=kg_to_units)
b1.grid(row=0, column=2)

# Create three empty text boxes, t1, t2, and t3

grm_t1 = Text(window,height=1,width=25)
grm_t1.grid(row=1, column=0)

pounds_t2 = Text(window,height=1,width=25)
pounds_t2.grid(row=1, column=1)

ounces_t3 = Text(window,height=1,width=25)
ounces_t3.grid(row=1, column=2)


# This makes sure to keep the main window open
window.mainloop()