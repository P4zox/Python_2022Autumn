from tkinter import *
root=Tk()
root.geometry('500x500+1200+200')
root.title("class5")

button1=Button(root, text="button1")
button2=Button(root, text="button2")
button3=Button(root, text="button3")
button4=Button(root, text="button4")
button5=Button(root, text="button5")

button1.pack()
button2.pack(side="left")
button3.pack(side="bottom")

root.mainloop()