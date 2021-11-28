#created 4/4/2020, finished 4/4/2020. tkinter project #4
import tkinter as tk
import random

class MainApplication(tk.Frame):
    
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        parent.title("Rock Paper Scissor")
        parent.geometry("500x300+500+350")

        self.user_score = 0
        self.computer_score = 0
        self.user_choice = 0
        self.computer_choice = 0
        self.choice_to_number = {"rock": 0, "paper": 1, "scissor": 2}
        self.choice = {0: "rock", 1: "paper", 2: "scissor"}

        self.rockButton = tk.Button(self.parent, font="16", text="Rock", command=self.rock)
        self.paperButton = tk.Button(self.parent, font="16", text="Paper", command=self.paper)
        self.scissorButton = tk.Button(self.parent, font="16", text="Scissor", command=self.scissor)
        self.board = tk.Text(self.parent, bg="#FFFF99", height=14, width=45)
        self.board.insert(tk.END, "User Choice:\nComputer's Choice:\n\nYour Score:\nComputer Score:")

        self.rockButton.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)   #expands to cell size
        self.paperButton.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
        self.scissorButton.grid(row=0, column=2, sticky=tk.N+tk.S+tk.E+tk.W)
        self.board.grid(row=1, column=0, columnspan=3, sticky=tk.N+tk.S+tk.E+tk.W)

        for r in range(2):
            parent.grid_rowconfigure(r, weight=1)
        for c in range(3):
            parent.grid_columnconfigure(c, weight=1)

    def rock(self):
        user_choice = self.choice_to_number["rock"]
        computer_choice = random.randint(0, 2)
        self.result(user_choice, computer_choice)

    def paper(self):
        user_choice = self.choice_to_number["paper"]
        computer_choice = random.randint(0, 2)
        self.result(user_choice, computer_choice)

    def scissor(self):
        user_choice = self.choice_to_number["scissor"]
        computer_choice = random.randint(0, 2)
        self.result(user_choice, computer_choice)

        
    def result(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            print("tie")
        elif (user_choice-computer_choice)%3 == 1:
            print("user wins")
            self.user_score += 1
        else:
            print("computer wins")
            self.computer_score += 1
        result = """User Choice: {}\nComputer's Choice: {}\n\nYour Score: {}\nComputer Score: {}
                """.format(self.choice[user_choice], self.choice[computer_choice], self.user_score, self.computer_score)
        self.board.delete('1.0', tk.END)
        self.board.insert(tk.END, result)


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()
