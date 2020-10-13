import random
random.seed()
n=int(input("введите количество строк матрицы "))
m=int(input("введите количество столбцов матрицы "))
a=[]
for i in range(0,n) :
    buf=[]
    for j in range(0,m) :
        buf.append(random.randint(1,100))
    a.append(buf)
print(a)
mul=[]
for i in range(0,n) :
    mul.append(1)
    for j in range(0,m) :
        mul[i] *= a[i][j]
print(mul)
min_of_mul=min(mul)
print(min_of_mul)
