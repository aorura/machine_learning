import numpy as np
'''
#1. 5 X 6 형태의 데이터 행렬을 만들고 이 데이터에 대해 다음과 같은 값을 구한다.
#   a. 전체의 최대 값
#   b. 각 행의 합
#   c. 각 열의 평균
#   d. 첫 번째 열 값으로 모든 행으로 정렬
#   e. 두 번째 행 값으로 모든 열을 정렬

np.random.seed(777)
arr = np.random.randn(5,6)

print(arr)

print('a.전체의 최대 값: ', format(arr.max(), '.3f',))

print('b.각 행의 합: ', arr.sum(axis=1))
print('c.각 열의 평균: ', arr.mean(axis=0))
print('d.첫 번째 열값으로 모든 행으로 정렬: ')
print(arr[arr[:,0].argsort()])
print('ㄷ.첫 번째 행값으로 모든 열을 정렬: ')
print(arr[:,arr[0,:].argsort()])
'''
'''
2.1990년 초에 크레욜라 크레용은 72개의 색상(Pre1990.txt)을 갖고 있었다. 1990년대
8색상(Retired.txt)이 빠지게 되었고 56개의 새로운 색상(Added.txt)이 추가되었다.
지난 1990년대 119개의 크레용 색상을 알파벳 순서로 나열한 텍스트 파일을 생성하는 
프로그램을 작성한다.
'''
f_pre1990 = open("data/Pre1990.txt", 'r')
firstSet = {line for line in f_pre1990}
f_retired=open('data/Retired.txt','r')
secondSet={line for line in f_retired}
f_added=open('data/Added.txt','r')
thirdSet={line for line in f_added}

f_pre1990.close()
f_retired.close()
f_added.close()

outfile=open("data/creyon119.txt",'w')
outfile.writelines(sorted(firstSet.difference(secondSet).union(thirdSet)))
outfile.close()

'''
outfile=open("data/creyon119.txt",'w')
outfile.writelines(firstSet.union(secondSet))
outfile.close()

outfile = open('data/intersection.txt','w')
outfile.writelines(firstSet.intersection(secondSet))
outfile.close()

outfile=open('data/Difference.txt','w')
outfile.writelines(firstSet.difference(secondSet))
outfile.close()

'''