# iris dataset으로 시각화
import pandas as pd
import matplotlib.pyplot as plt

iris_data = pd.read_csv("https://raw.githubusercontent.com/thomas819/AcornAnalysis/master/testdata_utf8/iris.csv")
print(iris_data.head(3))

plt.scatter(iris_data['Sepal.Length'], iris_data['Petal.Length'])
plt.show()

from pandas.plotting import scatter_matrix

iris_col = iris_data.loc[:, 'Sepal.Length': 'Petal.Width']
scatter_matrix(iris_col, diagonal='kde')
plt.show()

print(iris_data['Species'].unique())
print(set(iris_data['Species']))
cols = []
for s in iris_data['Species']:
    choice = 0
    if s == 'setosa': choice = 1
    if s == 'versicolor': choice = 2
    if s == 'virginica': choice = 3
    cols.append(choice)

plt.scatter(iris_data['Sepal.Length'], iris_data['Petal.Length'], c=cols)
plt.show()

import seaborn as sns

sns.pairplot(iris_col)#, hue='species',height=3
plt.show()

print()

x =iris_data['Sepal.Length'].values
print(x)
sns.rugplot(x)
plt.show()
