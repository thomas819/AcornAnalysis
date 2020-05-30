# mysqlclient설치
import MySQLdb
import pandas as pd
import numpy as np
import csv
import ast

config = {
    'host': '221.151.185.221',
    'user': 'root',
    'password': '1234',
    'database': 'test',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True
}

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()  # sql 실행
    sql = """
        select jikwon_no,jikwon_name,buser_name,jikwon_jik,jikwon_gen,jikwon_pay 
        from jikwon inner join buser
        on buser_num=buser_no    
    """
    cursor.execute(sql)
    for (a, b, c, d, e, f) in cursor:
        print(a, b, c, d, e, f)

        #    jikwon_no jikwon_name buser_name jikwon_jik jikwon_gen  jikwon_pay
        # 0          1         홍길동        총무부         이사          남        9900
        # 1         10         박치기        총무부         사원          남        3700
        # 2         13         박명화        총무부         대리          남        4900

    with open('jik_data.csv', 'w', encoding='utf-8') as fw:
        writer = csv.writer(fw)
        for row in cursor:
            writer.writerow(row)
    print('저장 완료')

except Exception as e:
    print('err : ' + str(e))

finally:
    pass
    # cursor.close()
    # conn.close()

# 읽기1 (csv 로읽기)
df1 = pd.read_csv('jik_data.csv', header=None, names=('번호', '이름', '부서', '직급', '성별', '연봉'))
print(df1.head(3))

#읽기 2(db서 바로 읽기)
df2 = pd.read_sql(sql, conn)
df2.columns=('번호', '이름', '부서', '직급', '성별', '연봉')
print(df2.head(3))

print(len(df2))

high = '직급'
m = '연봉'
s = '성별'

print(df2[high].count())
print(df2[high].value_counts())
print(df2.loc[:, [m]].mean())
print(df2.loc[:, [m]].describe())
ctab = pd.crosstab(df2[s], df2[high], margins=True)
print(ctab)
print(df2.pivot_table([m], index=[s, high], aggfunc=np.mean))

import matplotlib.pyplot as plt

plt.rc('font', family='malgun gothic')
jik_pay = df2.groupby([high])[m].mean()
print(jik_pay.index)
print(jik_pay.values)
plt.pie(jik_pay,
        labels=jik_pay.index,
        labeldistance=0.5,
        counterclock=False,
        explode=(0.2, 0, 0, 0.3, 0),
        shadow=True)
plt.show()
