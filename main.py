from tkinter import *
from Gui import Window
from sort import *


# set the root
root = Tk()

# Home window
win1 = Window(root,(400,200),"Machine Sort", "pics/logo.ico","#dddddd")

# Lable for menu
choose_label = Label(root, text="Choose Sort Method:", bg="#dddddd")
choose_label.grid(row=0, column=0)

# Sort methods
sort_options = ("Bubble Sort", "Quick Sort", "Selction Sort")


def fixElements(arr):
    newArray = [float(i) for i in arr]
    n = len(newArray)
    for i in range(n):
        if newArray[i].is_integer():
            newArray[i] = int(newArray[i])
    return newArray

def check_array(arr):
        checked = [s for s in arr if s.isdigit()]
        if len(arr) != len(checked):
            return False
        return TRUE

def Sort(met,arr):
    fixed_array = [i for i in arr.split()]
    if check_array(fixed_array):
        fixed_array = fixElements(fixed_array)
        if met == sort_options[0]:
            out = Label(root, text="324")
            out.grid(row=2, column=1)
    else:
        return

def Sort_method():
    met = var.get()
    if met in sort_options:
        global array_box
        array_box = Entry(root)
        array_box.grid(row=1, column=1, columnspan=2, sticky=W+E)
        global box_val 
        box_val = array_box.get()
        array_box.delete(0,END)
        sort_button = Button(root, text="Sort", command=lambda met=met, box_val=box_val: Sort(met,box_val))
        sort_button.grid(row=1,column=2)
    else:
        print("ERROR")

# Sets the menu bar
var = StringVar()
var.set("Method")
sort_type = OptionMenu(root, var, *sort_options)
sort_type.grid(row=0, column=1, padx=10)


# Lable for menu
select_button = Button(root, text="Select", bg="#dddddd", command=Sort_method)
select_button.grid(row=0, column=2)



# main loop
root.mainloop()
