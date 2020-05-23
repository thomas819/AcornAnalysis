# 상속 : 자원의 재활용 - 다형성을 구사
print('어쩌구 저쩌구')


class Animal:
    leg = 4

    def move(self):
        print('움직이는 동물')


class Dog(Animal):  # 상속
    age = 1

    def my(self):
        print('나는 개')


dog1 = Dog()
dog1.my()
dog1.move()
print(dog1.leg)


class Horse(Animal):
    pass


h = Horse()
h.move()


class Person:
    say = '난 사람이야'
    age = '20'

    def __init__(self, age):
        print('Pserson 생성자')
        self.age = age

    def PrintInfo(self):
        print('나이:{} 이야기:{}'.format(self.age, self.say))

    def Hello(self):
        print("안녕")


p = Person('33')
p.PrintInfo()
p.Hello()

print('***' * 20)


class Employee(Person):
    def __init__(self, age):
        super().__init__(age)
        print('Employee 생성자')


print('***' * 20)
ee = Employee('1')
ee.PrintInfo()


class Worker(Person):
    def __init__(self, age):
        super().__init__(age)  # =Person.__init__(self, age)
        print('Worker 생성자')

    def PrintInfo(self):
        print('Method overriding')

    def abc(self):
        self.PrintInfo()
        super().PrintInfo()


w = Worker('44')
w.PrintInfo()
w.abc()

print('-------------------------')
print(type(1))
print(type(w))
print(Worker.__bases__)
print(Person.__bases__)


# 다중 상속

class Tiger:
    def Cry(self):
        print('어흥')

    def aa(self):
        print('aa')


class Lion:
    def Cry(self):
        print('푸하하')

    def bb(self):
        print('bb')


class Liger(Tiger, Lion):
    pass


li = Liger()
li.aa()
li.bb()
li.Cry()
