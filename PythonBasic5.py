# Module : 소스코드를 하나의 이름공간으로 구분하고 관리한다
# 내장 모듈
import math

print(math.pi)

import calendar

calendar.setfirstweekday(6)
calendar.prmonth(2020, 5)

import random

print(random.random())
from random import random, randrange

print(random())
print(randrange(1, 10))

# 사용자 정의 모듈

import MyModule as m
#from MyModule import Hap, Cha


# print(dir())  # 파이썬자체적으로 쓰는 네이밍

def aa():
    list1 = [1, 3]
    list2 = [2, 4, 6]

    print(m.ListHap(list1, list2))
    print(m.kbs)


if __name__ == '__main__':
    print("최상위 모듈이다")
    aa()
