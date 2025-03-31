import tkinter as tk
from tkinter import messagebox


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        

        self.title('Calculator')
        self.geometry('300x415')
        self.resizable(0, 0)

        self.update_idletasks()

        self.window_width = self.winfo_width()

        self.window_height = self.winfo_height()


        self.create_widgets()


    def create_widgets(self):
        

        self.buttons = ["x", "x", "x", "x",
                        "7", "8", "9", "*",                        
                        "6", "5", "4", "-",
                        "3", "2", "1", "+",
                        "+/-", "0",".",'=']

        self.topframe = tk.Frame(self, bg='gray',width= self.window_width, height=self.window_height // 2)
        self.topframe.pack()

        self.bottomframe = tk.Frame(self, bg = 'blue', width = self.window_width, height=self.window_height)
        self.bottomframe.pack()



        for index, button in enumerate(self.buttons):
            row, col = divmod(index, 4)
            
            if button in self.buttons[0:4]:
                btn = tk.Button(self.bottomframe, text= button, width= 7, height=1,
                        command= lambda b = button: self.button_on_click(b))
            else:

                btn = tk.Button(self.bottomframe, text= button, width= 7, height=2,
                            command= lambda b = button: self.button_on_click(b))

            btn.grid(row = row, column = col, padx = 1, pady= 1)
            

    def button_on_click(self, value):

        if value == '+/-':
            value = '-'
            print(f"Button {value} has been clicked")
        
        else:
            print(f"Button {value} has been clicked")



if __name__ == '__main__':
    app = App()

    app.mainloop()

