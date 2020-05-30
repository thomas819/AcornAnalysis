# 선형회귀 : 독립변수 : 연속형, 종속변수 : 연속형
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf

iris = sns.load_dataset('iris')
print(iris.head(2))
print(iris.corr())  # 상관관계(데이터분포를 수치로 표현)

# 단순 선형회귀 모델
# result = smf.ols(formula='sepal_length ~ sepal_width', data=iris).fit()
result = smf.ols(formula='sepal_length ~ petal_length', data=iris).fit()
print('요약 결과 :', result.summary())

# y = wx+b ex)y= 0.4089 * x +4.3066
y = 0.4089 * 1.4 + 4.3066
print('실제값은 : 5.1,예측값 : ', y)

x = 2.3
y = 0.4089 * x + 4.3066
print('x=2.3일때 예측 값 :', y)
print()
# 다중 선형회귀
result = smf.ols(formula='sepal_length ~ petal_length + petal_width', data=iris).fit()
print(result.summary())

# 새로운 데이터로 예측값 얻기
new_data = pd.DataFrame({'petal_length': [1.4, 0.8, 8.0], 'petal_width': [0.4, 0.8, 2.0]})
y_pred = result.predict(new_data)
print(y_pred)

