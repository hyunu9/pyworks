# 변수의 사용(사용 범위)
# 지역변수 생성 - 함수나 제어문의 블럭 안에서 생성
# 지역변수 소멸 - 함수나 제어문의 실행이 끝나면 소멸

def one_up():
    x = 1
    x = x + 1
    return x
#print(x) - x
print(one_up()) #2
print(one_up()) #3
print(one_up()) #4

