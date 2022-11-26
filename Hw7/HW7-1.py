from tkinter import *
root=Tk()
root.geometry('400x200')
root.title("HW5-3")
sum=0
a=0
def clicker():
# 方法2
    global a
    global sum
    a+=1
    mystringvar.set(str(a))
    sum+=1200
    mystringvar2.set(str(sum))
def clicker2():
# 方法2
    global a
    global sum
    mystringvar.set(str(a))
    a-=1
    if a<0:
        a=a+1
    sum-=1200
    if sum<0:
        sum=sum+1200

    mystringvar2.set("總額: $"+str(sum))


mystringvar=StringVar()
mystringvar.set('0')
mystringvar2=StringVar()
mystringvar2.set('總額: $0')

storename= Label(root,text='Kube Store')
productName= Label(root,text='戶外餐桌椅組')
productPrice=Label(root,text='$ 1200')
productNum=Label(root, textvariable=mystringvar)
addbutton=Button(root,text="+",command=clicker)
minusbutton=Button(root,text='-',command=clicker2)
totalproduct=Label(root,textvariable=mystringvar2)


storename.grid(row=0,column=0,columnspan=4,sticky=W+S+N+E)
productName.grid(row=1,column=0,columnspan=2,sticky=W)
productPrice.grid(row=2,column=0,sticky=W)
addbutton.grid(row=3,column=0,sticky=W)
productNum.grid(row=3,column=1,sticky=W)
minusbutton.grid(row=3,column=2,sticky=W)
totalproduct.grid(row=4,column=0,columnspan=4,sticky=W+S+N+E)

root.mainloop()