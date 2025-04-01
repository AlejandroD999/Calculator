import tkinter as tk
from tkinter import messagebox


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        

        self.title('Calculator')
        self.geometry('275x415')
        self.resizable(0, 0)
        self.config(bg='#16182C')
        self.update_idletasks()

        self.window_width = self.winfo_width()

        self.window_height = self.winfo_height()


        self.create_widgets()


    def create_widgets(self):

        self.buttons = ["(", ")", "C", "/",
                        "7", "8", "9", "*",                        
                        "6", "5", "4", "-",
                        "3", "2", "1", "+",
                        "+/-", "0",".",'=']

        self.topframe = tk.Frame(self, bg='#060270',width= self.window_width, height=self.window_height // 2,
                                 )
        self.topframe.propagate(False)
        self.topframe.pack()

        self.displayframe = tk.Frame(self.topframe, bg='#595865', width= 245, height= 70,
                                     borderwidth=2, relief='sunken')
        self.displayframe.propagate(False)
        self.displayframe.place(x=13, y=30)

        self.bottomframe = tk.Frame(self, bg = '#323450', padx=14, pady=7,
                                    width = self.window_width,
                                    height=self.window_height)
        self.bottomframe.propagate(False)
        self.bottomframe.pack()



        for index, button in enumerate(self.buttons):
            row, col = divmod(index, 4)
            
            #Top four buttons / top row
            if button in self.buttons[0:4]:
                btn = tk.Button(self.bottomframe, text= button, width= 7, height=0)
                btn.bind("<Button-1>", self.button_on_click)
            else:

                btn = tk.Button(self.bottomframe, text= button, width= 7, height=2)
                btn.bind("<Button-1>", self.button_on_click)           

            btn.grid(row = row , column = col, padx = 1, pady= 0.5)
        
        self.display_var = tk.StringVar()
        self.display_var.set("")

        self.display_label = tk.Label(self.displayframe, textvariable=self.display_var, width=35, height=5,
                                      font=('Arial', 12, 'bold'),
                                      bg='#595865')
        self.display_label.pack(anchor='e')

    def button_on_click(self, value):
        operations = ["+", '-', '/', '*']
        text = value.widget.cget("text")
        display_data = self.display_var.get()

        if text == '+/-':
            text = '-'

        elif  text == '=':
            try:
                solution = eval(display_data)

                self.display_var.set(solution)
                


            except Exception as e:
                self.display_var.set("Error!")
        
        elif text == 'C':
            self.display_var.set("")


        else:
            self.display_var.set(display_data + text)
                        
        

        



if __name__ == '__main__':
    app = App()

    app.mainloop()

