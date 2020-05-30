# 분류 모형 중 logistic regression을 이용해 날씨 예측(비 여부)
import pandas as pd
from sklearn.model_selection._split import train_test_split
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np

data = pd.read_csv('https://raw.githubusercontent.com/thomas819/AcornAnalysis/master/testdata_utf8/weather.csv')
print(data.head(2), data.shape)
data2 = pd.DataFrame()
data2 = data.drop(['Date', 'RainToday'], axis=1)
data2['RainTomorrow'] = data2['RainTomorrow'].map({'Yes': 1, 'No': 0})
print(data2.head(2))

print(data2.head(2), data2.shape)  # 366.10

# train / test dataset으로 분리해서 모델 학습시 train,모델 평가시 test dataset
train, test = train_test_split(data2, test_size=0.3, random_state=42)
print(train.shape, test.shape)  # (256, 10)(110, 10)

# 분류 모델
# my_formula = 'RainTomorrow ~ MinTemp + MaxTemp + Rainfall .....'
col_select = "+".join(train.columns.difference(['RainTomorrow']))
# print(col_select)
my_formula = 'RainTomorrow ~' + col_select
print(my_formula)
# result = smf.glm(formula=my_formula, data=train, family=sm.families.Binomial()).fit()
result = smf.logit(formula=my_formula, data=train).fit()
# print(result.summary())
# print(result.params)
#학습데이터로
conf_mat = result.pred_table()
print(conf_mat)
print('분류 정확도 :', (conf_mat[0][0] + conf_mat[1][1])/len(train))

from sklearn.metrics import accuracy_score
pred = result.predict(test)
#print(np.around(pred))
print('분류 정확도 :',accuracy_score(test['RainTomorrow'],np.around(pred)))