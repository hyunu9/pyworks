# 4명의 학생
student=[
    {'name': '이대한', 'kor': 80, 'eng': 80, 'math': 75},
    {'name': '박민국','kor': 70, 'eng': 50, 'math': 77},
    {'name': '오상식', 'kor': 60, 'eng': 45, 'math': 78},
    {'name': '최지능', 'kor': 30, 'eng': 90, 'math': 45}
]
print("=== 학생의 성적표 ===")
print("이름  국어영어수학")
for std in student:
  # print(std['name'], std['kor'], std['eng'], std['math'])
    print(f'{std["name"]} {std["kor"]} {std["eng"]} {std["math"]}')

print("=== 개인별 총점과 평균 ===")
for std in student:
    total = std["kor"]+ std["eng"]+ std["math"]
    avg = total /3
    print(f'{std["name"]} {total} {avg:0.2f}')