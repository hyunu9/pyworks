#날짜 시간 관련 모듈
import datetime

#오늘의 날짜와 시간
now = datetime.datetime.today()
print(now)
print(now.strftime("%Y, %m, %d, %H:%M:%S"))

# 날짜 - 년, 월, 일 출력
print("{}년".format(now.year))
print("{}월".format(now.month))
print("{}일".format(now.day))

#시간 - 시,분,초
print("{}시".format(now.hour))
print("{}분".format(now.minute))
print("{}초".format(now.second))

# 나이가 100세 되는 해의 연도 계산하기
today = datetime.date.today()
print(today.year) #2023

age = int(input("나이 입력 : "))
result = today.year + (100 - age)
print(f'100세 되는 해는 {result}년 입니다')

