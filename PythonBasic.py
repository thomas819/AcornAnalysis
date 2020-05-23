v1 = '555'
v1 = 5
v1 = 5.1
print("{a}이다".format(a=v1))

print(7, type(7))
print(7.7, type(7.7))
print(3 + 4j, type(3 + 4j))
print(True, type(True))
print('sbs', type('sbs'))
print((1,), type((1,)))  # tuple 데이터 하나일떄 , 필수
print([1], type([1]))
print({1}, type({1}))
print({'k': 1}, type({'k': 1}))

v1 = v2 = v3 = 3
print(v1, v2, v3, end=' ')
print('aa')
print(format(3.56789, '10.3f'))  # 10번쨰의 소수3번쨰까지
print('나이가 {a}'.format(a=22))
print('나이는 {}이고 이름은 {}'.format(22, "haha"))
print('나이는 {1}이고 이름은 {0}'.format(22, "haha"))
print('나이는 {a}이고 이름은 {b}'.format(a=22, b="haha"))

v1, v2 = 10, 20
print(v1, v2)
v2, v1 = v1, v2
print(v1, v2)

v1, *v2 = (1, 2, 3, 4, 5)
v1, *v2 = 1, 2, 3, 4, 5
print(v1, v2)

*v1, v2, v3 = 1, 2, 3, 4, 5
print(v1, v2, v3)

print(5 + 3, 5 - 3, 5 / 3, 5 // 3, 5 % 3)
print(divmod(5, 3))
print('한' + '국')
print('한국' * 20)

a = 10
a = a + 1
a += 1  # ++,-- 없다
print(a)
print(a, -a, a * -1, --a)

print(bool(0), bool(1), bool(-12), bool(3.5), bool('aa'))
print(bool(False), bool(None), bool([]))

print('abc\nnbc\ta')
print(r'abc\nnbc\ta')  # r붙이면 그냥입력

