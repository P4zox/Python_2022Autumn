from tkinter import *
root=Tk()
root.geometry('200x100')
root.title("HW5-3")
productName= Label(root,text='三人坐沙發 綠色/灰色/黑色')
productPrice=Label(root,text='NT. 28,900')
productNum=Label(root, text='0')
addbutton=Button(root,text="+")
minusbutton=Button(root,text='-')

productName.pack(fill="x")
productPrice.pack(side="left",fill="y",ipadx=30)
addbutton.pack(side="right")
productNum.pack(side="right")
minusbutton.pack(side="right")

root.mainloop()