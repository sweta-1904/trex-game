from tkinter import *
from tkinter import filedialog

root=Tk()
root.geometry("500x600")
root.config(bg="gray")
frame = Frame(root)
frame.pack()


def save_file():
    open_file=filedialog.asksaveasfile(mode='w',  defaultextension=".txt") 
    if open_file is None:
         return
    text=str(entry.get(1.0 , END))
    open_file.write(text)
    open_file.close()
    
    
def clear_file():
    entry.delete(1.0, END)
    
def open_file():
    file=filedialog.askopenfile(mode='r', filetype=[('text files', '*.text')])
    if file is not None:
        content=file.read()
    entry.insert(INSERT, content )
    
    

b1=Button(root,  text="SAVE", command=save_file, bg="orange")
b1.place(x=10, y=10)

b2=Button(root,  text="CLEAR", command=clear_file, bg="white")
b2.place(x=70, y=10)

b3=Button(root,  text="OPEN", command=open_file, bg="green")
b3.place(x=150, y=10)

entry=Text(root, height=33, width=58, wrap=WORD)
entry.place(x=10, y=50)


root.mainloop()
