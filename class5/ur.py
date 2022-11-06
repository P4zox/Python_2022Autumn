import random as r
# while True:
#     for i in range(1,100):
#         for n in range(1,100):
#             print("%3d%2s%3d%2s%5d"%(i,"*",n,"=",i*n),end="                                     ")
#         print("")
score=1
time=1
a=":)"
while a!=619:
    i = r.randrange(1,101)
    n= r.randrange(1,101)
    print(time,".  ",i,"+",n,"= ?")
    a=int(input("ur answer(type 619 to stop): "))
    if a == int(i+n):
        print("True")
        score+=1
    else:
        print("False")
        score-=1
    time+=1
print("ur score=%d"%(score))
