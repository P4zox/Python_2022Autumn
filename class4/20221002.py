from tkinter import *
root=Tk()
root.geometry('600x400+150+200')
root.title("class4")
#Label(root, text='hello world').pack()
#Label(root, text='second world', bg="lightgreen", fg="lightblue").pack(pady=20)
Label(root, text='2022/10/02', fg='blue',bg='pink',font=('Arial',16,'bold')).pack()
Label(root,text='Sunday',fg='blue',bg='pink',font=('Georgia',20,'italic')).pack(pady=50)

def clicker():
    Label(root,text='Y u click me, nothin will happen >:)').pack()
def ifGetText():
    Label(root,text="hi "+name.get()).pack()
Label(root,text="enter ur name").pack()
name=Entry(root,font=('Impact',20))
name.pack()
mybutton2=Button(root,text="enter",command=ifGetText)
mybutton=Button(root, text='Don\'t click me!',command=clicker)
mybutton.pack()
mybutton2.pack()


root.mainloop()
