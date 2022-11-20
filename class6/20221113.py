#引入 tkinter module
from tkinter import *

#建立主視窗 frame
root=Tk()

#設定視窗標題
root.geometry('400x400')
root.title("class6")

#建立主選單
menu=Menu(root)


#anchor=元件在容器中錨定位置:E,W,S,N,CENTER(預設),NE,SE,SW,NW

# mybutton1=Button(root,text='東').pack(anchor=E)
# mybutton2=Button(root,text='西').pack(anchor=W)
# mybutton3=Button(root,text='南').pack(anchor=S)
# mybutton4=Button(root,text='北').pack(anchor=N)
# mybutton5=Button(root,text='東南').pack(anchor=SE)
# mybutton6=Button(root,text='西北').pack(anchor=NW)

#row=列索引
#cloumn=行索引
#rowspan=儲存格合併列數
#columnspan=儲存格合併行數

# mybutton1=Button(root,text='button1').grid(row=0,column=0)
# mybutton2=Button(root,text='button2').grid(row=0,column=1)
# mybutton3=Button(root,text='button3').grid(row=0,column=2)
# mybutton4=Button(root,text='button4').grid(row=1,column=0,columnspan=2)
# mybutton5=Button(root,text='button5').grid(row=1,column=2)
#button6=Button(root,text='button6').grid(row=2,column=1)
#sticky=元件於網格中的錨定位置:E,W,S,N

# mybutton1=Button(root,text='button1').grid(row=0,column=0)
# mybutton2=Button(root,text='button2').grid(row=0,column=1)
# mybutton3=Button(root,text='button3').grid(row=0,column=2)
# mybutton4=Button(root,text='button4').grid(row=1,column=0,columnspan=2, sticky=W+E)



# width=Label(root,text='Width ')
# height=Label(root,text='Height ')
# entry1=Entry(root,font=('Arial',18))
# entry2=Entry(root,font=('Arial',18))
# Result=Button(root,text='result')

# width.grid(row=0,column=0)
# entry1.grid(row=0,column=1)
# height.grid(row=1,column=0)
# entry2.grid(row=1,column=1)
# Result.grid(row=0,column=2,columnspan=2,rowspan=2,stick=W+E+N+S)

#建立子選單，選單綁定 menubar 主選單(tearoff=0)
# menubar1=Menu(menu,tearoff=0)

# #子選單項目
# menubar1.add_command(label="Open")
# menubar1.add_command(label="Save")
# menubar1.add_command(label="Exit")

# #建立主選單，內容為子選單
# menu.add_cascade(label="file",menu=menubar1)


# menubar2=Menu(menu,tearoff=0)
# menubar2.add_command(label="a")
# menubar2.add_command(label="b")
# menubar2.add_command(label="c")
# menubar2.add_separator()

# menubar2more=Menu(menubar2,tearoff=0)
# menubar2more.add_command(label="x")
# menubar2more.add_command(label="y")
# menubar2more.add_command(label="z")
# menubar2.add_cascade(label="file",menu=menubar2more)
# menu.add_cascade(label='Test', menu=menubar2)

def open(): Label(root,text='you open a file').pack()
def save(): Label(root,text='the file has been saved').pack()
def exit():
    print('exit')
    root.destroy()

menubar1=Menu(menu,tearoff=0)

#子選單項目
menubar1.add_command(label="Open",command=open)
menubar1.add_command(label="Save",command=save)
menubar1.add_command(label="Exit",command=exit)

#建立主選單，內容為子選單
menu.add_cascade(label="file",menu=menubar1)

# #主視窗加入主選單
root.config(menu=menu)

#執行程式
root.mainloop()