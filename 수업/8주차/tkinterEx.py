from tkinter import *

window = Tk()

l1 = Label(window, text = "화씨")
l2 = Label(window, text = "섭씨")
l1.pack()
l2.pack()

e1 = Entry(window)
e2 = Entry(window)
e1.pack()
e2.pack()

b1 = Button(window, text = "화씨 → 섭씨")
b2 = Button(window, text = "섭씨 → 화씨")
b2.pack()
b1.pack()

window.mainloop()
