# 제한속도가 50이상이면 "속도 위반 아니면 "속도 준수"
"""
limit_speed = 50

if  limit_speed >= 50: # 55 >+ 50 -> True
   print("속도 위반") #들여쓰기, 인덴트
"""
#조건문(if ~ else문)
#제한 속도가 50km이상이면 "속도 위반, 과태료 10만'이고
# 50km 미만이면 "안전 준수"
"""
limit_speed = 49

if limit_speed >= 50:
  print("속도 위반, 과태료 10만원")
else: #limit  _speed < 50
    print("안전 준수")

"""
# 시험 점수가 60점 이상이면 "합격" , 아니면 "불합격"
"""
점수 = 65
if 점수 < 65:
  print("합격")
else:
    print("불합격")
"""
# 어떤 수를 짝수와 홀수로 출력하세요
num = 5
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 어떤 수를 입력받아서 짝수와 홀수를 출력하세요
# %를 나머지 연산자
num = int(input("숫자 입력: "))
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

