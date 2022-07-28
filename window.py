from tkinter import *
import os
dic = open('dict.txt', 'r')
dic = dic.read()
dic = dic.split()

def install(d):
    for lis in d:
        str(lis)
        os.system('pip install ' + lis)
tk = Tk()
lbl = Label(tk, text = 'You must install...')
lbl.pack()
tk.title('установка библиотек')
listbox = Listbox(tk)
listbox.pack()
btn = Button(tk, text = 'install all now', command = install(dic))
btn.pack()
tk.resizable(0, 0)

tk.overrideredirect(1)
tk.lift()
tk.attributes('-topmost',True)
tk.after_idle(tk.attributes,'-topmost',True)
    
for i in dic:
    listbox.insert(0, i)
tk.mainloop()


