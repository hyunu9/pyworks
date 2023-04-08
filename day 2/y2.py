# 반복문(while 무한반복문)
# 1부터 10까지 출력
"""
n = 0
while True:
      n = n + 1
      if n > 10:
        break   

      print(n)
"""
# 입력 문자가 = ' y ' 이면 "반복을 계속합니다."
# 'n'이면 "반복을 중단합니다."
# 'y' , 'n' 둘 다 아니면 "정상 답변이 아닙니다."

while True :
    key =  input("반복을 계속 할까요(y/n)?")

    if key == 'y':
        print("반복을 계속 합니다.")
    elif key == 'n': 
       print("반복을 중단합니다.")
       break
    else:
       print("정상 답변이 아닙니다.")
