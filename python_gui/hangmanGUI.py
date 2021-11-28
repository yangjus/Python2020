# created 4/2/2020, finished 4/3/2020. editied: 4/4/2020, tkinter project #3
import tkinter as tk
import random
from functools import partial
import sys, os

#future plans:
#create actual hangman using canvas on a separate class and then polymorph (?) into MainApp class
#touch on formatting when window is resized
#add easy, medium, hard mode (make function to change lives and list_of_words in same frame)
#create a general popup function for lose_popup and win_popup and other similar functions
#create an I/O statement where easy for list_of_words to recieve more words through a .txt file

class MainApplication(tk.Frame):
    button_identities = {}
    list_of_words = ['hello', 'win', 'you', 'okay', 'solve', 'motorist', 'warn', 'muscle',
                     'shoot', 'frighten', 'spare', 'transfer', 'embrace', 'look', 'technique',
                     'electron', 'superior', 'eyebrow', 'harmony', 'vat', 'looting', 'adopt', 'angle',
                     'error', 'rescue', 'vacuum', 'feather', 'beard', 'separation', 'completion',
                     'patch', 'agency', 'bare', 'problem', 'revolution', 'point', 'expose', 'month']
    #random word selection
    mystery_string = list_of_words[random.randint(0, len(list_of_words)-1)]

    def create_underscores(self):
        self.underscores = ""
        for i in range(len(self.mystery_string)):
            self.underscores = self.underscores + "_ "
        return self.underscores

    def create_letter_button(self, row_number, rownum, i):
        self.curButton = tk.Button(self.parent, text=row_number[i].upper(), width=8, height=4, font="12",
                                   command=partial(self.press, row_number[i], rownum, i))   #partial
        self.curButton.grid(row=rownum, column=i)
        self.button_identities[(rownum, i)] = self.curButton

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        parent.title("Hangman")
        parent.geometry("500x300+500+350")

        alphabet_row = []
        self.var_lives = tk.StringVar()
        self.amount_lives_left = 6  #number of lives left
        self.var_lives.set(self.amount_lives_left)
        self.var_string = tk.StringVar()
        self.var_string.set(self.create_underscores())

        #set alphabet buttons in a grid format
        alphabet_row.append(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
        alphabet_row.append(['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'])
        alphabet_row.append(['s', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
        #create buttons
        for rownum in range(2,5):
            for i in range(len(alphabet_row[rownum-2])):
                self.create_letter_button(alphabet_row[rownum-2], rownum, i)

        self.label_lives = tk.Label(self.parent, text='Lives left: ')
        self.number_lives = tk.Label(self.parent, anchor=tk.W, textvariable=self.var_lives)
        self.string = tk.Label(self.parent, font="Calibri 30", textvariable=self.var_string)
        
        self.label_lives.grid(row=0, column=0, columnspan=2)
        self.number_lives.grid(row=0, column=2)
        self.string.grid(row=0, column=3, columnspan=8, rowspan=2)
        for r in range(6):
            parent.grid_rowconfigure(r, weight=1)
        for c in range(9):
            parent.grid_columnconfigure(c, weight=1)

    def press(self, char, row, col):
        button_name = self.button_identities[(row, col)] #calls button in certian row and col
        button_name.config(state=tk.DISABLED)   #disables button
        if char in self.mystery_string:
            button_name.config(bg='green', disabledforeground='white')
            self.fill_in_string(char)
        else:
            button_name.config(bg='red', disabledforeground='white')
            self.wrong_letter()

    def fill_in_string(self, char):
        list_string = (self.var_string.get()).split(' ')
        for letter in range(len(self.mystery_string)):
            if char == self.mystery_string[letter]:
                list_string[letter] = char
        matchingString = ""
        self.var_string.set(" ".join(list_string))
        #if string so far matches the mystery_string, then win
        for letter in list_string:
            matchingString = matchingString + letter
        if matchingString == self.mystery_string:
            self.win_popup()

    def wrong_letter(self):
        self.amount_lives_left = self.amount_lives_left - 1
        self.var_lives.set(self.amount_lives_left)
        if self.amount_lives_left == 0:
            self.lose_popup()
            
    def win_popup(self):
        alist = ["Congrats!", "You win!", "Smart!", "You deserve a W!"]
        the_text = alist[random.randint(0, 3)]
        popup = tk.Tk()
        popup.wm_title("Win!")
        popup.geometry("300x75+600+450")
        label = tk.Label(popup, text=the_text)
        label.pack(side="top", fill="x", pady=10)
        B1 = tk.Button(popup, text="Reset game", command = lambda:[popup.destroy, self.restart_game()])
        B1.pack()
        popup.mainloop()
        
    def lose_popup(self):
        announcement = "The word was:  {}\n".format(self.mystery_string)
        alist = ["You lose.", "Take the L.", "Better luck next time."]
        the_text = announcement + alist[random.randint(0, 2)]
        popup = tk.Tk()
        popup.wm_title("Loss")
        popup.geometry("300x75+600+450")
        label = tk.Label(popup, text=the_text)
        label.pack(side="top", fill="x", pady=10)
        B1 = tk.Button(popup, text="Reset game", command = lambda:[popup.destroy, self.restart_game()])
        B1.pack()
        popup.mainloop()

    def restart_game(self):     #import os and sys modules
        python = sys.executable
        os.execl(python, python, * sys.argv)

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()
