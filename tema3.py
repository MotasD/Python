# 1. Avem u cuvant ca input si vreau sa il oglinditi
def oglindit(s):
    str = ""
    for i in s:
        str = i + str
    print(str)

# 2. Avem o lista de numere naturale consecutive de la 0 la n din care lipseste un singur numar.
# Vreau sa stiu care e numarul ala. De exemplu pentru 1, 2, 4 avem 3 care lipseste.

def consecutive(lista):
    i = 1
    for index in lista:
        if i < len(lista) and lista[i] - lista[i-1] != 1:
            print(lista[i]-1)
        i += 1

#3. Avem o lista de numere ca input unde toate elementele au un duplicat mai putin un element.
# Vreau sa imi spuneti care element nu are duplicat.

def elemente_dif(lista1,lista2):
    lista3 = []
    for element in lista1:
        if element not in lista2:
            lista3.append(element)
    print(lista3)

def element_unic(lista):
    newlist = []
    duplist = []
    for i in lista:
        if i not in newlist:
            newlist.append(i)
        else:
            duplist.append(i)
    return elemente_dif(newlist,duplist)


#4. Avem o lista de numere ca input, vreau sa imi spuneti suma elementelor care au cel putin un duplicat in lista.

def suma_duplicate(lista):
    sum=0
    newlist = []
    duplist = []
    for i in lista:
        if i not in newlist:
            newlist.append(i)
        else:
            duplist.append(i)
    set_res = set(duplist)
    list_res = (list(set_res))
    for index in range(len(list_res)):
        sum=sum+duplist[index]
    print(sum)


#5. Avem o lista de numere ca input, vreau sa imi listati toate numerele care isi au perechea in lista.
# Spunem ca un numar are o pereche daca diferenta lui fata de 10 e si el in lista.
# De exemplu daca avem 4, 5, 8, 2, 3, 6 avem 4 (pentru ca avem 6), 8 pentru ca avem 2, 6 pentru ca avem 4, 2 pentru ca avem 8 etc.

def pereche(lista):
    for index in range(len(lista)):
        dif = 10 - lista[index]
        if dif in lista:
            print(lista[index])

#6. Avem 2 numere ca input si o lista de stringuri. Vreau sa faceti swap pentru cele 2 numere la cuvintele de pe pozitiile respective.
# De exemplu daca avem  1 si 3 si lista "ma", "aici", "e", "ta" rezultatul va fi "ma, "ta", "e", "aici".

def swap(list, poz1, poz2):
    #list[poz1]= list[poz1]
    #list[poz2]=list[poz1]
    list[poz1], list[poz2] = list[poz2], list[poz1]
    print(list)

#7. Avem o lista de numere pozitive si negative, vreau sa imi dati spuneti suma celei mai lungi subliste de numere.
# De exemplu pentru -2, -3, 4, -1, -2, 1, 5, -3 avem 7 ca avem de la 4, -1, -2, 1, 5 suma 7.

def suma_secventa(lst):
    s_sum = list()
    r_sum = list()
    for i in range(len(lst)):
        s_sum = list()
        s_sum.append(lst[i])
        k = 1
        for j in range(i+1,len(lst)):
            s_sum.append(s_sum[k-1] + lst[j])
            k+=1
        r_sum.append(max(s_sum))
    sum = max(r_sum)
    if  sum < 0:
        sum = 0
    print(sum)
