from tkinter import *
root=Tk()
root.geometry('500x500+1200+200')
root.title("class5")

button1=Button(root, text="button1")
button2=Button(root, text="button2")
button3=Button(root, text="button3")
button4=Button(root, text="button4")
button5=Button(root, text="button5")

button1.pack(fill="x")
button2.pack(side="left",fill="y",ipadx=30)
button3.pack(side="left")
button4.pack(side="right")
button5.pack()

root.mainloop()