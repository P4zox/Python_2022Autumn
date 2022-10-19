class People:
    def __init__(self,height,weight,age,name):
        self.height=height
        self.weight=weight
        self.age=age
        self.name=name
    def family(self):
        print("My "+self.name+" is "+str(self.height)+"cm, "+str(self.weight)+"kg, "+str(self.age)+" years old")
    
name1=People(157,48,43,"Mom")
name2=People(178,120,41,"Dad")
name1.family()
name2.family()