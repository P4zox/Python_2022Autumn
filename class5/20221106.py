from tkinter import *
root=Tk()
root.geometry('500x500+1200+200')
root.title("class5")

#side = 排列方向:TOP(預設), BOTTOM, LEFT, RIGHT

my咖ㄘㄥ1=Button(root, text="左")
my咖ㄘㄥ2=Button(root, text="右")
# my咖ㄘㄥ3=Button(root, text="右右")

# my咖ㄘㄥ1.pack(side="left")
# my咖ㄘㄥ2.pack(side="right")
# my咖ㄘㄥ3.pack(side="right")

#fill = 填滿所分配空間之方向:NONE(預設),X,Y,BOTH

# my咖ㄘㄥ1.pack(fill="x")
# my咖ㄘㄥ2.pack(side="right",fill="y")

#expand = 填滿容器:True/False(預設)

# my咖ㄘㄥ1=Button(root, text="expand=0")
# my咖ㄘㄥ1.pack(fill="both",expand=0)
# my咖ㄘㄥ2=Button(root, text="expand=1")
# my咖ㄘㄥ2.pack(fill="both",expand=1)

#padx / pady = 元件邊框與容器之距離(px,預設=0)

# my咖ㄘㄥ1.pack(side="left",padx=200)
# my咖ㄘㄥ2.pack(side="right",padx=20)

#ipadx / ipady = 元件內容(文字/圖像)與其邊框之距離(px, 預設=0)

# my咖ㄘㄥ1.pack(side="left",ipadx=30)
# my咖ㄘㄥ2.pack(side="right",ipady=30)

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