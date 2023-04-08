# 리스트의 주요 함수
car = ['소나타', '모닝' , 'BMW']
# 요소 추가 - append() : 맨 뒤에 추가
car.append('스포티지')
print(car)

# 요소 삭제 - pop() : 맨 뒤에서삭제
car.pop()
print(car)

# 특정 위치에 추가 - insert (인덱스,요소)
car.insert(1, 'K7')
print(car)

#특성 요소 삭제 - remove(요소)
car.remove('모닝')
print(car)

#리스트의 복사, 데이터 저장
a = [1,2,3,4,5]
a2 = [] #빈 리스트 생성

#a2 = a 전체 복사
#print(a2)

#append() 사용
a2.append(1)
print(a2)

# 2의 배수로 저장
"""
a3 = []
for i in a:
    a3.append(i*2)
"""
# 리스트 내포(append() 사용안함)
# [표현식 for 항목 in 리스트]
a3 = [i*2 for i in a]
print("a3 =", a3)

#3의 배수이면서 짝수 저장
"""
b1 = []
for i in a:
    if i % 2 == 0:
      b1.append(3*i)
"""
b1 = [3 * i for i in a if i % 2 == 0]
print(b1)
