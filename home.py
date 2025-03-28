import tkinter as tk
from tkinter import messagebox


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('Calculator')
        self.geometry('300x400')
    




if __name__ == '__main__':
    app = App()

    app.mainloop()
