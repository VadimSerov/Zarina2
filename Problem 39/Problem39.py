p=int(input("введите периметр прямоугольного треугольника "))
if p<1000:
	tri = []
	a=1
	while a<p-2:
		b=1
		while b<p-a:
			c=p-a-b
			if a*a+b*b==c*c:
				tri.append([a,b,c])
			b+=1
		a+=1
	if len(tri)>0:
		print(tri)
	else:
		print("целочисленного решения нет ")
else:
	print("периметр слишком велик ")
