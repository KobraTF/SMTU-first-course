from tkinter import Tk, Label, Button, Entry, StringVar, END, N,S
from random import randint

class GuessingGame:
    def __init__(self,master:'Tk'):
        self.master = master
        master.title('Guess game')
        self.entered_number = 0
        self.goal = randint(1,100)
        self.answer = 'Try your guess'
        self.answer_label = StringVar()
        self.answer_label.set(self.answer)
        self.label = Label(master,textvariable=self.answer_label)
        self.guesses = 0
        vcmd = self.master.register(self.validate)
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.button = Button(master, text="Try", command=lambda: self.guess())
        self.label.grid(row=1,column=1,sticky=N)
        self.entry.grid(row=2, column=1, sticky=N)
        self.button.grid(row=3,column=1, sticky=S)
        
    def guess(self):
        self.guesses+=1
        if self.entered_number == self.goal:
            self.answer = f"{self.goal} is correct, {self.guesses} guesses"
        elif self.entered_number < self.goal:
            print(1)
            self.answer = "Try higher"
        else:
            print(1)
            self.answer = "Try lower"
        self.answer_label.set(self.answer)
        self.entry.delete(0, END)

    def validate(self, new_text: str):
        if not new_text:
            self.entered_number = 0
            return True
        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False
            
root = Tk()
window = GuessingGame(root)
root.mainloop()