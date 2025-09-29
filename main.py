from sympy import *

k, T, C, L = symbols(
    'k T C L'
)  #Сосед поменял местами буквы T и C # Что это означает? (Это объявление переменных, которые будут использоваться в формулах в дальнейшем) - оценка 5

# 1 способ
C_ost = 100000
Am_lst = [
]  # Что это означает? (Это список, в который будут добавляться значения переменной Am) - оценка 5
C_ost_lst = []

for i in range(5):
  Am = (C - L) / T
  C_ost -= Am.subs({
      L: 0,
      T: 4,
      C: 100000
  })  #Сосед поменял значение переменной T с 5 на 4
  Am_lst.append(
      round(Am.subs({
          L: 0,
          T: 4,
          C: 100000
      }), 4)
  )  #Сосед поменял значение переменной T с 5 на 4, также поменял последнее значение с 2 на 4
  C_ost_lst.append(round(C_ost,
                         4))  #Сосед поменял значение переменной T с 5 на 4

print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst)

# 2 способ
Aj = 0
C_ost = 100000  # Что это означает? (Это переменная с присвоенным ей значением, которая будет использоваться в формулах в дальнейшем)  - оценка 5
Am_lst_2 = []
C_ost_lst_2 = []

for i in range(5):
  Am = k * 1 / T * (C - Aj)
  C_ost -= Am.subs({k: 2, T: 5, C: 100000})
  Am_lst_2.append(round(Am.subs({k: 2, T: 5, C: 100000}), 2))
  Aj += Am
  C_ost_lst_2.append(round(C_ost, 2))

print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

# #Контейнер табличного выхода
# import pandas as pd

# Y = range(1, 6)
# table1 = list(zip(Y, Am_lst, C_ost_lst))
# table2 = list(zip(Y, Am_lst_2, C_ost_lst_2))
# frame = pd.DataFrame(table1, columns=['Y', 'Am_lst', 'C_ost_lst']) # Что это означает? (Это создание таблицы с помощью библиотеки pandas, которая будет использоваться для визуализации данных в дальнейшем)  - оценка 5
# frame2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2', 'C_ost_lst_2'])

# print(frame)
# print(frame2)

# #Контейнер визуализации
# from matplotlib import pyplot as plt # Что это означает? (Это импортируемая библиотека для визуализации данных с помощью различных графиков)  - оценка 5

# #Линейный график
# plt.plot(frame['Y'], frame['C_ost_lst'], label='Am')
# plt.plot(frame2['Y'], frame2['C_ost_lst_2'], label='Am_2')
# #plt.show()

# #Круговая диаграмма
# vals = Am_lst_2
# labels = list(range(1, 6))
# explode = (0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie(vals,
#        labels=labels,
#        autopct='%1.1f%%',
#        explode=explode,
#        shadow=True,
#        rotatelabels=True,
#        wedgeprops={
#            'edgecolor': 'k',
#            'lw': 1,
#            'ls': '--'
#        })
# ax.axis('equal')
# #plt.show()

# #Гистограмма
# table1 = list(zip(Y, Am_lst))
# table2 = list(zip(Y, Am_lst_2))
# tfame = pd.DataFrame(table1, columns=['Y', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])

# plt.bar(tfame['Y'], tfame['Am_lst'])
# plt.show()

# plt.bar(tfame2['Y'], tfame2['Am_lst_2'])
# plt.show()

#1 вариант
# from sympy import *

# k, T, C, L = symbols('k C T L')

# # 1 способ
# C_ost = 1000000
# Am_lst = []
# C_ost_lst = []

# for i in range(16):
#   Am = (C - L) / T
#   C_ost -= Am.subs({L: 0, T: 15, C: 1000000})
#   Am_lst.append(round(Am.subs({L: 0, T: 15, C: 1000000}), 2))
#   C_ost_lst.append(round(C_ost, 2))

# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# # 2 способ
# Aj = 0
# C_ost = 1000000
# Am_lst_2 = []
# C_ost_lst_2 = []

# for i in range(16):
#   Am = k * 1 / T * (C - Aj)
#   C_ost -= Am.subs({k: 2, T: 15, C: 1000000})
#   Am_lst_2.append(round(Am.subs({k: 2, T: 15, C: 1000000}), 2))
#   Aj += Am
#   C_ost_lst_2.append(round(C_ost, 2))

# print('Am_lst_2:', Am_lst_2)
# print('C_ost_lst_2:', C_ost_lst_2)

# import pandas as pd
# Y = range(1, 16)
# table1 = list(zip(Y, Am_lst, C_ost_lst))
# table2 = list(zip(Y, Am_lst_2, C_ost_lst_2))
# frame = pd.DataFrame(table1, columns=['Y', 'Am_lst', 'C_ost_lst'])
# frame2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2', 'C_ost_lst_2'])

# print(frame)
# print(frame2)

Секрет
import os

print(os.getenv('My_secret'))

print(os.getenv('Secret_key_1'))
print(os.getenv('Secret_key_2'))
print(os.getenv('Secret_key_3'))
