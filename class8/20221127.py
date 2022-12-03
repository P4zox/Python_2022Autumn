from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root=Tk()
root.geometry('400x200')
root.title("Nope")
# 獲取button文字內容 way1
# 建立 計算按鈕次數 Label 標籤
# mybutton = Button(root, text='Hello World')
# mybutton.pack()
# get mylabel的文字內容
# Label(root,text=mybutton['text']).pack()


#建立StringVar way2
# mystringvar=StringVar()
# mystringvar.set('Hello World')
# # 建立 計算按鈕次數 Label 標籤
# mybutton=Button(root,textvariable=mystringvar)
# mybutton.pack()

# img=Image.open('C:/Users/halst/Downloads/corgi1.jpg')
# resized_image=img.resize((100,1000))
# tk_img=ImageTk.PhotoImage(resized_image)

# # Label(root,image=tk_img).pack()
# Button(root,image=tk_img).pack()

result=messagebox.askquestion('askquestion','Welcome this is a question:)\nR u fat:/')
print('user click'+result)
if result == "yes":
    messagebox.showinfo('showinfo','This site might be danger\nReason: cuz u r fat :](no capping)')
else:
    messagebox.showinfo('showinfo','Nice u r safe now\nunless u r fat:]')


root.mainloop()
