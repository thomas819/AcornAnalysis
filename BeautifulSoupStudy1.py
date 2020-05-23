import requests
from bs4 import BeautifulSoup

html_data = """
    <html><body>
    <h1>제목</h1>
    <p>웹문서 분석</p>
    <p>자료 추츨</p>
    </body></html>
"""

print(type(html_data))
soup = BeautifulSoup(html_data, 'html.parser')
print(type(soup))
print(soup)
h1 = soup.html.body.h1
print('h1 :', h1, ' ', h1.string)  # h1에 있는 string얻기
p1 = soup.html.body.p
print('p1 : ', p1, ' ', p1.string)
p2 = p1.next_sibling.next_sibling
print('p2 : ', p2, ' ', p2.string)

html_data2 = """
    <html><body>
    <h1>제목</h1>
    <p>웹문서 분석</p>
    <p id='my'>자료 추츨</p>
    </body></html>
"""

soup2 = BeautifulSoup(html_data2, 'lxml')
print(soup2.p, ' ', soup2.p.string)
print(soup2.find('p'), ' ', soup2.find('p').string)  # p태그의 string
print(soup2.find('p', id='my'))  # p태그의 id=my인것 찾기
print(soup2.find_all('p'))  # p태그 다 list로

print()

html_data3 = """
    <html><body>
    <h1>제목</h1>
    <p>웹문서 분석</p>
    <p id='my'>자료 추츨</p>
    <div>
        <a h href='http://www.naver.com'>naver</a>
        <a h href='http://www.daum.net'>daum</a>
    </div>
    </body></html>
"""
soup3 = BeautifulSoup(html_data3, 'lxml')
print(soup3.find('a'))
print(soup3.find('a').string)
print(soup3.find(['a']))
print(soup3.find_all(['a']))
print(soup3.find_all('a'))
print(soup3.findAll('a'))
# print(soup3)
# print(soup3.prettify()) #예쁘게 보여줌
print()
print()
links = soup3.find_all('a')
print(links)
for i in links:
    href = i.attrs['href']
    text = i.string
    print(href, ' ', text)

print()
print()

import re

links2 = soup3.find_all(href=re.compile(r'^http://'))
print(links2)
print()
print(soup3.find_all(['h1', 'p']))
