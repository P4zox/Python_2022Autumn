from tkinter import *
import datetime as d
today=d.date.today()
root=Tk()
root.geometry('400x400+150+200')
root.title("HW4-2")
birth=Entry(root,font=('Arial',18))
Label(root,text="Enter ur birth day(yyyy/mm/dd): ").pack()
def clicker():
    birth_1=birth.get().split("/")
    year = today.year - int(birth_1[0])           
    month = today.month - int(birth_1[1])
    if month<0:                                      
        year = year - 1                             
        month = 12 + month                            
    day_list = [31,28,31,30,31,30,31,31,30,31,30,31]  
    day = today.day - int(birth_1[2])                
    if day<0:                                         
        month = month - 1                             
    if month<0:                                   
        year = year - 1                           
        month = 12 + month                        
    day = day_list[month] + day       

    Label(root,text=f"{year} years old, {month} months, {day} days.").pack()
    

mybutton2=Button(root,text="enter",command=clicker)

birth.pack()
mybutton2.pack()
root.mainloop()


# 1. 現在的時間 > 出生的時間(月與日)
#年份差 * 365 + (現在月日 - 出生月日)
#2.  現在的時間 < 出生的時間(月與日) 
#年份差 * 365 + (出生月日 - 現在月日)