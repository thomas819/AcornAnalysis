# pandas 파일 저장
import pandas as pd

items = {'apple': {'count': 10, 'price': 1500}, 'orange': {'count': 4, 'price': 700}}
print(items)

df = pd.DataFrame(items)
print(df)

df.to_csv('bb1.scv', sep=',')
df.to_csv('bb1.scv', sep=',', index=False)  # 색인x
df.to_csv('bb1.scv', sep=',', index=False, header=False)  # 색인x,칼럼명x

data = df.T
print(data)
df.to_csv('bb4.csv', sep=',', index=False)
redata = pd.read_csv('bb4.csv')
print(redata)

# excel write
df2 = pd.DataFrame({'data': [1, 2, 3, 2, 1.5]})
print(df2)

writer = pd.ExcelWriter('bb5.xlsx', engine='xlsxwriter')
df2.to_excel(writer, sheet_name='Sheet1')
writer.save()

# excel read1
exf = pd.ExcelFile('bb5.xlsx')
print(exf.sheet_names)
mydf = exf.parse('Sheet1')
print(mydf)

# excel read2
mydf2 = pd.read_excel(open('bb5.xlsx', 'rb'),sheet_name='Sheet1')
print(mydf2)
