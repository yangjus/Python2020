#created 4/4/2020, tkinter project #5
import tkinter as tk
from time import time
import random
import sys, os

#future plans:
#polish up game interface
#create a top down menu with help section
#input score_variable at the end of game along with a user inputted -
    #name into a highscore.csv file that also outputs in beginning of game into topdown menu's highscore section
#highscore.csv file is sorted by score when outputted into highscore section, with date, name, and score columns respectively.
#add more variety of colors and more buttons on separate difficulty levels (with different sizes of buttons too for more mayhem)

score_variable = 0    #starting score
timeleft = 30   #in seconds
color_list = ['red', 'blue', 'yellow', 'green', 'orange', 'purple']
class MainApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        parent.title("Color Game")
        parent.geometry("500x300+500+350")  #frame dimensions

        #initializes StringVar (ability for string to change value at button press)
        self.var_color_wanted = tk.StringVar(value="blue")
        self.var_score = tk.StringVar(value="Score: 0")
        self.var_time = tk.StringVar(value="  Play  ")

        self.color_label = tk.Label(parent, font="35", fg="blue", textvariable=self.var_color_wanted)
        self.button_play = tk.Button(parent, font="30", textvariable=self.var_time, command=self.play)   #play button
        self.score_label = tk.Label(parent, font="20", textvariable=self.var_score)    #score label
        self.button_1 = tk.Button(parent, text="", fg="white", bg="red", command=lambda: self.change_score(self.button_1.cget('bg')))
        self.button_2 = tk.Button(parent, text="", fg="white", bg="blue", command=lambda: self.change_score(self.button_2.cget('bg')))
        self.button_3 = tk.Button(parent, text="", fg="white", bg="yellow", command=lambda: self.change_score(self.button_3.cget('bg')))
        self.button_4 = tk.Button(parent, text="", fg="white", bg="green", command=lambda: self.change_score(self.button_4.cget('bg')))
        self.button_5 = tk.Button(parent, text="", fg="white", bg="orange", command=lambda: self.change_score(self.button_5.cget('bg')))
        self.button_6 = tk.Button(parent, text="", fg="white", bg="purple", command=lambda: self.change_score(self.button_6.cget('bg')))

        #sets position
        self.color_label.grid(row=0, column=0, sticky=tk.N+tk.E+tk.S+tk.W)
        self.button_play.grid(row=0, column=1)
        self.score_label.grid(row=0, column=2, sticky=tk.N+tk.E+tk.S+tk.W)
        self.button_1.grid(row=1, column=0, sticky=tk.N+tk.E+tk.S+tk.W)
        self.button_2.grid(row=1, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
        self.button_3.grid(row=1, column=2, sticky=tk.N+tk.E+tk.S+tk.W)
        self.button_4.grid(row=2, column=0, sticky=tk.N+tk.E+tk.S+tk.W)
        self.button_5.grid(row=2, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
        self.button_6.grid(row=2, column=2, sticky=tk.N+tk.E+tk.S+tk.W)
        
        self.paused = True
        
        for r in range(3):  #configures even grid size
            parent.grid_rowconfigure(r, weight=1)
        for c in range(3):
            parent.grid_columnconfigure(c, weight=1)
            
    def play(self): #starts game, sets countdown timer of 30 seconds
        if self.paused:
            self.paused = False
            self.oldtime = time()
            self.run_timer()

    def run_timer(self):    #timer for 30 seconds
        if self.paused:
            return
        delta = int(time() - self.oldtime)
        self.var_time.set('{:02}:{:02}'.format(*divmod(delta, 60)))
        self.button_play.after(1000, self.run_timer)
        if delta >= 30 and delta < 31:  #limits so only one popup occurs once reaches goal time
            self.game_end_popup()

    def game_end_popup(self):   #game over popup and restart game option
        global score_variable
        popup = tk.Tk()
        popup.wm_title("Your Time is Up!")
        popup.geometry("500x300+500+350")
        label = tk.Label(popup, font="60", text="Your score is: {}".format(score_variable))
        label.pack(side="top", fill="x", pady=10)
        B1 = tk.Button(popup, text="Play Again", command = lambda:[popup.destroy, self.restart_game()])
        B1.pack()
        popup.mainloop()

    def restart_game(self):     #import os and sys modules
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def change_score(self, color):  #adds one to score if color picked is the color text presented
        global score_variable, color_list
        if color == self.var_color_wanted.get():
            score_variable += 1
        self.var_score.set("Score: " + str(score_variable))
        self.var_color_wanted.set(random.choice(color_list)) #sets different text presented for next round
        self.color_label.config(fg=(random.choice(color_list))) #sets different color for the text
        if self.color_label.cget('fg') == "yellow": #because yellow doesn't show clearly in text, no outlining either
            self.color_label.config(fg="black")
        self.change_color()
        print(color)    #bug checking and testing

    def change_color(self): #randomly changes all 6 button colors for next round
        global color_list
        random.shuffle(color_list)
        button_list = [self.button_1, self.button_2, self.button_3, self.button_4, self.button_5, self.button_6]
        for i in range(6):
            button_list[i].config(bg=color_list[i])
        
    
if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()
