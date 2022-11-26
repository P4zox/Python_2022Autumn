#引入 tkinter module
from tkinter import *

#建立主視窗 frame
root=Tk()

#設定視窗標題
root.geometry('400x400')
root.title("class6")

# #加入Frame框架
# frame=Frame(root)
# frame.pack()

# #將Label放在指定的Frame裡
# Label(frame,text="sussy baka").pack()

# frame1=Frame(root,pady=10,padx=2,bg='lightblue')
# frame2=Frame(root,pady=5,padx=10,bg='lightgreen')

# Label(frame1,text='second',width=10).pack(side='right')
# Label(frame2,text='first',width=10).pack(side='left')

# frame1.pack(side="right")
# frame2.pack(side="left")

#更改label文字內容
# Label(root,text="click for more num:)").pack()
# a=0
# def clicker():
#方法1
#     global a
#     a+=1
#     mylabel['text']='click'+str(a)
#方法2
#     global a
#     a+=1
#     mystringvar.set('click'+str(a))

# mybutton=Button(root, text='click me!',command=clicker)
# mybutton.pack()

# mystringvar=StringVar()
# mystringvar.set('click 0')


# # mylabel = Label(root,text='click 0')
# mylabel = Label(root,textvariable=mystringvar)
# mylabel.pack()

# # 方法1
# mylabel=Label(root,text='hello world')
# mylabel.pack()
# Label(root,text=mylabel['text']).pack

# 方法2
# mystringvar=StringVar()
# mystringvar.set('hello world')
# mylabel=Label(root,textvariable=mystringvar)
# mylabel.pack()
# Label(root,text=mystringvar.get()).pack()


mystringvar=StringVar()
mystringvar.set('hello world')
mylabel=Label(root,textvariable=mystringvar)
mylabel.pack()
def clicker():
    Label(root,text=mystringvar.get()).pack()
mybutton=Button(root, text='click me!',command=clicker)
mybutton.pack()
root.mainloop()








#執行主程式
root.mainloop()

