# 비교연산

x = 10
y = 11

print(x > y)
print( x== y)
print(x != y)
print(x is not y)

'''
#논리 연산
#비교연산을 or, and를 사용해서 수행
# and는 둘 다 참일 때 참
 True and True -> True 이외 나머지는 False
or는 둘 중에 하나만 참이라도 참
 True or False -> True
 True or False -> True
 False or True -> True
not은 논리 부정(반대)
 True -> False
 False -> True
'''

x = 10
y = -10
print(y)
print( x > 0 and y > 0)
print( x > 0 or y  > 0)
print(not x > 0)
