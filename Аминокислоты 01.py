import json
#
filename=input("введите имя json файла для хранения названий и свойств аминокислот ")
#
inp = open(filename,"r")
amin_content = json.load(inp)
inp.close()
n_amin = len(amin_content)
#
print()
print("количество аминокислот в базе",n_amin,"Название в первой записи",amin_content[0]["name"])
print()
#
print("если хотите завершить программу введите 0")
print(" - добавить аминокислоты в файл хранения 1")
print(" - вывести аминокислоты в порядке увеличения молярой массы 2")
#
case_of = 1
while case_of != 0 :
	case_of = int(input("введите номер вашего выбора "))
	if case_of == 1 :	
		trap1 = 1
		while trap1 !=0 :
			trap1 = int(input("если хотите продолжить введите 1 иначе 0 "))
			if trap1==0 :
				break
			ami1 = input("введите трехбуквенное обозначение аминокислоты ")
			ru_name = input("введите русское название аминокислоты ")
			formula1 = input("введите упрощенную формулу аминокислоты ")
			weight1 = float(input("введите молярную массу аминокислоты "))
			buf1 = {"key":ami1,"name":ru_name,"ch_form":formula1,"weight":weight1}
			amin_content.append(buf1)
#			
	elif case_of == 2 :
#		цикл сортировки
		trap2 = True
		while trap2 :
			trap2 = False
			for i2 in range(1,len(amin_content)) :
				if amin_content[i2-1]["weight"] > amin_content[i2]["weight"] :
					buf2 = amin_content[i2-1]
					amin_content[i2-1] = amin_content[i2]
					amin_content[i2] = buf2
					trap2 = True
#   цикл вывода
		for i in range(0,len(amin_content)) :
			print(amin_content[i]["key"],amin_content[i]["name"],amin_content[i]["ch_form"],amin_content[i]["weight"])
#			
	elif case_of == 0 :
		out = open(filename,"w")
		json.dump(amin_content,out,ensure_ascii=False)
		out.close()
