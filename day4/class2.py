# 클래스

class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def learn(self):
        print("수업을 들어요")

s1 = Student("김하나",1)
print(f'{s1.name} 학생은 {s1.grade}학년입니다.')
s1.learn()

s2 = Student("김둘",1)
print(f'{s2.name} 학생은 {s2.grade}학년입니다.')
s2.learn()