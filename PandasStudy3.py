# pandas로 file i/o
import pandas as pd

df = pd.read_csv('testdata_utf8/ex1.csv')
print(df, type(df))
df = pd.read_table('testdata_utf8/ex1.csv', sep=',')
print(df)
print()
df = pd.read_csv('testdata_utf8/ex2.csv', header=None)
print(df)
print()
df = pd.read_csv('testdata_utf8/ex2.csv', names=['a', 'b', 'c', 'd', 'e'])
print(df, type(df))

print()
df = pd.read_csv('testdata_utf8/ex2.csv', names=['a', 'b', 'c', 'd', 'msg'], index_col='msg')
print(df, type(df))
print()

df = pd.read_csv('testdata_utf8/ex3.txt')
print(df)
print()
df = pd.read_csv('testdata_utf8/ex3.txt', sep='\s+')  # 정규표현식
print(df)

df = pd.read_csv('testdata_utf8/ex3.txt', sep='\s+', skiprows=[1, 3])  # 정규표현식
print(df)

print()
df = pd.read_fwf('testdata_utf8/data_fwt.txt', widths=(10, 3, 5), names=('data', 'name', 'price'), encoding='utf8')
print(df)
print()

# chunk (덩어리) 단위로 파일 자료 읽기
test = pd.read_csv('testdata_utf8/data_csv2.csv', header=None, chunksize=3)
print(test)
for p in test:
    # print(p)
    print(p.sort_values(by=2, ascending=True))
