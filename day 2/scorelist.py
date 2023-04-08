'''
# 리스트의 생성 및 인덱싱
seasons - ['봄','여름','가을','겨울']
print(seasons[0])
print(seasons[-1])

# 리스트 출력
print(seasons)

#전체 요소 출력
for i in seasons:
    print(i)

'''
scorelist = [10,20,30,40]

#요소 추가(append() 함수 - 맨뒤에 추가됨)
scorelist,append(50)
print(scorelist)

#특정 위치에 요소 추가(insert(위치 번호,값))
scorelist,insert(2, 60)
print(scorelist)

#요소 삭제(pop() - 맨 뒤 요소 삭제)
scorelist.pop()
print(scorelist)

#요소 개수(len())
print(len(scorelist))
