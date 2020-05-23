# pandas : Series,DataFrame 객체지원
# import pandas
# pandas.Series
from pandas import Series

obj = Series([3, 6, -5, 4])
# obj = Series((3, 6, -5, 4))
# obj = Series({3, 6, -5, 4}) # set type x
print(obj, type(obj))

obj = Series([3, 7, -5, 4], index=['a', 'b', 'c', 'd'])
print(obj)
import numpy as np

print(obj.sum(), ' ', sum(obj), ' ', np.sum(obj))
print(obj.values)
print(obj.index)
print()
print(obj['a'])
print(obj[['a']])
print(obj[0])
print()
print(obj[['a', 'b']])
print(obj['a':'c'])
print()
print(obj[2])
# print(obj[1, 4])
print(obj[[2, 1]])
print(obj > 0)
print('a' in obj)

names = {'mouse': 5000, 'keyboard': 25000, 'mornitor': 450000}
print(names)
obj = Series(names)
print(obj)
obj.index = ['마', '키', '모']
print(obj)
obj.name = '상품가격'
print(obj)

from pandas import DataFrame

df = DataFrame(obj)
print(df, type(df))

data = {
    'irum': ['호징어', '한국인', '신기해', '공기밥', '한가해'],
    'juso': ('신당동', '역삼동', '역삼동', '역삼동', '신사동'),
    'nai': [23, 25, 33, 27, 35]
}
print(data, type(data))
frame = DataFrame(data)
print(frame, type(frame))
print(frame['irum'])
print(frame.irum, type(frame.irum))
print()
print()
print(DataFrame(data, columns=['juso', 'irum', 'nai']))
frame2 = DataFrame(data, columns=['juso', 'irum', 'nai', 'tel'], index=['a', 'b', 'c', 'd', 'e'])
print(frame2)
frame2['tel'] = '111-111'
print(frame2)
val = Series(['222-222', '333-3333', '444-4444'], index=['b', 'c', 'e'])
frame2['tel'] = val
print(frame2.T)
print(frame2.values)
print(frame2.values[0, 2])
print(frame2.values[0:2])
print()
# frame3 = frame2.drop('d')
frame3 = frame2.drop('d', axis=0)  # 행 삭제
print(frame3)
frame4 = frame2.drop('juso', axis=1)  # 열 삭제
print(frame4)

print()

print((frame3['juso'].value_counts()))

# Series 재색인
data = Series([1, 3, 2], index=(1, 4, 2))
print(data)
data2 = data.reindex((1, 2, 4))
print(data2)
print()
# 재 색인 시 값 채우기
data3 = data2.reindex([0, 1, 2, 3, 4, 5])
print(data3)

data3 = data2.reindex([0, 1, 2, 3, 4, 5], fill_value=777)
print(data3)

data3 = data2.reindex([0, 1, 2, 3, 4, 5], method='ffill')  # nan 앞의 값을 씀 ffill ==pad
print(data3)
data3 = data2.reindex([0, 1, 2, 3, 4, 5], method='pad')  # nan 앞의 값을 씀 ffill ==pad
print(data3)
print()

data3 = data2.reindex([0, 1, 2, 3, 4, 5], method='bfill')  # nan 뒤의 값을 씀 backfill ==bfill
print(data3)

print()

# bool 처리
df = DataFrame(np.arange(12).reshape(4, 3), index=['1월', '2월', '3월', '4월'], columns=['강남', '강북', '서초'])
print(df)
print(df['강남'])
print(df['강남'] > 3)
print(df[df['강남'] > 3])
df[df < 3] = 0
print(df)
print()

print('-----loc(), iloc()-----')
print(df.loc['3월', :])
print(df.loc[:'2월'])
print(df.loc[:'2월', ['서초']])
print()

print(df.iloc[2])
print(df.iloc[2, :])

print(df.iloc[:3, 1:3])
print()
print()

# 범주화
import pandas as pd

price = [10.3, 5.5, 7.8, 3.6]
cut = [3, 7, 9, 11]  # 구간 기준값
re_cut = pd.cut(price, cut)
print(re_cut)
print(pd.value_counts(re_cut))

# Series
datas = Series(np.arange(1, 1001))
print(datas.tail(3))
re_cut2 = pd.qcut(datas, 3)
print(re_cut2)
print(pd.value_counts(re_cut2))
print()

# df 의 merge
df1 = pd.DataFrame({'data1': range(7), 'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b']})
print(df1)

df2 = pd.DataFrame({'data2': range(3), 'key': ['a', 'b', 'd'], 'data2': range(3)})
print(df2)

print()
print(pd.merge(df1, df2, on='key'))  # defalut = inner join
print(pd.merge(df1, df2, on='key', how='inner'))  # inner join
print()
print(pd.merge(df1, df2, on='key', how='outer'))  # outer join
print()
print(pd.merge(df1, df2, on='key', how='left'))  # left join
print()
print(pd.merge(df1, df2, on='key', how='right'))  # right join
print()


