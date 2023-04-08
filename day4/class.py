# 학생 클래스(Student)
# 클래스 이름은 첫 글자 대문자임.

class Student:

    def __init__(self): #초기자(함수)
        self.name = "이순신"
        self.grade = 1

# 객체 이름 = 클래스 이름()
s1 = Student() #객체(인스턴스) 생성(객체 변수 - 메모리에서 실행됨)
print(f'이름 : {s1.name}')
print(f'학년 : {s1.grade}')