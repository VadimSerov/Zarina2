# Нужно создать одноцепочечную ДНК длиной next
import random 
n=int(input("Введите длину одноцепочечной ДНК (рекомендуется больше 300) "))
random.seed()
m_dna = ""
for i in range(0,n) :
	n_nitbase=random.randint(0,3)
	if n_nitbase==0 :
		c_nitbase="A"
	elif n_nitbase==1 :
		c_nitbase="T"
	elif n_nitbase==2 :
		c_nitbase="G" 
	else :
		c_nitbase="C" 
	m_dna += c_nitbase
#print(m_dna)
file_fasta=open("m_dna.fasta","w")
file_fasta.write(m_dna)
file_fasta.close()


