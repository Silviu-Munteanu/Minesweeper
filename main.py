import random
from tkinter import *
import math
import numpy as np
def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
global in_menu,in_game,n,m,rectangle_center,cells,first_click,no_bombs,bombs,marked
def generate_random(i,j):
    available=[t for t in range(n*m) if t!=i*m+j]
    bombs=[]
    for i in range(no_bombs):
        r_index=random.randint(0,len(available)-1)
        next_bomb=available[r_index]
        available.remove(available[r_index])
        bombs.append((next_bomb//m,next_bomb%m))
    return bombs
def check_neighbors(i,j):
    global bombs
    no_n=0
    print(bombs)
    for k in range(-1,2,1):
        for p in range(-1,2,1):
            if i+k<n and j+p<m and i+k>=0 and j+p>=0:
                if bombs[i+k,j+p] == 1 and (k!=0 or p!=0):
                    print(i,j,":",i+k,j+p)
                    no_n+=1
    return no_n
def mark(event):
    global marked
    if in_game == 1:
        abs_x = root.winfo_pointerx() - root.winfo_rootx()
        abs_y = root.winfo_pointery() - root.winfo_rooty()
        if abs_y < 800 and abs_x < 0.8 * 1600:
            i = int(abs_y / 800 * n)
            j = int(abs_x / (0.8 * 1600) * m)
            if revealed[i,j] == 0:
                marked[i,j]=1-marked[i,j]
                if marked[i,j] == 1:
                    cells[i][j] = Button(root, background='yellow').place(relheight=1 / n, relwidth=0.8 / m, relx=j * 0.8 / m,rely=i * 1 / n)
                else:
                    cells[i][j] = Button(root, background='white').place(relheight=1 / n, relwidth=0.8 / m,relx=j * 0.8 / m, rely=i * 1 / n)
def reveal_cell(i,j):
    if bombs[i,j] == 1:
        cells[i][j] = Button(root, background='red').place(relheight=1 / n, relwidth=0.8 / m, relx=j * 0.8 / m,rely=i * 1 / n)
    else:
        cells[i][j] = Button(root, text=str(check_neighbors(i,j))).place(relheight=1 / n, relwidth=0.8 / m, relx=j * 0.8 / m,rely=i * 1 / n)
def reveal(event):
    global n,m,rectangle_center,cells,first_click,bombs,marked,revealed
    if in_game==1:
        abs_x= root.winfo_pointerx() - root.winfo_rootx()
        abs_y= root.winfo_pointery() - root.winfo_rooty()
        if abs_y <800 and abs_x<0.8 * 1600:
            i=int(abs_y/800*n)
            j=int(abs_x/(0.8*1600)*m)
            if first_click!=1 and marked[i,j] == 0:
                index_bombs=generate_random(i,j)
                bombs=np.zeros((n,m))
                for k in index_bombs:
                    bombs[k[0],k[1]]=1
                first_click=1
                cells[i][j]=Button(root,text=str(check_neighbors(i,j))).place(relheight=1/n,relwidth=0.8/m,relx=j*0.8/m,rely=i*1/n)
                revealed[i,j]=1
            else:
                if bombs[i,j] == 1:
                    print("Game over!")
                    cells[i][j] = Button(root,background='red').place(relheight=1 / n, relwidth=0.8 / m,relx=j * 0.8 / m, rely=i * 1 / n)
                    revealed[i, j] = 1
                    for i in range(n):
                        for j in range(m):
                            reveal_cell(i,j)
                else:
                    if marked[i,j] == 0:
                        cells[i][j]=Button(root,text=str(check_neighbors(i,j))).place(relheight=1/n,relwidth=0.8/m,relx=j*0.8/m,rely=i*1/n)
                        revealed[i, j] = 1
def buildGame(n,m):
    rectangle_center=[]
    global in_menu,in_game,cells,marked,revealed
    marked=np.zeros((n,m))
    revealed=np.zeros((n,m))
    in_menu=0
    in_game=1
    clearFrame(root)
    canvas=Canvas(root,width=0.8 * 1600,height=800)
    canvas.place(x=0,y=0)
    cells=[]
    for i in range(n):
       cells.append([])
       for j in range(m):
           cells[i].append(Button(root).place(relheight=1/n,relwidth=0.8/m,relx=j*0.8/m,rely=i*1/n))
def buildMenu():
    global in_menu,in_game,n,m
    in_menu=1
    in_game=0
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
    global n,m
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
no_bombs=2
first_click=0
root = Tk()
root.title("Minesweeper")
root.geometry("1600x800")
root.bind("<Button-1>",reveal)
root.bind("<Button-3>",mark)
buildMenu()
