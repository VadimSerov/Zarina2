import random
random.seed()
n=int(input("введите разменость массива "))
a=[]
for i in range(0,n) :
    a.append(random.randint(0,100))
print(a)
k=int(input("введите целое число для проверки "))
aver=sum(a)
print(aver)