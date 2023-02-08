from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

def open():
    file = askopenfilename()
    if file != None:
        lines = file.read()
        text.insert('1.0', lines)
        file.close()

def save():
    file = asksaveasfilename(title = "파일 저장", filetypes = [('Plain text', '*.txt'), ('Any File', '*.*')])
    if file != None:
        lines = text.get('1.0', END+'-1c')
        file.write(lines)
        file.close

def exit():
    if messagebox.askokcancel("Quit", "종료하시겠습니까?"):
        window.destroy()

def about():
    label = messagebox.showinfo("About", "메모장 프로그램")

window = Tk()
text = Text(window, height=30, width=80)
text.pack()

menu = Menu(window)
window.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="파일", menu=filemenu)
filemenu.add_command(label="열기", command=open)
filemenu.add_command(label="저장하기", command=save)
filemenu.add_command(label="종료", command=exit)

helpmenu = Menu(menu)
menu.add_cascade(label="도움말", menu=helpmenu)
helpmenu.add_command(label="프로그램 정보", command=about)

window.mainloop()
