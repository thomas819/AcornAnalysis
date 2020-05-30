# 시각화
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False  # 한글깨짐방지

x = ['서울', '인천', '수원']
y = [5, 3, 7]
plt.plot(x, y)
plt.xlim([-1, 3])
plt.ylim([0, 10])
plt.yticks(list(range(0, 11, 3)))  # y축
plt.show()

data = np.arange(1, 11, 2)
print(data)
plt.plot(data)
plt.show()

plt.plot(data)
plt.plot(data, data, 'r')
for a, b in zip(data, data):
    plt.text(a, b, str(b))
plt.show()

x = np.arange(10)
y = np.sin(x)
print(x, y)
# plt.plot(x, y)
# plt.plot(x, y, 'bo')
# plt.plot(y,'rt')
plt.plot(x, y, 'go--', linewidth=2, markersize=12)
plt.show()

x = np.arange(0, np.pi * 3, 0.1)
print(x)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.figure(figsize=(10, 5))
plt.plot(x, y_sin, 'r')
plt.scatter(x, y_cos)
plt.xlabel('x축')
plt.ylabel('y축')
plt.legend(['sine', 'cosine'])
plt.title('사인과 코사인')
plt.show()

# subplot
plt.subplot(2, 1, 1)
plt.plot(x, y_sin)
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.show()

irum = ['a', 'b', 'c', 'd', 'e']
kor = [80, 50, 70, 70, 90]
eng = [60, 70, 80, 70, 60]
plt.plot(irum, kor, 'ro-')
plt.plot(irum, eng, 'gs-')
plt.ylim([0, 100])
plt.legend(['국어', '영어'], loc=3)
plt.grid(True)

fig = plt.gcf()
plt.show()
fig.savefig('test.png')

from matplotlib.pyplot import imread

img = imread('test.png')
plt.imshow(img)
plt.show()

# 명시적으로 차트 객체 영역 선언
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.hist(np.random.randn(10), bins=10, alpha=0.9)
ax2.plot(np.random.randn(10))
plt.show()

data = [50, 80, 100, 70, 90]
plt.bar(range(len(data)), data)
plt.show()
plt.barh(range(len(data)), data)
plt.show()

error = np.random.rand(len(data))
plt.barh(range(len(data)), data, xerr=error)
plt.show()

plt.boxplot(data)
plt.show()

import pandas as pd

fdata = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range('1/1/2000',
                                                                   periods=1000), columns=list('ABCD'))
print(fdata.head(3))
fdata = fdata.cumsum()
print(fdata.head(3))
plt.plot(fdata)
plt.show()
