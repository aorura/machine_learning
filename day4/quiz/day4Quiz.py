import numpy as np
import pandas as pd

grade = pd.DataFrame({'Class':['A','A','B','A','B','A','B','B','A','B'],'Number':[1,2,1,3,2,4,3,4,5,5],\
                      'Lan':[10,20,40,30,10,40,70,80,60,20],'Math':[38,24,67,87,98,34,60,45,29,10],'Eng':[45,36,56,73,46,87,2,45,78,10]})
print('a.','\n')
print('\n', grade)

print('b.','\n')
print('\n', grade.groupby([grade['Class'],grade['Number']]).mean())

clsNum = grade.groupby([grade['Class'],grade['Number']]).mean()
clsNum['Aver'] = (clsNum['Lan'] + clsNum['Math'] + clsNum['Eng']) / 3

print('c.','\n')
print('\n', clsNum)

#print('\n',grade.pivot_table(columns=['Class','Number']))