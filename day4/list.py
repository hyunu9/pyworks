#리스트 항목을 무작위로 섞기
#f2 = random.shuffle(fruit)
import random

com = random.randint(1, 100)

while True:
    guess = int(input(f'맞혀보세요 {"min_v"} ~ {"max_v"})? ')) #사람이 추측한 숫자 입력
    if guess == com:
        print("정답!!")
        break
    elif guess > com:
        print("너무 커요")
        max_v = guess
    else:
        print("너무 작아요")
        min_v = guess
