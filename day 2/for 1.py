# for 문을 이용한 반복문
# 1부터 10까지 출력, 합계

i = 0
while  i < 10:
     i = i + 1
     print(i, end='')
print()   
print('=' * 30)

# range(시작값, 종료값, 증감값)
for i in range(0, 11):  #10 + 1
     print(i)

# 1부터 10까지 홀수 출력
for i in range(1, 11, 2):
     print(i)

# 1부터 10까지 짝수를 출력
for i in range(1, 11):
      if i % 2 == 0:
       print(i)

# 1부터 10까지의 합계
#sum_v = 0
for i in range(11): #range(0, 11, 1)
    sum_v = sum_v + i

print("합계:", sum_v)
     
