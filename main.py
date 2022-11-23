from tkinter import *
import numpy as np
def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
def buildGame(n,m):
    clearFrame(root)
    cells=[]
    for i in range(n):
        cells.append([])
        for j in range(m):
            cells[i].append(Button(root).place(relheight=1/n,relwidth=0.8/m,relx=j*0.8/n,rely=i*1/m))
def buildMenu():
    clearFrame(root)
    n = StringVar()
    m = StringVar()
    n_text = Label(root, text="No. rows:", font=("Arial", 30)).place(x=500, y=200)
    n_entry = Entry(root, textvariable=n, font=("Arial", 30)).place(x=700, y=200)
    m_text = Label(root, text="No. columns:", font=("Arial", 30)).place(x=450, y=400)
    m_entry = Entry(root, textvariable=m, font=("Arial", 30)).place(x=700, y=400)
    start_button = Button(root, command=lambda: play(n, m), text="Play", font=("Arial", 30))
    start_button.place(x=700, y=500)
    root.mainloop()
def play(n_text,m_text):
    n=n_text.get()
    m=m_text.get()
    for i in n:
        if i.isdigit() == False:
            return False
    for i in m:
        if i.isdigit() == False:
            return False
    n=int(n)
    m=int(m)
    buildGame(n,m)
global change
root = Tk()
root.title("Minesweeper")
root.geometry("1600x800")
buildMenu()