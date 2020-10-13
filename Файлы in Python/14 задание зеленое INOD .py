#Topics: Combinatorics, Phylogeny
#Culling the Forest
 
#Дано: положительное целое число n (3≤n≤10000).

#Возврат: количество внутренних узлов любого необращенного двоичного дерева, имеющего n листьев.

#примем следующую модель
# одномерный массив из словарей
# элемент словаря parent - индекс родительского узла
# data - любые данные в этом узле (изначально - пустая строка)
# node0 - индекс "нулевой" ветки (другие названия: левая, ложная, отрицательная)
# node1 - индекс "первой" ветки ( правая, истинная, положительная)
#дополнительныё определения:
# - корень это узел, который не имеет входящих ветвей (элемент parent имеет значение None)
# - лист это узел, который не имеет исходящих ветвей ( элеметы node0 и node1 одновременно имеют значение None )
# - корень и листья это не внутренние узлы

import json
n=int(input("введите количество листьев двоичного дерева "))
tree=[]
if not(3<=n and n<=10000) :
	print("необходимое количество листьев не входит в допустимый диапазон ")
else :
	#на старте создать корень а на нем 2 листика	
	tree.append({"parent":None,"data":"","node0":None,"node1":None})	
	#текущий номер это самый крайний
	curent=len(tree)-1
	#добавить ветку
	tree.append({"parent":None,"data":"","node0":None,"node1":None})	
	curent=len(tree)-1
	tree[curent]["parent"]=0
	tree[0]["node0"]=curent
	#добавить ещё ветку
	tree.append({"parent":None,"data":"","node0":None,"node1":None})
	curent=len(tree)-1
	tree[curent]["parent"]=0
	tree[0]["node1"]=curent
	#в таком дереве два листа
	n_leaf=2
	#и пока ни одного внутреннего узла
	n_intro=0
#----------------------------------------------------------------
	#чтобы начать создавать следующий этаж дерева
	#до тех пор, пока количество листьев созданного дерева не совпадет с нужным количеством листьев
	while not(n_leaf==n) :
		i_start=len(tree)-1
		#найдём стартовую позицию (индекс узла с хотя бы одной незаполненной веткой)
		while i_start>0 :
			if (tree[i_start]["node0"] is None) and (tree[i_start]["node1"] is None) :
				i_start -=1
			else :
				break
		i_start +=1
		#print(tree,i_start)	#часть дерева перед добавлением двух узлов
		i=i_start
		#добавим лист (нулевая ветка)
		tree.append({"parent":None,"data":"","node0":None,"node1":None})
		curent=len(tree)-1
		tree[curent]["parent"]=i
		tree[i]["node0"]=curent
		n_intro +=1
		#один лист добавился, но и один лист превратился во внутренний узел
		#следовательно количество листьев не изменилось
		tree.append({"parent":None,"data":"","node0":None,"node1":None})
		curent=len(tree)-1
		tree[curent]["parent"]=i
		tree[i]["node1"]=curent
		n_leaf += 1
		#один лист добавился, но количество внутренних узлов не изменилось
#----------------------------------
	#print(tree) #полностью построенное дерево
	print("внутренних узлов ",n_intro)
	#print("общее количество узлов ",len(tree),"- 1","-",n," =",len(tree)-1-n) #Проверка результата
	if int(input("введите 1 еcли нужно записать дерево в файл в формате JSON "))==1 :
		file_json=open("TREE.txt","w")
		file_json.write(json.dumps(tree))
		file_json.close()
	#--------------------------------------- проверка зписи
		#file_pro = open("TREE.txt","r")
		#print(json.loads(file_pro.read()))
		#file_pro.close()
