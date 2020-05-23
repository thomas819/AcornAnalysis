# class : 자원의 재활용 목적으로 새로운 class type을 생성
print(type(1))


# 접근지정자 없다
# method overload 없다
class TestClass:
    aa = 1  # 멤버 변수 . TestClass type 객체에서 공유 가능 .prototype

    def __init__(self):  # 생성자
        print("생성자")

    def __del__(self):
        print('소멸자')

    def printMsg(self):  # 멤버 메소드
        name = '이기자'  # 지역변수


print(id(TestClass), type(TestClass))
print(TestClass.aa)
# TestClass.printMsg() #error

test1 = TestClass()  # 생성자 호출 후 해달 클래스 타입의 객체 생성
print(test1.aa)
test1.printMsg()  # Bound Method call
TestClass.printMsg(test1)  # UnBound Method call
print(id(TestClass), ' ', id(test1))


class Car:
    handle = 0
    speed = 0

    def __init__(self, speed, name):
        self.speed = speed
        self.name = name

    def showData(self):
        km = '킬로미터'
        msg = '속도' + str(self.speed) + km
        return msg


# print(Car.handle)
car1 = Car(10, 'tom')
print(car1.handle, car1.name, car1.speed)
car1.color = '검정'
print(car1.color)

print()
car2 = Car(20, 'james')
print(car2.handle, car2.name, car2.speed)

car1.speed = 77
car2.speed = 88

print(car1.showData())
print(car2.showData())

Car.handle = 5
print(Car.handle)
print(car1.handle)
print(car2.handle)

kor = 100


def abc():
    print('함수')


class My:
    kor = 90

    def abc(self):
        print('메소드')

    def show(self):
        kor = 80
        print(kor)
        print(self.kor)
        self.abc()
        abc()


m = My()
m.show()


# 가수들
class Singer:
    titleSong = '코리아 만세'

    def sing(self):
        msg = '노래는 '
        print(msg, self.titleSong, '랄라라라`~')
    # ...


psy = Singer()
psy.sing()

redvelvet = Singer()
redvelvet.sing()
redvelvet.titleSong = "빨간맛"
redvelvet.sing()
redvelvet.co = 'SM'

print('소속사',redvelvet.co)


psy.sing()
#psy.co

