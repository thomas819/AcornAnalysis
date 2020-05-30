import sqlite3

sql = 'create table if not exists test(product varchar(10),marker varchar(10),weight real,price integer )'
conn = sqlite3.connect(':memory:')  # ram에만존재 휘발성
# conn = sqlite3.connect('testdb')
conn.execute(sql)
conn.commit()

data1 = ('mouse', 'sam', '12.5', 5000)
data2 = ('keyboard', 'lg', '52.5', 25000)
stmt = "insert into test values(?,?,?,?)"
conn.execute(stmt, data1)
conn.execute(stmt, data2)
conn.commit()

cursor = conn.execute("select * from test")
rows = cursor.fetchall()
print(rows)

import pandas as pd

df1 = pd.DataFrame(rows, columns=['product', 'maker', 'weight', 'price'])
print(df1)

print()

df2 = pd.read_sql('select * from test', conn)#pandas의 sql 직접쓰기
print(df2)


