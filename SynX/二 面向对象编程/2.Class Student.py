#1.定义类
class Student:
    def __init__(self,a,b,c):
        self.name = a
        self.age = b
        self.__scores = c
        # ？如何命名私有属性，包含语文 数学 英语的字典
#想命名私有属性，直接在属性名前加上两个__即可。至于字典，用大括号括键与值，逗号隔开。
        # ！复习字典及常见容器的用法和声明
    def introduce(self):
        print(f"我是{self.name},今年{self.age}岁，成绩；{self.__scores}")#打印字符串中包含变量的结构
        # ? 依旧字典等容器的用法规范"我是张三，今年18岁，成绩：{'语文':90, '数学':85, '英语':92}"
    def get_average(self):
        return sum(self.__scores)/len(self.__scores)# ! 求和除长度(科目数)
    #？？？？？

    def update__score(self,subject,value):
 #这里的subject,value是啥意思
        if subject in self.__scores:
            self.__scores[subject] = value
    #?update_score(subject, value)：修改某一科成绩具体要咋操作呀

#2，创建两个学生对象
stu1 = Student('机器',18,{'语文': 90, '数学': 85, '英语': 92})#？冒号后加空格会影响字符串和整型吗
stu1.introduce()

print(stu1.get_average())#这里如果仅是print(get_average())，没有限定就不知道是针对哪一个对象
#？return和print的区别
# print ：把结果显示给人看，返回  None 。
 #return ：把结果交给程序/调用者，函数从此点结束并带回该值。1.函数本身不会“输出”；调用函数会产生一个值，这个值就是  return  给出的。 2.没有  return （或只写  return  不带值），函数调用表达式的值就是  None 。3. 一旦执行到  return ，函数立即结束，后面语句不再执行。)
stu2 = Student('学习',18,{'语文': 100, '数学': 100, '英语': 100})#？这里逗号后若没有空格会怎样
stu2.introduce()
print(stu2.get_average())

#3.测试封装效果
#直接修改私有属性
#stu1.update__score['数学'] = 100#这里方括号是什么意思，列表？
#正确更新成绩
stu1.update__score("数学", 100)
stu1.get_average()
#?更新成绩的具体操作
