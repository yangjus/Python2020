#created 4/2/2020, tkinter project #2
from tkinter import *

window = Tk()
window.title("Basic Converter")

window.geometry("500x300+500+350")

#globally declare measurement variables
measurement1 = ""
measurement2 = ""

def convert_SI(val, unit_in, unit_out):     #based on unitconverters.net
    SI = {'Meter':1, 'Kilometer':1000, 'Centimeter':0.01, 'Millimeter':0.001,
          'Micrometer':0.000001, 'Mile':1609.35, 'Yard':0.9144, 'Foot':0.3048,
          'Inch':0.0254}
    return val*SI[unit_in]/SI[unit_out]

def helpsection():
    popup = Tk()
    popup.wm_title("Instructions")
    popup.geometry("400x150+550+450")
    label = Label(popup, text="""Instructions: Enter valid number in left entry box,
select what to convert from and what to convert to in the list boxes and
then click convert button. Do not enter anything in right entry box.
This is a simple unit converter by Justin. Created 4/2/2020.""")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def selectedInput():
    global measurement1
    measurement1 = listbox.get(listbox.curselection())#whatever is currently selected

def selectedOutput():
    global measurement2
    measurement2 = listbox1.get(listbox1.curselection()) #whatever is currently selected

def converter():
    try:
        global measurement1, measurement2
        result.set(str(convert_SI(float(inputEntry.get()), measurement1, measurement2)))
                    
    except:
        result.set("Error")

title = Label(window, text="Basic Converter", font="Calibri 16")
title.grid(columnspan=3)
result = StringVar()    #initalize dispalyed output variable
#create a top-level menu
filemenu = Menu(window)
filemenu.add_command(label='Help', command=helpsection)
window.config(menu=filemenu)    #displays menu
#input and output entry fields
inputEntry = Entry(window)
inputEntry.grid(row=1, column=0)
arrow = Label(window, text="--->", font="Calibri 20").grid(row=1, column=1)
outputEntry = Entry(window, textvariable=result).grid(row=1, column=2)

convertButton = Button(window, text='Convert!', command=converter).grid(row=2, column=1)

#if nonetype error, because .grid needs to be called on thier own line since it always returns None
scrollbar = Scrollbar(window)   #left scrollbar
scrollbar.grid(row=2, column=0, sticky = NE + SE)
listbox = Listbox(window, exportselection=False)   #left listbox
#exportselection option in order to select 2 different listbox at same time
listbox.grid(row=2, column=0)

measurement_list = ['Meter', 'Kilometer', 'Centimeter', 'Millimeter',
                    'Micrometer', 'Mile', 'Yard', 'Foot', 'Inch']
for measurement in measurement_list:
    listbox.insert(END, measurement)
listbox.bind("<<ListboxSelect>>", lambda x: selectedInput())   #this instead of command= option
# attach listbox to scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


scrollbar1 = Scrollbar(window)   #right scrollbar
scrollbar1.grid(row=2, column=2, sticky = NE + SE)   #add sticky if scrollbar not showing
listbox1 = Listbox(window, exportselection=False)   #right listbox
listbox1.grid(row=2, column=2)

for measurement in measurement_list:
    listbox1.insert(END, measurement)
listbox1.bind("<<ListboxSelect>>", lambda x: selectedOutput())
listbox1.config(yscrollcommand=scrollbar1.set)
scrollbar1.config(command=listbox1.yview)

#configure grid layout to adjust whenever window dimensions change
for i in range(3):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)
    

window.mainloop()
