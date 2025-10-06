from sympy import *

k, T, C, L = symbols(
    'k T C L'
) 

# 1 способ
C_ost = 90000
Am_lst = [
] 
C_ost_lst = []

for i in range(9):
    Am = (C - L) / T
    C_ost -= Am.subs({
        L: 0,
        T: 9,
        C: 90000
    }) 
    Am_lst.append(
        round(Am.subs({
            L: 0,
            T: 9,
            C: 90000
        }), 2)
    ) 
    C_ost_lst.append(round(C_ost,
                           2))  

print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst)

# 2 способ
Aj = 0
C_ost = 90000  
Am_lst_2 = []
C_ost_lst_2 = []

for i in range(9):
    Am = k * 1 / T * (C - Aj)
    C_ost -= Am.subs({k: 2, T: 9, C: 90000})
    Am_lst_2.append(round(Am.subs({k: 2, T: 9, C: 90000}), 2))
    Aj += Am
    C_ost_lst_2.append(round(C_ost, 2))

print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Контейнер табличного выхода
import pandas as pd

Y = range(1, 10)
table1 = list(zip(Y, Am_lst, C_ost_lst))
table2 = list(zip(Y, Am_lst_2, C_ost_lst_2))
frame = pd.DataFrame(
    table1, columns=['Y', 'Am_lst', 'C_ost_lst']
)  
frame2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2', 'C_ost_lst_2'])

print(frame)
print(frame2)

#Контейнер визуализации
from matplotlib import pyplot as plt 

#Линейный график
plt.plot(frame['Y'], frame['C_ost_lst'], label='Am')
plt.plot(frame2['Y'], frame2['C_ost_lst_2'], label='Am_2')
#plt.show()

#Круговая диаграмма
vals = Am_lst_2
labels = list(range(1, 10))
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(vals,
       labels=labels,
       autopct='%1.1f%%',
       explode=explode,
       shadow=True,
       rotatelabels=True,
       wedgeprops={
           'edgecolor': 'k',
           'lw': 1,
           'ls': '--'
       })
ax.axis('equal')
#plt.show()

#Гистограмма
table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame = pd.DataFrame(table1, columns=['Y', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])

plt.bar(tfame['Y'], tfame['Am_lst'])
plt.show()

plt.bar(tfame2['Y'], tfame2['Am_lst_2'])
plt.show()
