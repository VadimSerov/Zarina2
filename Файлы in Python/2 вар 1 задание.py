if int(input("введите 1 если нужно ввести ДНК вручную "))==1 :
    nuc_bas=input("Введите азотистые основания ДНК ")
    file= open("DNA.txt",'w')
    file.write(nuc_bas)
    file.close()
# chek file for correctness
f_check=open("DNA.txt",'r')
check_bas=f_check.read()
f_check.close()
# check for parity the number of characters in the file
num_of_bas= len(check_bas)
if num_of_bas%2!=0 :
    print("Ваш файл не удовлетворяет условиям четности")
else :
    # creat set for checking
    set_checking= set("A TGC")
    for i in range (0,num_of_bas) :
        if not(check_bas[i] in set_checking) :
            print("Не то азотистое основание ",check_bas[i])
    trap = True
    k=0
    for i in range (0,num_of_bas-1,2) :
        if not(check_bas[i]+check_bas[i+1]=='AT' or check_bas[i]+check_bas[i+1]=="TA" or check_bas[i]+check_bas[i+1]=="CG" or check_bas[i]+check_bas[i+1]=="GC") :
            trap=False
            k=i
            break
    if not trap :
        print("Последовательности не комплементарны ",k//2+1,"пара, основание ",check_bas[i]+check_bas[i+1])
    else :
        print("Последовательности комплементарны ")
    # main task is chanch nukleotid bases
    file_change= open("DNA.txt",'r')
    nuc_base_change= file_change.read()
    file_change.close()
    nuc_base_change2=""
    for i in range (0,num_of_bas-1,2) :
        nuc_base_change2+=nuc_base_change[i+1]+nuc_base_change[i]
    print(nuc_base_change2)
    if int(input("Если нужно вывести последовательность в файл нажмите 1 ")) :
        file_out= open("DNA2.txt","w")
        file_out.write(nuc_base_change2)
        file_out.close()
        
        
    