from tkinter import *
from tkinter import messagebox
root=Tk()
# new window

root.geometry('400x200')
root.title("HW5-3")
from PIL import Image, ImageTk
# def createNew():
#     # create new window
#     newWin=Toplevel(root)
#     # create new label in new wiindow
#     mylabel=Label(newWin,text="New Window")
#     mylabel.pack()
#     # create new button in new window
#     mybutton=Button(newWin,text='quit',command=newWin.destroy)
#     mybutton.pack()
#     mybutton1=Button(newWin,text='hide',command=root.iconify)
#     mybutton1.pack()
#     mybutton2=Button(newWin,text='show',command=root.deiconify)
#     mybutton2.pack()
#     mybutton3=Button(newWin,text='Withdraw Main Window',command=root.withdraw)
#     mybutton3.pack()
#     mybutton4=Button(newWin,text="Quit Main Window",command=root.destroy)

#     newWin.mainloop()
# create=Button(root,text="click to create new window!",command=createNew)
# create.pack()

# # # create a string varible
# # val=StringVar()
# # #create a radiobutton
# # radiobtn1=Radiobutton(root,text="Black",variable=val,value='Black')
# # radiobtn1.pack()
# # # select a varible
# # radiobtn1.select()
# # #create another radiobutton
# # radiobtn2=Radiobutton(root,text='Red',variable=val,value="Red")
# # radiobtn2.pack()
# # create a string varible
# # can change color
# def blue():
#     selectlabel['fg']='Blue'
#     selectlabel['textvariable']=val
# def green():
#     selectlabel['fg']='Green'
#     selectlabel['textvariable']=val
# def pink():
#     selectlabel['fg']='Pink'
#     selectlabel['textvariable']=val
# val=StringVar()
# Label(root,text="Please select a color").pack()
# #create a radiobutton
# radiobtn1=Radiobutton(root,text="Blue",variable=val,value='Blue',foreground="Blue",command=blue)

# radiobtn1.pack()

# # select a varible
# radiobtn1.select()
# #create another radiobutton
# radiobtn2=Radiobutton(root,text='Green',variable=val,value="Green",foreground="Green",command=green)

# radiobtn2.pack()
# radiobtn3=Radiobutton(root,text="Pink",variable=val,value="Pink",foreground="Pink",command=pink)

# radiobtn3.pack()
# # show the value using label
# selectlabel=Label(root,textvariable='',font=("Ariel",30))
# selectlabel.pack()

# def function(n,*arg):
#     print(n)
#     print(arg)
# # call function and give multiple number tto the function, except 1 aka n, the others  are *args' value
# function(1,2,3,4,5,6)

# def function(*arg,**kwargs):
#     print(kwargs)
#     print(arg)
# # call function and give multiple number to the funnction, the first 4 numbers in *arg, and the dict numbers are for kwargs 
# function(1,2,3,4,num1=5,num2=10)

def createNew():
    newWin=Toplevel(root)
    mylabel=Label(newWin,text="New Window")
    mylabel.pack()
    def blue():
        selectlabel['fg']='Blue'
        selectlabel['textvariable']=val
    def green():
        selectlabel['fg']='Green'
        selectlabel['textvariable']=val
    val=StringVar()
    Label(newWin,text="Please select a color").pack()
#     #create a radiobutton
    radiobtn1=Radiobutton(newWin,text="Blue",variable=val,value='Blue',foreground="Blue",command=blue)

    radiobtn1.pack()

#     # # select a varible
    radiobtn1.select()
#     # create another radiobutton
    radiobtn2=Radiobutton(newWin,text='Green',variable=val,value="Green",foreground="Green",command=green)

    radiobtn2.pack()
    selectlabel=Label(newWin,textvariable='',font=("Ariel",30))
    selectlabel.pack()
    mybutton=Button(newWin,text='quit',command=newWin.destroy)
    mybutton.pack()
    newWin.mainloop()

create=Button(root,text="start",command=createNew)
create.pack()

root.mainloop()
# a=0
# def function(n,*arg,**kwarg):
#     global a
#     for i in arg:
#         a+=i
#     for j in kwarg.values():
#         a+=j
#     print(n)
#     print(a)
# function(6,4,3,2,1,n1=10,n2=20)
