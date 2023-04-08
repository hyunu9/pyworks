# 커피 자동판매기 프로그램
# 커피 가격은 400원
coffee = 5

while True:
    try:
        money = int(input("돈을 넣어주세요: "))
        if money == 400:
             print("커피가 나옵니다.")
             coffee = coffee - 1
             print(" 남은 커피의 양은  "+ str(coffee) + "개 입니다.")
        elif money > 400:
             # print("커피가 나오고, 거스름돈 " + str(money-400) + "원입니다" + " 남은 커피의 양은  "+ str(coffee-1) + "개 입니다.")
            print(f'커피가 나오고, 거스름돈{money -400}원 입니다.')
           coffee -= 1
        else :
              print("커피가 나오지 않습니다.")

             #print(" 남은 커피의 양은  "+ str(coffee) + "개 입니다.")
              print(f"남은 커피의 양은 {coffee}개입니다.")

        #커피의 개수가 0이되면 반복 중단.
        if coffee == 0:
           print("커피가 모두 소진되었습니다. 판매를 중지합니다.")
           break

