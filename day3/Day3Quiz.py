import numpy as np
import pandas as pd
'''
data1 = pd.DataFrame({"color":['red','blue','green','yello','black'],"size":['s','m','l','xl','xs'],\
                      'gender':['m','w','m','w','m'],'part':['shirt','shirt','pant','shirt','pant'],'sale':['yes','no','no','yes','yes']})
data2 = pd.DataFrame({"Farbe":['red','blue','green','yello','black'],"size":['s','m','l','xl','xs'],\
                      'brand':['tommy','eagle','guess','zara','ck'],'part':['shirt','shirt','pant','shirt','pant'],'soldout':['yes','no','no','yes','yes']})


data3 = pd.merge(data1,data2,left_on='color', right_on='Farbe',how='outer',suffixes=('_left','_right'))

print('\n',data3.drop(['size_left','part_left','size_right','part_right'],axis='columns'))
'''

df1 = pd.DataFrame({
    '매출': [10000000, 12000000, 9000000, 6000000, 8000000, 1100000],
    '비용': [15000000, 1300000, 1200000, 9000000, 9900000, 9500000]},
    index=['1월', '2월', '3월', '4월', '5월', '6월'])

df2 = pd.DataFrame({
    '매출': [13000000, 14000000, 17000000, 15400000, 16500000, 16600000],
    '비용': [11000000, 10400000, 11000000, 12100000, 9000000, 9500000]},
    index=['7월', '8월', '9월', '10월', '11월', '12월'])

df3 = pd.DataFrame([],columns=['매출','비용','이익'],index=['1월', '2월', '3월', '4월', '5월', '6월','7월', '8월', '9월', '10월', '11월', '12월'])

print('\n',df1)
print('\n',df2)
print('\n',df3)

print('\n', pd.concat([df1,df2]))
print('\n', df3.add(pd.concat([df1,df2]), fill_value=0))

df4 = df3.add(pd.concat([df1,df2]), fill_value=0)
#df4.fillna(method=lambda profit )

