import pandas as pd
import numpy as np

fec = pd.read_csv('data/P00000001-ALL.csv')
print(fec.info())

print(fec.loc[123456])

unique_cands = fec.cand_nm.unique()
print('\n', unique_cands)

parties = {'Bachmann, Michelle':'Republican',
           'Cain, Herman':'Republican',
           'Gingrich, Newt':'Republican',
           'Huntsman, Jon':'Republican',
           'Johnson, Gary Earl':'Republican',
           'McCotter, Thaddeus G':'Republican',
           'Obama, Barack':'Democrat',
           'Paul, Ron':'Republican',
           'Pawlenty, Timothy':'Republican',
           'Perry, Rick':'Republican',
           "Roemer, Charles E. 'Buddy' III":'Republican',
           'Romney, Mitt':'Republican',
           'Santorum, Rick':'Republican'}

#print('\n',fec['cand_nm'].map(lambda x:parties[x.lower()]),'\n')
# 정당을 후보자에 매칭
fec['party']=fec['cand_nm'].map(parties)
print('\n',fec.head(),'\n')

#키값에 대한 빈도수
print('\n',fec.party.value_counts())

# 0이상값이 있는 것만 리턴
fec = fec[fec.contb_receipt_amt>0]
print('\n',fec)

#isin 값이 있는지 확인하는 펑션
#fec_mrbo = fec[fec.cand_nm == 'Obama, Barack'
fec_mrbo = fec[fec.cand_nm.isin(['Obama, Barack','Romney, Mitt'])]
print('\n',fec_mrbo)

print('\n',fec.contbr_occupation.value_counts()[:10])

occ_mapping = {
    'INFORMATION REQUESTED PER BEST EFFORTS':'NOT PROVIDED',
    'INFORMATION REQUESTED':'NOT PROVIDED',
    'INFORMATION REQUESTED (BEST EFFORTS)':'NOT PROVIDED',
    'C.E.O':'CEO'
}
# get(값, 값이없으면 이값사용)
f = lambda x : occ_mapping.get(x,x)
fec.contbr_occupation = fec.contbr_occupation.map(f)

emp_mapping = {
    'INFORMATION REQUESTED PER BEST EFFORTS':'NOT PROVIDED',
    'INFORMATION REQUESTED':'NOT PROVIDED',
    'SELF':'SELF-EMPLOYED',
    'SELF EMPLOYED':'SELF-EMPLOYED'
}

f = lambda x : emp_mapping.get(x,x)
fec.contbr_employer = fec.contbr_employer.map(f)

by_occupation = fec.pivot_table('contb_receipt_amt',index='contbr_occupation',columns='party',aggfunc='sum')
print('\n', by_occupation)

over_2mm = by_occupation[by_occupation.sum(axis=1)>2000000]
print('\n', over_2mm)

import matplotlib.pyplot as plt

over_2mm.plot(kind='barh')
#plt.show()

def get_top_amounts(group, key, n=5):
    totals = group.groupby(key)['contb_receipt_amt'].sum()
    return totals.sort_values(ascending=False)[:n]

grouped = fec_mrbo.groupby('cand_nm')
print('\n', grouped.apply(get_top_amounts,'contbr_occupation',n=7),'\n')

bins = np.array([0,1,10,100,1000,10000,100000,1000000,10000000])
labels = pd.cut(fec_mrbo.contb_receipt_amt, bins)
print('\n', labels, '\n')

grouped = fec_mrbo.groupby(['cand_nm', labels])
print('\n', grouped.size(), '\n')
print('\n', grouped.size().unstack(0), '\n')

bucket_sums = grouped.contb_receipt_amt.sum().unstack(0)
print('\n', bucket_sums)

normed_sums= bucket_sums.div(bucket_sums.sum(axis=1), axis=0)
print('\n', normed_sums)

# stacked : 겹쳐지게 그래프 그림
normed_sums[:-2].plot(kind='barh',stacked=True) #-2 마지막 2개 빼서 그래프 그림
plt.show()
