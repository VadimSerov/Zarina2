# Из данного файла формата фаста создать еще 9 файлов с мутациями
import random
random.seed()
#
def rn_nit_base() :
	n_nitbase=random.randint(0,3)
	if n_nitbase == 0 :
		c_nitbase="A"
	elif n_nitbase == 1 :
		c_nitbase="T"
	elif n_nitbase == 2 :
		c_nitbase="G" 
	else :
		c_nitbase="C"
	return c_nitbase
#
file_name= input("Введите название файла с расширением fasta ")
files = []
files.append(open(file_name+".fasta","r"))
dna = []
dna.append(files[0].read())
len_parent=len(dna[0])
files[0].close()
max_mut = len_parent//50
# Мутация методом замены
n_mut = int(input('Введите количество замен в каждой цепочке (рекомендуется не больше '+str(max_mut)+' ) '))
# Создать еще 9 мутированных цепочек ДНК 
segment = len_parent//n_mut
proxy_parent = 0
for i in range(1,9) :
	mut_place = random.randint(0,segment)
	dna_buf = ""
	for j in range(0,len_parent) :
		if(j==mut_place) :
			dna_buf += rn_nit_base()
			mut_place += random.randint(1,segment)
		else :
			dna_buf += dna[proxy_parent][j]
	dna.append(dna_buf)
	proxy_parent = random.randint(0,len(dna)-1)
	#print("мутирующая цепочка: ",len(dna)," родитель: ",proxy_parent)
#	
for i in range(0,9) :
	print("['"+dna[i]+"']")

if 1 == int(input("Введите 1 если нужно создать ещё девять файлов с мутировавшими цепочками днк ")) :
	for i_m in range(1,9) :
		files.append(open(file_name+str(i_m).strip()+".fasta","w"))
		files[i_m].write(dna[i_m])
		files[i_m].close()
