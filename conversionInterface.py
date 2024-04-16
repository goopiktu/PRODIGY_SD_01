from tkinter import *
from conversionLogic import main

root = Tk()
root.title("Temperature converter")
root.geometry("500x100")

# Change the label text 
def show():
    label.config( text = firstArg.get() + " to " + secondArg.get())  
    return main(firstArg.get(), secondArg.get(), float(firstEntry.get())) 

# for setting the 2nd Entry
def set_text():
    secondEntry.delete(0, END)
    ans = show()
    fans = round(ans, 3)
    secondEntry.insert(0, str(fans))
    return

# Dropdown menu options 
options = [ 
    "Celsius", 
    "Farenheit", 
    "Kelvin", 
] 
  
firstEntry = Entry(root, font=("Arial", 15) )
secondEntry = Entry(root, font=("Arial", 15) )
secondEntry.grid(row=0, column=1)
firstEntry.grid(row=0, column=0)

# datatype of menu text 
firstArg = StringVar() 
secondArg = StringVar()
  
# initial menu text 
firstArg.set( "Celsius" ) 
secondArg.set( "Farenheit" )
  
# Create Dropdown menu 
drop = OptionMenu( root , firstArg , *options) 
drop1 = OptionMenu( root , secondArg , *options)
drop.config(width=14, font=("Arial", 15))
drop1.config(width=14, font=("Arial", 15))
drop.grid(row=1, column=0) 
drop1.grid(row=1, column=1)
  
# Create button, it will change label text 
button = Button( root , text = "=" , command =lambda:set_text(), font=("Arial", 15) ).grid(row=0, column=3, rowspan=3)


# Create output Label 
label = Label( root , text = " ", font=("Arial", 15)) 
label.grid(row=3, column=0, columnspan=2)


  
# Execute tkinter 
root.mainloop() 