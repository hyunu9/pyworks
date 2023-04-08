#딕셔너리(Dictionary) 생성과 사용
#{'과일':"딸기"} -> {key:value}
fruit = {'딸기':5000, 'banana' : 3000, 'apple' : 10000}
print(fruit)

#요소 추가
fruit['감'] = 4000

#모든 키 가져오기 - keys() 함수 사용
#딕셔너리를 리스트로 바꾸기
print(fruit.keys)
print(list(fruit.keys()))\
                           
#모든 값 가져오기 - values()
print(fruit.values())
print(list(fruit.values()))

#value 출력
print(fruit['딸기'])

# 전체 출력
for key in fruit:
    print(key, ':' ,fruit[key])

# 전체 출력 - items() : 모든 키와 값 가져오기
for key,val in fruit.items():
    print(key,':', val)
