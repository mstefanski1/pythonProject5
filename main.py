import numpy as np
#zad 1
a = np.array([2, 2, 5])
b = np.array([1, 3, 8])
print(a)
print(b)
c=np.dot(a,b)
print(c)
#zad 2
d=np.array([[1,2,3],[4,5,6],[7,8,9]])
e=np.array([[1,2,3,7],[4,5,6,2],[6,7,8,9],[7,5,2,7]])
print(d)
print(e)
print(d.min(axis=1))
print(e.min(axis=1))
print(d.min(axis=0))
print(e.min(axis=0))
#zad3
f=a*b
print(f)
#zad4
g = np.array([2, 2, 5])
h = np.array([1.5, 3.2, 8.8])
i=np.dot(g,h)
print(i)
#zad 5
j = np.array([[2, 2, 5],[6,2,7]])
for u in j:
    a=np.sin(j)
print(a)
#zad 6
for u in j:
    b=np.cos(j)
print(b)
#zad 7
r=a+b
print(r)
#zad 8
q= np.arange(9).reshape((3,3))
for t in q:
    print(t)
#zad 9
m = np.arange(9).reshape((3,3))
for i in m.flat:
    print(i)
#zad 10
a = np.arange(81).reshape((9,9))
print(a)
c=a.reshape(3,27)
print(c)
#mamy 8 mozliwosci(3 rzedowa, 9 rzedowa, 27 rzedowa, 81 rzedowa oraz 3 kolumny, 9 kolumn, 27 kolumn, 81 kolumn)
#zad 11
y=np.arange(12)
print(y)
c=y.reshape(3,4)
print(c)
c=y.reshape(4,3)
print(c)
c=y.reshape(2,6)
print(c)
#nie sa identyczne














