def one_up():
    global x
    x = x + 1
    return x

# 메인 영역
x = 1
#one_up() 함수의 전역변수 선언
print(one_up()) #2
print(one_up()) #3
print(one_up()) #4
print(x) #4