from tkinter import *
from conversionLogic import main

root = Tk()
root.title("Temperature converter")
root.geometry("450x100")

# Function to change label text
def show():
    return main(firstArg.get(), float(firstEntry.get()))

# Function to set the 2nd Entry
def set_text():
    secondEntry.delete(0, END)
    thirdEntry.delete(0, END)
    ans, ans1 = show()
    secondEntry.insert(0, str(ans))
    thirdEntry.insert(0, str(ans1))

# Dropdown menu options
options = [
    "Celsius",
    "Fahrenheit",
    "Kelvin",
]

# Create Entry widgets
firstEntry = Entry(root, font=("Calibri", 15))
secondEntry = Entry(root, font=("Calibri", 15))
thirdEntry = Entry(root, font=("Calibri", 15))
thirdEntry.grid(row=1, column=3)
secondEntry.grid(row=0, column=3)
firstEntry.grid(row=0, column=0)

# Datatype of menu text
firstArg = StringVar()

# Initial menu text
firstArg.set("Celsius")

# Create Dropdown menu
drop = OptionMenu(root, firstArg, *options)
drop.config(width=16, font=("Calibri", 15))
drop.grid(row=1, column=0)

# Create button to trigger the conversion
button = Button(root, text="=", command=set_text, font=("Calibri", 15))
button.grid(row=0, column=2, rowspan=3, padx=4)

# Centering content in the grid
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

# Execute tkinter
root.mainloop()
