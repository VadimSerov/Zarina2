import json
filename= input("Введите имя json файла: ")
inp = open(filename,"r")
amin_content = json.load(inp)
inp.close()
len_amin= len(amin_content)
trap1 = True
while trap1 :
	trap1 = False
	for i2 in range(1,len_amin) :
		if amin_content[i2-1]["weight"] > amin_content[i2]["weight"] :
			#поменять местами аминокислоты 
			buf2 = amin_content[i2-1]
			amin_content[i2-1] = amin_content[i2]
			amin_content[i2] = buf2
			trap1 = True
print("Если хотите закончить нажмите Enter ")
key_amin="0"
while key_amin!="" :
	key_amin= input("Введите название аминокислоты: ")
	for i in range (0,len_amin):
		if amin_content [i]["key"]==key_amin:
			print(amin_content[i]["weight"])
	

