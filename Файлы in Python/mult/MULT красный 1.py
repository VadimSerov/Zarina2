def fasta_to_dict(text):
    ch = []
    start = 0
    trap = True
    while trap:
        try:
            sind = text.index(">", start)+1
        except:
            trap = False
        eind = text.find("\n", start)
        start = eind+1
        ssind = text.find(">", start)
        if ssind == -1:
            ssind = len(text)
            trap = False
        if text[sind:eind].strip() != "":
            ch.append({"comment": text[sind:eind],
                       "chain": text[start:ssind-1]})
    return ch


chains = [{"comment": "Rosalind_7", "chain": "ATATCCG"},
          {"comment": "Rosalind_35", "chain": "TCCG"},
          {"comment": "Rosalind_23", "chain": "ATGTACTG"},
          {"comment": "Rosalind_44", "chain": "ATGTCTG"}]
#
if bool(int(input("введите 1 для чтения файла FASTA "))):
    fasta_file = open("rosalind.fasta", "r")
    chains = fasta_to_dict(fasta_file.read())
    fasta_file.close()
print(chains)
# выравнивание строк
# выберем самую длинную цепочку
max_of_len_chain = 0
for elem in chains:
    len_chain = len(elem["chain"])
    if len_chain > max_of_len_chain:
        max_of_len_chain = len_chain
        max_elem = elem
print(max_elem, chains.index(max_elem))
out_result = []
# У всех остальных искать совпаденя
for elem in chains:
    if elem != max_elem:
        print( elem )
        buf_chain = ""
        index_max = 0
        index_el = 0
        while index_max < len(max_elem["chain"]):
            print(max_elem["chain"][index_max],elem["chain"][index_el],index_max,index_el)
            if max_elem["chain"][index_max] == elem["chain"][index_el]:
                buf_chain += elem["chain"][index_el]
                index_el += 1
            else:
                buf_chain += "-"
            index_max += 1
        out_result.append(buf_chain)
print(out_result)
