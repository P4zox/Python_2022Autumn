from tkinter import *
root=Tk()
root.geometry('400x200')
root.title("HW5-3")
storename= Label(root,text='Kube Store')
productName= Label(root,text='戶外餐桌椅組')
productPrice=Label(root,text='$ 1200')
productNum=Label(root, text='0')
addbutton=Button(root,text="+")
minusbutton=Button(root,text='-')


storename.grid(row=0,column=1)
productName.grid(row=1,column=0)
productPrice.grid(row=2,column=0,sticky=W+E)
addbutton.grid(row=3,column=0)
productNum.grid(row=3,column=1,sticky=W)
minusbutton.grid(row=3,column=2,sticky=W)

root.mainloop()