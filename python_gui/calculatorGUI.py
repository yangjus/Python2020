#created 3/31/2020, tkinter project #1
import tkinter as tk

#creates main window GUI
window = tk.Tk()
window.title("Simple Calculator")

# globally declare the expression variable 
expression = "" 
  
  
# Function to update expression(either number or operator)
# in the text entry box 
def press(num): 
    # point out the global expression variable 
    global expression 
  
    # concatenation of string 
    expression = expression + str(num) 
  
    # update the expression by using set method 
    equation.set(expression) 
  
  
# Function to evaluate the final expression 
def equalpress(): 
    # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 
  
    # Put that code inside the try block 
    # which may generate the error 
    try: 
  
        global expression 
  
        # eval function evaluate the expression 
        # and str function convert the result 
        # into string 
        total = str(eval(expression)) 
  
        equation.set(total) 
  
        # initialze the expression variable 
        # by empty string 
        expression = "" 
  
    # if error is generate then handle 
    # by the except block 
    except: 
  
        equation.set(" Error ") 
        expression = "" 
  
  
# Function to clear the contents 
# of text entry box 
def clear(): 
    global expression 
    expression = "" 
    equation.set("")
    
#changes widthxheight of window, and +Xpos+Ypos of window relative to screen
window.geometry("250x300+900+350")
#equation is instance of stringVar() class from tkinter module
equation = tk.StringVar()   #set as a proxy for expression variable
equation.set('0')

screen = tk.Entry(window, textvariable=equation, width=20, font='Calibri 20', justify='right')  #use textvariable here
screen.grid(row=0, columnspan=4, pady=20, ipady=10)

a = 10 #width of button
b = 5 #height of button

#passing functions with parameters through command= is hard without lambda
#lambda is used to create a temporary, one-time function to be called, and no arguments are needed
seven = tk.Button(window, text='7', width=a, height=b, command=lambda: press(7)).grid(row=1, column=0)
eight = tk.Button(window, text='8', width=a, height=b, command=lambda: press(8)).grid(row=1, column=1)
nine = tk.Button(window, text='9', width=a, height=b, command=lambda: press(9)).grid(row=1, column=2)
divide = tk.Button(window, text='/', width=a, height=b, command=lambda: press("/"), bg='lightgray').grid(row=1, column=3)

four = tk.Button(window, text='4', width=a, height=b, command=lambda: press(4)).grid(row=2, column=0)
five = tk.Button(window, text='5', width=a, height=b, command=lambda: press(5)).grid(row=2, column=1)
six = tk.Button(window, text='6', width=a, height=b, command=lambda: press(6)).grid(row=2, column=2)
multiply = tk.Button(window, text='x', width=a, height=b, command=lambda: press("*"), bg='lightgray').grid(row=2, column=3)

one = tk.Button(window, text='1', width=a, height=b, command=lambda: press(1)).grid(row=3, column=0)
two = tk.Button(window, text='2', width=a, height=b, command=lambda: press(2)).grid(row=3, column=1)
three = tk.Button(window, text='3', width=a, height=b, command=lambda: press(3)).grid(row=3, column=2)
subtract = tk.Button(window, text='-', width=a, height=b, command=lambda: press("-"), bg='lightgray').grid(row=3, column=3)

clear = tk.Button(window, text='C', width=a, height=b, command=clear, bg='red', fg='white').grid(row=4, column=0)
zero = tk.Button(window, text='0', width=a, height=b, command=lambda: press(0)).grid(row=4, column=1)
equal = tk.Button(window, text='=', width=a, height=b, command=equalpress, bg='green', fg='white').grid(row=4, column=2)
add = tk.Button(window, text='+', width=a, height=b, command=lambda: press("+"), bg='lightgray').grid(row=4, column=3)

for r in range(1,5):
    window.grid_rowconfigure(r, weight=1)
for c in range(4):
    window.grid_columnconfigure(c, weight=1)

window.mainloop()
