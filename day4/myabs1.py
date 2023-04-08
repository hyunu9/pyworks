# 절대값을 계산하는 함수

def myabs(x):
    if x < 0:
        return -x
    else:
        return x


print(myabs(4)) #4
print(myabs(-1)) #1
print(abs(-1)) #1

# 1 ~ 30 까지 자연수 중에서 배수를 3의 배수를 출력하세요

def times(x):
    for i in range(1, 31):
        # 3의 배수 : 3으로 나누어 떨어지는 수(나머지가 0)
        if i % x == 0:
             print(i, end= ' ')
        """
        i=1, 1% 3 == 0 false
        i=2, 1% 3 == 0 false
        i=3, 1% 3 == 0 true
        """

count = 0 #전역 변수(정적(static) 변수)
times(3)
print(f'\n배수의 개수: {count}')