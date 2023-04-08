#딕셔너리 - 리스트처럼 여러 개의 값을 저장할 수 있고,
#키(key)와 값(value)으로 대응시켜 저장하는 자료구조이다.
# person = {'name':'김한국','age':28}

person = {} #빈 딕셔너리 선언

print(person)

#딕셔너리 생성
person['name'] = "오상식"
person['age'] = 35
person['phone'] = "010-1111-1111"
print(person)

#특정 요소 출력
print(person['name'])

#전체 출력
for key in person:
    print(person[key])

#특정 요소 출력
person['age'] = 40
print(person['age'])

#특정 요소 삭제
del person['phone']
print(person)

#요소 추가
person['email'] = "test@test.co.kr"
print(person)
print(type(person))


