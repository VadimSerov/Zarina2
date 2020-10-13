from tkinter import Tk, Canvas, Frame, BOTH
 
class Example(Frame):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.master.title("Рисуем круг")
        self.pack(fill=BOTH, expand=1)
 
        canvas = Canvas(self)
 
        # круг.
        canvas.create_oval(
            50, 50, 150, 150, outline="#f11",
            fill="#fff", width=2
        )
 
        canvas.pack(fill=BOTH, expand=1)
 
 
def main():
    root = Tk()
    ex = Example()
    root.geometry("330x220+300+300")
    root.mainloop()
 
 
if __name__ == '__main__':
    main()
