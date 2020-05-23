# pandas
# 문제
# 3)  타이타닉
# 승객 데이터를 사용하여 아래의 물음에 답하시오.
# 데이터: http: // cafe.daum.net / flowlife / RUrO / 103
# https: // github.com / pykwon / python / blob / master / testdata_utf8 / titanic_data.csv

# titanic_data.csv
# 파일을 다운로드 후
# df = pd.read_csv('파일명', header=None,,, )

# 1) 성별, 선실(class or pclass), 나이대(소년, 청년, 장년, 노년)에 의한 생존율을 데이터프레임을 사용해 계산한다.
#
# 행에는 성별 및 나이에 대한 계층적 인덱스(pd.cut())를 사용하고, 열에는 선실 인덱스를 사용한다.
# bins =[1, 20, 35, 60, 150]
# labels =["소년", "청년", "장년", "노년"]
# df["age_cat"] = pd.cut(titanic["age"], bins, labels=labels)
#
# 2) 성별 및 선실에 대한 자료를 이용해서 생존율('survived')을 피봇테이블 형태로 작성한다.
#
# df.pivot_table()
import pandas as pd

dft = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/titanic_data.csv')
# print(dft.head(3))
print(dft.head(3))
bins = [1, 20, 35, 60, 150]
labels = ["소년", "청년", "장년", "노년"]
dft.Age = pd.cut(dft.Age, bins, labels=labels)

print(dft.tail(3))
print(dft.Age.value_counts())
print()
dft2 = dft.pivot_table(index=['Sex', 'Age'], columns='Pclass', values='Survived', fill_value=0)
print(dft2)
print(round(dft2 * 100, 1))
