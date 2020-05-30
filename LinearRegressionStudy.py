# 최소 제곱해를 이용해 선형 행렬 방정식으로 만들기
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.9, 2.1])
plt.plot(x, y)
plt.grid(True)
plt.show()

A = np.vstack([x, np.ones(len(x))]).T
print(A)

import numpy.linalg as lin

# y = wx + b
w, b = lin.lstsq(A, y)[0]
print(w, b)

plt.plot(x, y, 'o', label='ori data', markersize=10)
plt.plot(x, w * x + b, 'r')
plt.show()
