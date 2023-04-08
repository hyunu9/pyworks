#return이 있는 함수
#제곱수를 계산하는 함수
def square(x):
    return x * x

#print(square(2))

#1이 증가하는 함수
def one_up(x):
    x = x + 1
    return x

print(one_up(2))

#매개 변수가 2개 있는 함수
#두 수의 차를 구하는 함수
def sub(x,y):
    minus = x - y
    return minus
#두 수의 합을 구하는 함수
def add(x,y):
    return x + y
   
#호출
val = sub (4,7)
val2 = add(4,7)
print("두 수의 합 = {0}", format(val2))
print("두 수의 차 = {0}", format(val))

    
    
