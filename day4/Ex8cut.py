import pandas as pd

ages = [20,22,25,27,31,38,61,40,45,32]
bins = [18,25,35,60,100]

cats = pd.cut(ages,bins)
print(cats)
cats = pd.cut(ages,bins,right=False) #오른쪽 미포함
print(cats)
print('\n',pd.value_counts(cats))

group_names=['youth','youngAdult','middleAge','Senior']
cats3 = pd.cut(ages,bins,labels=group_names)
print('\n', pd.value_counts(cats3))
#print('\n', pd.value_counts(cats3,sort=False))