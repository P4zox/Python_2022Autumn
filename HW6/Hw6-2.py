from tkinter import *
root=Tk()
root.geometry('200x100')
root.title("HW5-3")
menu=Menu(root)
menubar1=Menu(menu,tearoff=0)
menubar2=Menu(menu,tearoff=0)

menubar1.add_command(label='aaa')
menubar1.add_command(label='bbb')


def close():
    root.destroy()

menubar2.add_command(label="open")
menubar2.add_command(label="execute")
menubar2.add_command(label="close",command=close)
menubar2.add_separator()

menubar2more=Menu(menubar2,tearoff=0)
menubar2more.add_command(label="x")
menubar2more.add_command(label="y")
menubar2.add_cascade(label="place",menu=menubar2more)
menu.add_cascade(label='File', menu=menubar2)
menu.add_cascade(label='Triple',menu=menubar1)

root.config(menu=menu)

root.mainloop()