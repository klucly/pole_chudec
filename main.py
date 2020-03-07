from tkinter import *
from default_values import *
from tkinter import messagebox as mb

class Main():
    def __init__(self):
        self.score = score
        self.insert = insert
        self.symbols_len = symbols_len
        self.win = Tk()
        self.win.configure(bg = "#333333")
        self.win.geometry("350x370")
        self.win.title("Pole chudec (by klucly) - tk")
        self.win.resizable(0, 0)
        self.button_insert = Button(text = "insert word", bg = "#555555", fg = "#ffffff", font=("Comic Sans MS", 32, "bold"), command = self.on_start_button_vlick)
        self.insert_pole = Entry(width = 10, font=("Comic Sans MS", 32, "bold"))
        self.insert_pole1 = Entry(width = 1, font=("Comic Sans MS", 32, "bold"))
        self.button_insert_sym = Button(text = "insert symbol", bg = "#555555", fg = "#ffffff", font=("Comic Sans MS", 32, "bold"), command = self.on_sym_button_vlick)
        self.button_check = Button(text = "Open win again", bg = "#555555", fg = "#ffffff", font=("Comic Sans MS", 32, "bold"), command = self.check)
        self.button_insert.grid(row = 1, column = 0)
        self.insert_pole.grid(column = 0, row = 2)

        self.win.mainloop()

    def on_start_button_vlick(self):
        self.insert = self.insert_pole.get()
        self.button_insert.grid_forget()
        self.insert_pole.grid_forget()
        for i in range(len(self.insert)):
            self.symbol = self.LabelL(self.insert[i], text = "_", font=("Comic Sans MS", 48, "bold"), bg = "#8800ff")
            dir(self.symbol)
            self.symbols_len.append(self.symbol)
            self.symbol.grid(column = i, row = 0)

        self.insert_pole1.grid(column = 0, row = 1, columnspan = i+1)
        self.button_insert_sym.grid(column = 0, row = 2, columnspan = i+1)

        print(self.symbols_len)

    def on_sym_button_vlick(self):
        for i in self.insert:
            if self.insert_pole1.get() in self.insert and len(self.insert_pole1.get()) <= 1:
                if len(self.insert_pole1.get()) == 0:
                    pass
                else:
                    aka = self.symbols_len[self.insert.find(self.insert_pole1.get())]
                    if self.insert.find(self.insert_pole1.get()) == -1:
                        print("error")

                    try:
                        for aka in self.symbols_len:
                            if aka != None:
                                print(aka.symbol, self.insert_pole1.get(), self.insert)
                                if aka.symbol == " ":
                                    aka["text"] = " "
                                    self.score += 1
                                    self.symbols_len[self.symbols_len.index(aka)] = None

                                if aka.symbol == self.insert_pole1.get():
                                    aka["text"] = self.insert_pole1.get()
                                    self.score += 1
                                    self.symbols_len[self.symbols_len.index(aka)] = None
                                    print(self.symbols_len, self.insert)
                                    if self.score >= len(self.insert):
                                        self.check()
                                    break

                    except AttributeError:
                        print("AttributeError")
                        for i in self.symbols_len:
                            if i != None:
                                print(i.symbol)
                    
        else:
            print("Nooooo!")
        self.insert_pole1.delete(0, "end")

    def check(self):
        answer = mb.askyesno(title="Win", message="you win, go back?")
        if answer == True:
            obj_list = self.win.grid_slaves()
            for obj in obj_list:
                obj.grid_forget()
            self.button_insert.grid(row = 1, column = 0)
            self.insert_pole.grid(column = 0, row = 2)
            print(insert, obj_list, self.score)
            self.insert = ""
            self.symbols_len = []
            self.score = 0
        else:
            self.button_check.grid(row = 3, columnspan = 100)
            

    class LabelL(Label):
        def __init__(self, symb, master=None, cnf={}, **kw):
            self.symbol = symb
            super().__init__(master=None, cnf={}, **kw)

if __name__ == "__main__":
    Main()