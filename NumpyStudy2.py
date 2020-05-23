# numpy : 핵심 라이브러리, ndarray
import numpy as np

ss = ['tom', 'james', 'oscar']
print(ss, type(ss))

ss2 = np.array(ss)
print(ss2, type(ss2))

li = list(range(1, 10))
print(li)
print(id(li[0]), id(li[1]))
print(li * 10)
print('**' * 10)
for i in li:
    print(i * 10, end=' ')

print()
ar = np.array(li)
print(ar)
print(id(ar[0]), id(ar[1]))
print(ar * 10)

a = np.array([1, 2, 3.])  # 1차원
print(a, type(a), a.dtype, a.shape, a.ndim, a.size)
print(a[0], a[2])
a[0] = 5
print(a)
print()

b = np.array([[1, 2, 3], [4, 5, 6]])  # 2차원
print(b.shape)
print(b[0], b[0, 0])
print(b[0], ' ', b[[0]])
print()

c = np.zeros((2, 2))
print(c)
d = np.ones((2, 2))
print(d)
e = np.full((2, 2), 7)
print(e)
f = np.eye(3)
print(f)

print()
np.random.seed(12)  # 난수고정
print(np.random.rand(5))  # rand 균등분포
print(np.random.randn(2, 2))  # randn 정규분포
print(np.random.randint(10, size=6))  # 정수
print(np.random.randint(10, size=(2, 3)))  #
print(np.random.randint(10, size=(3, 2, 5)))  #

# 슬라이싱
a = np.array([1, 2, 3, 4, 5])
print(a[0], ' ', a[:3], ' ', a[3:], ' ', a[::2], ' ', a[2:5])
print()

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a, ' ', a[1:])
print(a[0], ' ', a[0][0], ' ', a[0, 0])
b = a[:2, 1:3]
print(b)
print(b[0, 1])
print(b[0, 0])
b[0, 0] = 88  # a도 같이 적용됨
print(a)
print(b)
print()
c = a[1:3].copy()  # sub배열 만들기 copy안하면 부모도 같이적용되기떄문
print(c)
c[0, 0] = 77
print(c)
print(a)

# 배열 연산
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.arange(5, 9).reshape(2, 2)
y = y.astype(np.float32)
print('x', x)
print('y', y)
print()
print('x+y', x + y)
print(np.add(x, y))
print('np.add(x, y)', x * y)
print("(np.multiply(x, y)", np.multiply(x, y))  # 곱셈

# 벡터의 내적
v = np.array([9, 10])
w = np.array([11, 12])

print(v.dot(w))
print(np.dot(v, w))

print()
print(x.dot(v))
