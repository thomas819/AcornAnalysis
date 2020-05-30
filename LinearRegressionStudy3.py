# caggle =https://www.kaggle.com/lavanya321/mtcars?select=mtcars.csv
import statsmodels.api
import statsmodels.formula.api as smf
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
from dask.dataframe.core import Series

plt.rc('font', family='malgun gothic')

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
# print(mtcars.describe())
print(np.corrcoef(mtcars.hp, mtcars.mpg))  # hp=마력 /mpg=연비  상관관계 0.776 음의 상관관계 높음

plt.scatter(mtcars.hp, mtcars.mpg)
plt.xlabel('마력수')
plt.ylabel('연비')
slope, intercept = np.polyfit(mtcars.hp, mtcars.mpg, 1)  # 차수1
print(slope, intercept)
plt.plot(mtcars.hp, slope * mtcars.hp + intercept, 'b')
plt.show()

# 단순 성형회귀 모델
result = smf.ols(formula='mpg ~ hp', data=mtcars).fit()
# print(result.summary())  # w 기울기 : -0.0682 , 절편 : 30.0989 y = wx+b
print('임의의 마력 수 에 대한 연비 : ', -0.0682 * 110 + 30.0989)
print('임의의 마력 수 에 대한 연비 : ', -0.0682 * 130 + 30.0989)
print('임의의 마력 수 에 대한 연비 : ', -0.0682 * 50 + 30.0989)
print()

# 다중 회귀
result2 = smf.ols(formula='mpg ~ hp + wt', data=mtcars).fit()
# print(result2.summary())  # y=-0.318 * hp + -37.2273 * wt +37.2273
kbs = result2.predict()
print(kbs)

# 추정치 구하기 : 차체 무게를 입력해 연비 예측
result3 = smf.ols(formula='mpg ~ wt', data=mtcars).fit()
# print(result2.summary())
mbc = result3.predict()
print(mbc)
# print('실제값 : ' + mtcars.mpg[0])
# print('예측값 : ' + mbc[0])

data = {
    'mpg': mtcars.mpg,
    'wt': mtcars.wt,
    'mpg_pred': mbc
}
df = DataFrame(data)
print(df)

# 새로운 차체무게로 연비 예측
mtcars.wt = 6
ytn = result3.predict(DataFrame(mtcars.wt))
print('6톤 일 떄 연비는', ytn[0])

mtcars.wt = 8
ytn = result3.predict(DataFrame(mtcars.wt))
print('8톤 일 떄 연비는', ytn[0])

mtcars.wt = 0.5
ytn = result3.predict(DataFrame(mtcars.wt))
print('0.5톤 일 떄 연비는', ytn[0])

import pandas as pd

wt_new = pd.DataFrame({'wt': [6, 3, 0.4]})
mpgs = result3.predict(wt_new)
print("예상 연비 : ", mpgs)
