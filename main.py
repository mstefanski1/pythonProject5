import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#y= np.arange(2,9,2)
#plt.plot(y)
#plt.show()

#x=np.array([1,2,3,4])
#y=x**2

#plt.plot(x,y,'r-')
#plt.plot(x,y,'o')
#plt.axis([0,6, 0,20])
#plt.show()

a=np.arange(0,5,0.2)
#plt.plot(a, a, 'r-', a,a**2,'bs',a,a**3,'g')
#plt.legend(labels=['liniowa','kwadratowa','szescienna'], loc='center left')
#plt.show()

#plt.plot(a,a,'r-',label='liniowa')
#plt.plot(a,a**2,'bs',label='kwadratowa')
#plt.plot(a,a**3,'g',label='szescienna')
#plt.xlabel('x')
#plt.ylabel('y')

#plt.title('Wykres liniowy')
#plt.savefig('wykres.png')
#plt.legend()
#plt.show()
#img = Image.open('wykres.png')
#img=img.convert('RGB')
#img.save('wykres')

#x=np.arange(0,10.1,0.1)
#y=np.sin(x)
#plt.plot(x,y,'r')
#plt.show()

# data = {'a':np.arange(50),
#         'c':np.random.randint(0,50,50),
#         'd':np.random.randn(50)}
# data['b'] = data['a']+ 10 * np.random.randn(50)
# data['d'] = np.abs(data['d'])*100
#
# plt.scatter('a','b',c='c',s='d',data=data,cmap='plasma')
# plt.xlabel('a')
# plt.ylabel('b')
# plt.show()

x1=np.arange(0,2,0.02)
x2=np.arange(0,2,0.02)

y1 = np.sin(2*np.pi*x1)
y2 = np.cos(2*np.pi*x2)

# plt.subplot(2,1,1)
# plt.plot(x1,y1)
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Wykres sin(x)')
# plt.subplot(2,1,2)
# plt.plot(x2,y2)
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.title('Wykres cos(x)')
# plt.subplots_adjust(hspace=0.5)
# fig,axs = plt.subplot(3,2)
# axs[0,0].plot(x1,y1,'r')
# axs[0,0].set_xlabel('x')
# axs[0,0].set_ylabel('sin(x)')
# axs[0,0].set_title('wykres sin(x)')
#
# axs[1,1].plot(x2,y2,'g')
# axs[1,1].set_xlabel('x')
# axs[1,1].set_ylabel('cos(x)')
# axs[1,1].set_title('wykres cos(x)')
#
# axs[2,0].plot(x1,y1,'r')
# axs[2,0].set_xlabel('x')
# axs[2,0].set_ylabel('sin(x)')
# axs[2,0].settitle('wykres cos(x)')
#
# fig.delaxes(axs[0,1])
# fig.delaxes(axs[1,0])
# fig.delaxes(axs[2,1])
#
# plt.show()

# ts=pd.Series(np.random.randn(1000))
# ts=ts.cumsum()
#
# ts.plot()
# plt.show()

# data={'Kraj': ['Belgia','Indie','Brazylia','Polska'],
#       'Stolica': ['Bruksela','New Delhi','Brasilia','Warszawa'],
#       'Kontynent': ['Europa','Azja','Ameryka Poludniowa','Europa'],
#       'Populacja': [11109846,1303171035,207847528,38675467]}
# df=pd.DataFrame(data)
# grupa=df.groupby('Kontynent').agg({'Populacja': ['sum']})
# # grupa.plot(kind='bar',xlabel='Kontynenty',ylabel='Populacja',legend=True,title='Populacja na kontynencie',rot=0)
# wykres=grupa.plot.bar()
# wykres.set_xlabel('Kontynenty')
# wykres.set_ylabel('Populacja')
# wykres.tick_params(axis='x',labelrotation=0)
# wykres.legend()
# wykres.set_title('Populacja na kontynentach')
#
# plt.show()

df = pd.read_csv('dance.csv',header=0,setp=';',decimal='.')
print(df)
grupa=df.groupby('Imie i nazwisko').agg({'Wartosc zamowienia':['sum']})
grupa.plot(kind='pie',subplots=True,autopct='%.2f%%',
           fontsize=20,colors=['red','green'])
plt.show()



