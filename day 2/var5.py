#조건문(if ~ elif ~ else문):  다중 조건문인 경우
"""
pizza = input('피자가게가 열렸나요(예/아니요)? ')
chicken = input('치킨가게가 열렸나요(예/아니요)? ')
if pizza == '예':
    print('피자 가게로 가자')
elif chicken == '예':
    print('치킨 가게로 가자')
else: # piazza != '예' , chicken != '예'
    print('편의점에서 라면을 먹자')
    """

#근속년수가 5년 이상이고 직급이 사원이면 대리로 승진
"""
진급 = '사원'
근속년수 = 4

if 직급 == '사원' and 근속년수 >= 5:
    print("승진 대상입니다.")
else:
    print("승진 대상이 아닙니다.")
"""

#교통 수단
pocket = ['스마트폰', 'money','paper']
if 'coin' in pocket:
    print("택시를 탄다")
else:
    print("지하철을 탄다")
