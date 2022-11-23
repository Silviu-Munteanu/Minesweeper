from tkinter import *
def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
def play(root):
    clearFrame(root)
root=Tk()
root.title("Minesweeper")
root.geometry("1600x800")
n_text=Label(root,text="No. rows:",font=("Arial",30))
n_entry=Entry(root,font=("Arial",30))
n_text.place(x=500,y=200)
n_entry.place(x=700,y=200)
m_text=Label(root,text="No. columns:",font=("Arial",30))
m_entry=Entry(root,font=("Arial",30))
m_text.place(x=450,y=400)
m_entry.place(x=700,y=400)
start_button=Button(root,command=lambda : play(root),text="Play",font=("Arial",30))
start_button.place(x=700,y=500)
root.mainloop()