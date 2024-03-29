import pandas as pd

df1 = pd.DataFrame({
    '매출' : [10000000, 12000000, 9000000, 6000000, 8000000, 1100000],
    '비용' : [15000000, 1300000, 1200000, 9000000, 9900000, 9500000]},
    index = ['1월', '2월', '3월', '4월', '5월', '6월'])
print(df1,'\n')

df2 = pd.DataFrame({
    '매출' : [13000000, 14000000, 17000000, 15400000, 16500000, 16600000],
    '비용' : [11000000, 10400000, 11000000, 12100000, 9000000, 9500000]},
    index = ['7월', '8월', '9월', '10월', '11월', '12월'])
print(df2,'\n')

df3 = pd.concat([df1, df2])
print(df3,'\n')

df4 = pd.concat([df3, pd.DataFrame({'이익' : df3['매출'] - df3['비용']})], axis =1)
print(df4,'\n')

df5 = pd.concat([df4, pd.DataFrame({'매출' : df4['매출'].sum(), '비용' : df4['비용'].sum(),
                                    '이익' : df4['이익'].sum()},
                                   index = ['총실적'])], axis =0)
print(df5, '\n')