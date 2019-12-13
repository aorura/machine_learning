import pandas as pd

# a
df_score = pd.DataFrame({
        '반' : ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
        '번호' : [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
        '국어' : [90, 80, 90, 70, 100, 80, 90, 100, 70, 80],
        '영어' : [100, 90, 100, 80, 70, 90, 100, 70, 80, 90],
        '수학' : [80, 100, 80, 90, 80, 100, 70, 80, 90, 100]},
        columns = ["반", "번호", "국어", "영어", "수학"]
    )
print(df_score,'\n')

# b
df1 = df_score.set_index(["반", "번호"])
print(df1,'\n')

# c
df1["평균"] = df1.mean(axis = 1)
print(df1,'\n')

# d
df2 = df_score.set_index(["반", "번호"])
df3 = df2.unstack("반")
print(df3,'\n')

# e
df3.loc["평균", :] = df3.mean()
print(df3,'\n')