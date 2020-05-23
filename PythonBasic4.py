# 함수 : 모듈 내에 중복 자료가 많은 경우 작은 unit을 만들고 호출


a = 5


def DoFun1():
    print('DoFunc1 처리')


print(DoFun1)
print(DoFun1())
a = DoFun1  # 주소넘김
a()
b = DoFun1()  # 값전달
print(b)

print()


def DoFun2(a, b):
    print(a, ' ', b)
    return a + b


result = DoFun2(10, 20)
print(result)

result = DoFun2('kbs', '공영방송')
print(result)

print('현재 모듈의 사용 개체 목록 :', globals())


def isOdd(arg):
    return arg % 2 == 1


mydict = {x: x * x for x in range(11) if isOdd(x)}
print(mydict)

# 변수의 생존 범위
a, b, c = 10, 20, 30  # 전역 변수
print('1) a:{},b:{},c:{}'.format(a, b, c))


def fun1():
    a = 40  # fun1 함수 영역내에서 유효 지역변수
    b = 50

    def fun2():
        global c
        nonlocal b  # 잘안씀
        # c = 60  # fun2 함수 여역 내에서 유효
        print('2) a:{},b:{},c:{}'.format(a, b, c))
        c = 60
        b = 70

    fun2()
    print('3) a:{},b:{},c:{}'.format(a, b, c))


fun1()
print('n) a:{},b:{},c:{}'.format(a, b, c))


def showGugu(start, end=5):
    for dan in range(start, end + 1):
        print(str(dan) + '단 출력')


showGugu(2, 3)
showGugu(2)
showGugu(start=2, end=3)
showGugu(end=2, start=3)


def ff(a, b, *c, **d):
    print(a)
    print(b)
    print(c)
    print(d)


ff(1, 2, 3, 4, 5, m=6, n=7)
ff(1, 2, 3, 4, 5)


# 이름이 없는 함수 :lambda
def Hap(x, y):
    return x + y


print(Hap(1, 2))

print((lambda x, y: x + y)(1, 2))

gg = lambda x, y: x * y

print(gg)
print(gg(1, 2))

# filter(함수,집합형자료)

print(list(filter(lambda a: a < 5, range(10))))


# 장식자

def maker2(fn):
    return lambda: '안녕' + fn()


def maker1(fn):
    return lambda: '반가워' + fn()


def hello():
    return '홍길동'


hi = maker2(maker1(hello))
print(hi())


@maker2
@maker1
def hello2():
    return '신기해'


print(hello2())
