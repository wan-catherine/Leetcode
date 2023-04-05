import tkinter as tk
from tkinter import *
from tkinter import messagebox


def disp_slogan():
    messagebox.showinfo("our message", "tkinter is easy to use")

root = tk.Tk()
slogan = Button(root, text='Hello', command=disp_slogan)
slogan.pack()

botton = Button(root, text='QUIT', fg='red', command=quit)
botton.pack()

root.mainloop()

