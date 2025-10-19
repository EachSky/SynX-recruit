class Dog:
    #?一个类必须要有属性吗
    #不必要有，没有需求就可以没有
    def speak(self):
        print("汪汪")

class Cat:
    def speak(self):
        print("喵喵")

dog = Dog()
cat = Cat()
def animal_speak(animal):
    animal.speak()#！体现多态
    #只要对象里确实有一个speak方法，Python运行时会自动找到对应的版本
    # （自动找到对应的版本指的是（自动找到对象）运行方法时，是谁的对象就执行谁的方法）

animal_speak(dog)#输出是调用函数，故要写函数名，再带入实参即可
animal_speak(cat)