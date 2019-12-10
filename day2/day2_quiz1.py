import numpy as np

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
print(arr[:,arr[1,:].argsort()])

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
3.Justices.txt를 참고합니다. 파일의 내용은 아래와 같다.
(이름, 성, 임명한 대통령, 임명 당시 재직한 주, 임명 연도, 대법원을 사임한 연도)
대통령의 이름을 입력 받은 후 해당 대통령이 임명한 대법관을 표시하는 프로그램을 작성한다. 
대법관은 해당 법원에서 근무한 기간에 의해 내림 차순으로 정렬되어야 한다.
(대법관 사임연도가 0인 경우 2015로 바뀌서 사용한다)

ex>
	Enter the name of a president:George W. Bush
	Justice Appointed:
		John Roberts
		Smuel Alito
'''

inputfile = open("data/Justices.txt", "r")
justices = [line.rstrip().rsplit(sep=',') for line in inputfile]

print("President Name: ")
PresName = input()

#Andrew Jackson Bill Clinton
result = []
i=0
for row in justices:
    row[4] = eval(row[4])
    row[5] = eval(row[5])
    if row[2] == PresName:
        if row[5] == 0:
            row[5] = 2015
        row.append(row[5]-row[4])
        row.append(i)
        result.append(row)
        i += 1

#print(result)

sorted=[]
for row in result:
    sorted.append(row[6])
sorted.sort(reverse=True)
#print(sorted)

indexed=[]
for years in sorted:
    for row in result:
        if row[6] == years:
            if row[7] not in indexed:
                print("{0} {1}, {2}, {3} yesrs".format(row[0], row[1], row[2], row[6]))
                indexed.append(row[7])
                break;


inputfile.close()