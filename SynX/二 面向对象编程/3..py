class Student:
    def __init__(self,a,b,c):
        self.name = a
        self.age = b
        self.__scores = c
    def introduce(self):
        print(f"我是{self.name},今年{self.age}岁，成绩；{self.__scores}")

class GraduateStudent(Student):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.research_choice = d
    def introduce(self):
        print(f"我是{self.name},今年{self.age}岁,研究方向：{self.research_choice}")
stu3 = GraduateStudent('李四',24,{'语文': 90, '数学': 85, '英语': 92},'机器学习')
stu3.introduce()