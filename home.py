import tkinter as tk
from tkinter import messagebox


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.window_height = self.winfo_height()
        print(self.window_height)
        self.title('Calculator')
        self.geometry('300x400')

        self.create_widgets()

    def create_widgets(self):

        self.topframe = tk.Frame(self, bg='gray',width=5, height=50)

        self.topframe.pack()


 
if __name__ == '__main__':
    app = App()

    app.mainloop()

