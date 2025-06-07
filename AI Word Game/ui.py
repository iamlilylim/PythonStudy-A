import tkinter as tk
from logic import get_question, check_answer
#design the game app
class WordGameApp:
    def __init__(self, root):
        self.level = "easy" #default level: easy
        #get a quiz
        self.word, self.meaning = get_question(self.level)

        #showing the meaning on the window
        self.label = tk.Label(root, text=f'meaning is: {self.meaning}')
        self.label.pack() #on the window

        #user input window
        self.entry = tk.Entry(root)
        self.entry.pack()

        #ergebnis label
        self.result = tk.Label(root, text= '')
        self.result.pack()


        #'enter'button -> when clicked, execute 'submit'
        tk.Button(root, text='enter', command=self.submit).pack()
    def submit(self):
        user_input = self.entry.get() # getting the input
        #checking the answer
        if check_answer(self.word, user_input):
            self.result.config(text=f'😆CORRECT!',fg='green')
        else:
            self.result.config(text=f'❌INCORRECT!❌ the answer is {self.word}', fg='red')

def run_app():
    root = tk.Tk() #tkinter basic window
    root.title('AI Word Game')
    WordGameApp(root) # open the game frame
    root.mainloop()
