import pyautogui
import tkinter as tk
from tkinter.filedialog import *


root=tk.Tk()

canvas1=tk.Canvas(root,width=300,height=300)
canvas1.pack()


def screenShot():
    myscreenshot=pyautogui.screenshot()
    save_path=asksaveasfilename()
    myscreenshot.save(save_path+"screenshot.png")

myButton= tk.Button(text="take screenshot",command=screenShot,font=10)
canvas1.create_window(150,150,window=myButton)

root.mainloop()

