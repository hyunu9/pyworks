#random 모듈
import random

#randint(시작수,끝수) - 시작과 끝 수 사이의 정수 중에서 난수 값 발생
#choice(리스트) - 리스트에서 무작위로 하나를 선택

# 1부터 10까지 자연수 중 랜덤하게 1개 출력

num = random.randint(1, 10)
print(num)

# 주사위 한 개 만들기
dice = random.randint(1, 6)
print(dice)

# 주사위 10번 던지기
for i in range(10):
    dice = random.randint(1, 6)
    print(dice)

fruit = ['apple', 'strawberry', 'banana']
f = random.choice(fruit)
print(f)

