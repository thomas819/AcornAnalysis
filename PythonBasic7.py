# 클래스가 다른 클래스를 호출해서 자신의 멤버인 양 사용하기 : 포함

class PohamHandle:
    quantity = 0  # 회전량

    def LeftTurn(self, quantity):
        self.quantity = quantity
        return '좌회전'

    def RightTurn(self, quantity):
        self.quantity = quantity
        return '우회전'


# PohamHandle을 별도 모듈로 만들고 import 했다 가정
print('자동 완성하기')


class PohamCar:
    handle = 1
    # ...
    turnShow = '정지'

    def __init__(self, ownerName):
        self.ownerName = ownerName
        self.handle = PohamHandle()  # 포함

    def TurnHandle(self, q):
        if q > 0:
            self.turnShow = self.handle.RightTurn(q)
        elif q < 0:
            self.turnShow = self.handle.LeftTurn(q)
        else:
            self.turnShow = '직진'


if __name__ == '__main__':
    tom = PohamCar('톰')
    tom.TurnHandle(10)
    print(tom.ownerName + '의 회전량은' + tom.turnShow + str(tom.handle.quantity))
    tom.TurnHandle(-20)
    print(tom.ownerName + '의 회전량은' + tom.turnShow + str(tom.handle.quantity))
    print()
    dong = PohamCar('길동')
    dong.TurnHandle(0)
    print(dong.ownerName + '의 회전량은' + dong.turnShow + str(dong.handle.quantity))


