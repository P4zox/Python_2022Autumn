from unicodedata import name


class Car:  #創立類別(藍圖)
    #建構式
    def __init__(self,color,seat):
        self.color=color
        self.seat=seat
    #方法
    def move(self,meter):
        print("My car moves "+str(meter)+" meters")
    def printAttritbute(self):
        print("My car's color is "+str(self.color))
        print("My car has "+str(self.seat)+" seats")


audi=Car("orange",2)
audi.move("infinity")   #呼叫方法
audi.printAttritbute()
# audi=Car()  #創立物件
#print(isinstance(audi,Car)) #判斷類別與物件的關係

# #建立屬性
# audi.color="orange"
# audi.seat=2

# #呼叫屬性
# print(audi.color)
# print(audi.seat)

class FullName:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def name_list(self):
        print("My name is "+self.first_name+", "+self.last_name)
name1=FullName("Andy","Wang")
name2=FullName("Lulu","Cheng")
name1.name_list()
name2.name_list()
# print(name1.first_name,name1.last_name,sep=" ")
# print(name2.first_name,name2.last_name,sep=" ")