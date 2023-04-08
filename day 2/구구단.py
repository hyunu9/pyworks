# 구구단
"""
dan = int(input("단을 입력하세요: "))
for i in range(1, 10):
    print(f'{dan} x {i} = {dan * i}')
    
    

#전체 구구단 (2~9단)
start_dan = int(input("시작단 입력:"))
end_dan = int(input("끝단 입력: "))

for i in range(start_dan, end_dan+1):
    for j in range(1, 10):
        print(f'{i} x {j} = {i*j}')

# 중첩 for문
for i in range(0,5): #0,1,2,3,4
    for j in range(0,5):
        print('가', end= '')
    print  () #줄바꿈
 
for i in range(0,5): #0,1,2,3,4
    for j in range(0,i+1):
        print('*', end= '')
    print  () #줄바꿈

for i in range(0,5): #0,1,2,3,4
    for j in range(0, 5-i):
        print('*', end= '')
    print  () #줄바꿈

"""


dan = int(input("단을 입력하세요: "))
result_val = ""
for i in range(1, 10):
    #이스케이프 문자 - '\n' (줄바꿈)
    current_val = f'{dan} x {i} = {dan * i}\n'
    result_val += current_val
print(result_val)



 
