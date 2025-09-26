import tkinter


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.labe1 = tkinter.Label(self.main_window, text="Witaj Świecie")
        self.labe2 = tkinter.Label(self.main_window, text="Witaj Świecie")
        self.labe3 = tkinter.Label(self.main_window, text="Witaj Świecie")
        self.labe4 = tkinter.Label(self.main_window, text="Witaj Świecie")

        self.labe1.pack(side="left")
        self.labe2.pack(side="right")
        self.labe3.pack(side="top")
        self.labe4.pack(side="bottom")
        tkinter.mainloop()


my_gui = MyGui()
