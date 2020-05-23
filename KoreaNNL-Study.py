#konlpy 라이브러리 실행 전 java 설치 필수
#https://konlpy-ko.readthedocs.io/ko/v0.4.3/
#참고:http://cafe.daum.net/flowlife/RUrO/65

# from konlpy.tag import Kkma
#
# from konlpy.utils import pprint
#
# kkma = Kkma()
#
# print(kkma.sentences('여러분, 안녕하세요. 반갑습니다.'))
#
# print()
#
# print(kkma.nouns(u'오늘 폭염이 주춤했지만 일부지방은 폭염 특보 속에 35도 안팎의 찜통더위가 기승을 부렸는데요.자세한 날씨, YTN 중계차 연결해 알아보겠습니다.'))
#
# print()
#
# print(kkma.pos(u'오류보고는 실행환경, 에러메세지와 함께'))

from konlpy.tag import Okt

okt = Okt()
aa = okt.pos("멋진 봄은 엄청 무더운 ")
print(aa)

import urllib
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from urllib import parse

okt = Okt()

para = parse.quote("이순신")
print(para)
url = "https://ko.wikipedia.org/wiki/" + para

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), 'lxml')
print(soup)

wordlist = []
for item in soup.select("#mw-content-text > div > p"):
    if item.string != None:
        # print(item.string)
        ss = item.string
        wordlist += okt.nouns(ss)

print('단어 수 :', len(wordlist))

word_dict = {}
for i in wordlist:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1

print('word_dict: ', word_dict)

setdata = set(wordlist)  # set에 넣으면 중복제거
print(setdata)
print('단어 수 (중복제거) :', len(setdata))

print('pandas : Series ---')
import pandas as pd

woList = pd.Series(wordlist)
print(woList[:3])
print(woList.value_counts()[:5])
print()
woDict = pd.Series(word_dict)
print(woDict[:3])
print(woDict.value_counts())

print('--dataframe--')
df1 = pd.DataFrame(wordlist, columns=['단어'])
print(df1.head())
print()
df2 = pd.DataFrame([word_dict.keys(), word_dict.values()])
print(df2)
df2 = df2.T
df2.columns = ['단어', '빈도수']
print(df2.head())

df2.to_csv('이순신.csv', sep=',', index=False)
df3 = pd.read_csv('이순신.csv')
print(df3)
