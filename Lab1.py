import numbers
import re
#Găsiți cel mai mare divizor comun al mai multor numere citite de pe consolă.
def cmmdc(m,n):
    while m!=n:
        if m>n: m = m - n
        else: n = n - m
    return m
#Scrieți un script care calculează câte vocale sunt într-un șir.
def vocale (str):
    nr=0
    for index in str:
        if index in 'AEIOUaiou':
            nr=nr+1
    return nr
#Scrieți un script care primește două șiruri și imprimă numărul de apariții ale primului șir în al doilea.
def nraparitii(str1,str2):
    if len(str1) >= str2:
        if str2 in str1:
            count= count +1
# Scrieți un script care convertește un șir de caractere scris în UpperCamelCase în minuscule_cu_liniere de subliniere.

def LowerChar(str):
    return str.lower()

#Având în vedere o matrice pătrată de caractere, scrieți un script care imprimă șirul obținut prin parcurgerea matricei în ordine spirală:

def spiralOrder(matrix):
    # Numarul de linii
    m = len(matrix)
    # Numarul de coloane
    n = len(matrix[0])
    # Lista finala afisata in urma afisarii in spirala
    result = []
    # Verificam daca matricea este empty
    if m == 0:
        return result
    # Lista pentru a tine minte celulele vizitate
    seen = [[False] * n for _ in range(m)]
   # simularea celor patru directii: stanga, dreapta, sus si jos
    # Modificare index pentru a se deplasa
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    # Pozitia intiala a matricei
    r, c = 0, 0
    # Directia intiala a indexului (0 corespunde pentru 'right')
    di = 0
    # Parcurgem toate elementele matricei
    for i in range(m * n):
        # Adaugam in noua lista elementele
        result.append(matrix[r][c])
        # Verificam daca celula respectiva din matrice a fost vizitata
        seen[r][c] = True
        # Calculam pozitia urmatoarei celule in functie de directie
        newR, newC = r + dr[di], c + dc[di]
        # Verificam daca urmatoarea celue este in limite si nu a fost vizitata
        if 0 <= newR < m and 0 <= newC < n and not seen[newR][newC]:
            # Mutam la urmatoarea linie
            r, c = newR, newC
        else:
            # Schimbam directia in senzul acelor de ceas
            di = (di + 1) % 4
            # Mutam la urmatoare linie
            r += dr[di]
            # Mutam la urmatoarea coloana
            c += dc[di]
    # Returnam lista finala cu elementele citite in spirala din matrice
    return result

#Scrieți o funcție care extrage un număr dintr-un text (de exemplu, dacă textul este „Un măr este 123 USD”, această funcție va returna 123, sau dacă textul este „abc123abc”, funcția va extrage 123). Funcția va extrage doar primul număr găsit.

def FindNumber(str):
    numbers = []
    current_number = ""
    for char in string:
        if char.isdigit():
            current_number += char

        elif current_number:
            numbers.append(int(current_number))
            current_number = ""

    if current_number:
        numbers.append(int(current_number))
print(numbers)

# Scrieți o funcție care validează dacă un număr este un palindrom.

def Palindrom(number):
    false = 0
    true =1
    palindrom = 0
    oglindit = number
    while number > 0:
        dig= number%10
        palindrom = palindrom*10 + dig
        number=number//10 #operator pentru a scoate ultima cifra
    if oglindit == palindrom:
        return true
    else:
        return false
#Scrieți o funcție care numără câți biți cu valoarea 1 are un număr. De exemplu, pentru numărul 24, formatul binar este 00011000, adică 2 biți cu valoarea „1”

def numarBiti(number):
    count=0
    while number > 0:
        count += number & 1 # verifica ultimul bit al numarului, daca este unul creste count pentru a numara
        number >>= 1 # efectueaza o deplasare la dreapta a bitilor numarului, astfel incat bitul cel mai din dreapta este eliminat
    return count

# Scrieți o funcție care determină cea mai comună literă dintr-un șir. De exemplu, dacă șirul este „un măr nu este o roșie”, atunci cel mai comun caracter este „a” (de 4 ori). Trebuie luate în considerare numai literele (A-Z sau a-z). Carcasa nu trebuie considerată „A” și „a” reprezintă același caracter.



#Scrieți o funcție care numără câte cuvinte există într-un text. Un text este considerat a fi format din cuvinte care sunt separate printr-un singur spațiu. De exemplu: „Am examen Python” are 4 cuvinte.

def numarCuvinte(str):
    cuvinte= str.split()
    return len(cuvinte)


str = 'AbcAa31a2 sadsa  '
number = 24
print(numarCuvinte(str))
#print(vocale(str))
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
#esult = spiralOrder(matrix)
#print(result)
#FindNumber(str)
#m = int(input('m = '))
#n = int(input('n = '))

