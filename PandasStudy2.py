# 그룹화 : group, pivot - 행열을 재구성하여 숫자 컬럼에 연산을 수행
import numpy as np
import pandas as pd

data = {'city': ['강남', '강북', '강남', '강북', ], 'year': [2000, 2001, 2002, 2002], 'pop': [3.3, 2.5, 3.0, 2.0]}
df = pd.DataFrame(data)
print(df)

print(df.pivot('city', 'year', 'pop'))
print()
print(df.set_index(['city', 'year']).unstack())
print()
print(df['pop'].describe())
print()
print()

print(df)
print(df.pivot_table(index=['city']))
print(df.pivot_table(index=['city'], aggfunc=np.mean))
print(df.pivot_table(index=['city', 'year'], aggfunc=[len, np.mean]))

print(df.pivot_table(['pop'], index='city'))
print(df.pivot_table(['pop'], index='city', aggfunc=len))  # np.mean : default

print()
print(df.pivot_table(['pop'], index=['year'], columns=['city']))
print(df.pivot_table(['pop'], index=['year'], columns=['city'], margins=True))
print(df.pivot_table(['pop'], index=['year'], columns=['city'], margins=True, fill_value=0))
print()

hap = df.groupby(['city'])
print(hap)
print(hap.sum())
print(df.groupby(['city']).sum())
print(df.groupby(['city', 'year']).mean())
