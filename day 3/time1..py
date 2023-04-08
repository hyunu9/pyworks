# time 모듈
import time

# 1970 1. 1 이후의 지금까지시간 - 초로 환산
print(time.time())

# 년과 일로 환산
year = round(time.time()/(365*24*60*60))
print(year)
day = round(time.time()/(24*60*60))
print(day)

#수행 시간 측정하기
# 1부터 10까지 출력하기
start = time.time() #시작시간
for i in range(1,11):
    print(i)
    time.sleep(0.5)

end=time.time() #끝나는 시간
print(f'수행 시간: {end-start:0.3f}초')

import calendar

#calendar.prcal(2023)
calendar.prmonth(2023, 4)
