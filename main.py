import math
import random
#zad1
liczby=random.sample(range(0,31),31)
print(liczby)
for i in range(0,len(liczby)):
    liczby[i]=liczby[i]*2
print(liczby)
plik=open("dane.txt","a+")
plik.writelines(str(liczby))
#zad2
plik=open("dane.txt","r")
wiersze=plik.readlines()
plik.close()
print(wiersze)
#zad3
with open("dane.txt","w") as plik:
    plik.write("a\n")
    plik.write("b\n")
    plik.write("c\n")
plik=open("dane.txt","r")
print(plik.read())
#zad4
class NaZakupy:
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jed=cena_jed
    def wyswietl_produkt(self):
        print(self.nazwa_produktu)
        print(self.ilosc)
        print(self.jednostka_miary)
        print(self.cena_jed)
    def ile_produktu(self):
        print(self.ilosc)
        print(self.jednostka_miary)
    def ile_kosztuje(self):
        print(self.cena_jed*self.ilosc)
obiekt = NaZakupy("Sok",3,"litry",1.5)
print(obiekt.ile_kosztuje())
#zad5
#class ciagi:
    #def __init__(self):

#zad6
class robak:
    def __init__(self,x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok
    def idz_w_gore(self,ile_krokow):
        self.y=self.y+(self.krok*ile_krokow)
    def idz_w_dol(self, ile_krokow):
        self.y=self.y-(self.krok*ile_krokow)
    def idz_w_lewo(self, ile_krokow):
        self.x=self.x-(self.krok*ile_krokow)
    def idz_w_prawo(self, ile_krokow):
        self.x=self.x+(self.krok*ile_krokow)
    def pokaz_gdzie_jestes(self):
        print(self.x,self.y)

robaczek=robak(0,0,2)
robaczek.idz_w_prawo(2)
robaczek.idz_w_gore(5)
robaczek.idz_w_lewo(4)
robaczek.idz_w_dol(3)
robaczek.pokaz_gdzie_jestes()