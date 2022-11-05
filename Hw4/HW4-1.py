from tkinter import *
root=Tk()
root.geometry('400x400+150+200')
root.title("HW4-1")
Label(root,text="click for more num:)").pack()
a=1
def clicker():
    global a
    Label(root,text=a).pack()
    a+=1
mybutton=Button(root, text='click me!',command=clicker)
mybutton.pack()
root.mainloop()
