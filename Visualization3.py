# yahoo 지원 주식자료 읽어 시각화
import pandas as pd
from pandas_datareader import data

kosdaq = pd.read_pickle('testdata_utf8/kosdaq.pickle')
kospi = pd.read_pickle('testdata_utf8/kospi.pickle')

print(kosdaq)
print(kospi)
start_date = '2018-01-01'
tikers = ['003380.KQ', '000060.KS']
holding_df = data.get_data_yahoo(tikers[0], start_date)
maritz_df = data.get_data_yahoo(tikers[1], start_date)
print(holding_df.head(3))
print(maritz_df.head(3))

holding_df.to_csv('./holding.csv')
maritz_df.to_csv('./metriz.csv')
holding_df.to_csv('./holding.pickle')
maritz_df.to_csv('./metriz.xls')

import matplotlib.pyplot as plt

plt.plot(holding_df)
plt.show()
plt.plot(maritz_df)
plt.show()

# pandas 의 plot 기능
import numpy as np

np.random.seed(0)

df = pd.DataFrame(np.random.randn(10, 3), index=pd.date_range('1/1/1919', periods=10), columns=['a', 'b', 'c'])
print(df)
df.plot(kind='bar')
plt.xlabel('time')
plt.ylabel('data')
plt.show()

