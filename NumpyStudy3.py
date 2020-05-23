# Transpose
import numpy as np

x = np.arange(1, 10).reshape(3, 3)
print(x)
print(x.T)  # 행과 열 바꾸기
print(x.transpose())  # 행과 열 바꾸기
print(x.swapaxes(0, 1))  # 행과 열 바꾸기

print(x, ' ', x.shape)
y = np.array([1, 0, 1])
print(y, ' ', y.shape)
z = np.empty_like(x)  # 구조 맞추기(배열방식?)
print(z)

print()

for i in range(3):
    z[i] = x[i] + y

print(z)
print()
kbs = np.tile(y, (3, 1))
print(kbs)
z = x + kbs
print(z)
print()

kbs = x + y  # broadcast
print(kbs)

# numpy : file i/o
print(x)
np.save('aa1', x)
np.savez('aa2', x)
np.savetxt('aa3', x)
imsi1 = np.load('aa1.npy')
imsi2 = np.loadtxt('aa3')
print(imsi1)
print(imsi2)

print()
mbc = np.loadtxt('abc.txt', delimiter=',')
print(mbc)

# 배열 행,열 추가
aa = np.eye(3)
print('aa=', aa)
bb = np.c_[aa, aa[2]]
print('bb=', bb)
cc = np.r_[aa, [aa[2]]]
print('cc=', cc)

print()
a = np.array([1, 2, 3])
print('a=', a)
print(a.reshape(3, 1))
print()

b = np.append(a, [4, 5])
print(b)
c = np.insert(a, 0, [6, 7])
print(c)
# d = np.delete(a, 1)
# d = np.delete(a, [1])
d = np.delete(a, [1, 2])
print(d)

print()

aa = np.arange(1, 10).reshape(3, 3)
print(aa)
print()
print(np.insert(aa, 1, 99))
print(np.insert(aa, 1, 99, axis=0))  # axis =행기준인지 열기준인지
print(np.insert(aa, 1, 99, axis=1))  # axis =행기준인지 열기준인지

print()

# 조건 연산
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
conditionData = np.array([True, False, True])
print(np.where(conditionData, x, y))
print()
aa = np.where(x >= 2)
print(aa)
print(x[aa])
print(np.where(x >= 2, 'T', 'F'))
print(np.where(x >= 2, x, x + 100))

print()

# 배열 결합
kbs = np.concatenate([x, y])
print(kbs)
x1, x2 = np.split(kbs, 2)
print(x1, x2)

# sampling : 복원 , 비복원
import random

li = np.array([1, 2, 3, 4, 5, 6, 7])
print(li)
# 복원
for _ in range(5):
    print(li[random.randint(0, len(li) - 1)], end=' ')

print()

# 비복원
print(random.sample(list(li), k=5))

print()
print(random.sample(range(1, 46), k=6))

print()
# 복원
print(list(np.random.choice(range(1, 46), 6)))
print(list(np.random.choice(range(1, 46), 6, replace=True)))
print()
# 비복원
print(list(np.random.choice(range(1, 46), 6, replace=False)))

# 가중치
ar = 'air book cat d e f god'
ar = ar.split(' ')
print(ar)
print(np.random.choice(ar, 3, p=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.5]))
