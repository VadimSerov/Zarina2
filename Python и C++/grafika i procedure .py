import tkinter
root=tkinter.Tk()

top_frame = tkinter.Frame(root)
top_frame.pack(side=tkinter.TOP)

bottom_frame = tkinter.Frame(root)
bottom_frame.pack(side=tkinter.BOTTOM)

button1 = tkinter.Button(top_frame,text="кнопка 2",fg="blue")
button2 = tkinter.Button(top_frame,text="кнопка 1",fg="red")
button3 = tkinter.Button(top_frame,text="кнопка 3",fg="yellow")
button4 = tkinter.Button(bottom_frame,text="кнопка 4",fg="green")

button1.pack()
button2.pack()
button3.pack()
button4.pack()

root.mainloop()
