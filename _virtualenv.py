import math
#zad 1
print("zadanie 1")
wynik=math.pow(math.log(20,3)+math.sin(45)*5/8,4)
print(wynik)
#zad 2
print("zadanie 2")
lista=[1,2,3,4,5,6,7,8,9]
lista1=[lista[i] for i in range(1,len(lista),2) if lista[i]%2==0]
print(lista)
print(lista1)
print("zadanie 3")
#zad 3
lista2=[1,5,2,76,2,6,2,4,6,2,3,6]
def funkcja(lista2):
    if(len(lista2)%2==1):
        print("listy nie da sie utworzyc")
    else:
        lista3 = []
        a = len(lista2) - 1
        for i in range(len(lista2)):
            lista3.append(lista2[i] + lista2[a])
            a = a - 1
            if (a == i):
                break
    return lista2,lista3
print(funkcja(lista2))
#Zad 4
print("zadanie 4")
with open('tekst.txt','r',encoding='utf-8') as f:
    plik=f.read()
znaki=plik[46:95]
duze_znaki=0
male_znaki=0
for znak in znaki:
    if znak.isupper():
        duze_znaki=duze_znaki+1
    else:
        male_znaki=male_znaki+1
print("fragment tekstu: ",znaki)
print("Ilosc duzych liter: ",duze_znaki)
print("Ilosc malych liter: ",male_znaki)
#zad 5
print("zadanie 5")
a=input('podaj a')
b=input('podaj b')
c=input('podaj c')
try:
    a=int(a)
    b=int(b)
    c=int(c)
    wynik1=float((a/b)*(a/b)*(a/b)*math.sqrt(c))
    zapis=open("Zadanie5.txt","w")
    zapis.writelines(str(wynik1))
    zapis.close()
except ValueError:
    print("Niepoprawne wartosci")



