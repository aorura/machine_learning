import pandas as pd

df1 = pd.DataFrame({'key':['b','b','a','c','a','a','b'],'data1':range(7)})
df2 = pd.DataFrame({'key':['a','b','d'],'data2':range(3)})

print('\n',df1, '\n')
print('\n',df2, '\n')

print('\n', pd.merge(df1,df2),'\n')

print('\n', pd.merge(df1,df2, on='key'),'\n')

print('\n1.', pd.merge(df1,df2, how='outer'),'\n')
print('\n2.', pd.merge(df1,df2, how='left'),'\n')
print('\n3.', pd.merge(df1,df2, how='right'),'\n')
print('\n4.', pd.merge(df1,df2, how='inner'),'\n')

'''
df3 = pd.DataFrame({'lkey':['b','b','a','c','a','a','b'], 'data1':range(7)})
df4 = pd.DataFrame({'rkey':['a','b','d'],'data2':range(3)})
'''

left = pd.DataFrame({'key1':['foo','foo','bar'],
                     'key2':['one','two','one'],
                     'lval':[1,2,3]})
right = pd.DataFrame({'key1':['foo','foo','bar','bar'],
                      'key2':['one','one','one','two'],
                      'rval':[4,5,6,7]})

print('\n1.',left,'\n')
print('\n2.',right,'\n')
print('\n3.',pd.merge(left,right,on=['key1','key2'],how='outer'),'\n')

print('\n4.',pd.merge(left,right,on='key1',suffixes=('_left','_right')),'\n')
