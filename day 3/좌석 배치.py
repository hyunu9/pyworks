# 좌석 배치
customer = int(input("입장객 수 입력: ")) #입장객
col_num =  int(input("좌석 열 수 입력: "))  #좌석 열
#row_num = 0;  #줄수

if customer % col_num == 0:
    row_num = customer // col_num
    #row_num = int(customer / col_num)
else:
    row_num = int(customer / col_num) + 1

#print(str(row_num) + "줄이 필요합니다.")
#print(f'{row_num}줄이 필요합니다.)
#print("{}줄이 필요합니다.".format(row_num))

for i in range(0, row_num):
    for j in range(1, col_num):
        seat_num = (col_num * i)+j
        print("좌석" + str(seat_num), end=' ')
    print()
