from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote

keyword = input('검색어:')
print(keyword)
print(quote(keyword))
target_url = 'https://www.donga.com/news/search?query=' + quote(keyword)
print(target_url)

source_code = urllib.request.urlopen(target_url)
soup = BeautifulSoup(source_code, 'lxml', from_encoding='utf-8')
# print(soup)
msg = ""
for title in soup.find_all('p', 'tit'):
    title_link = title.select('a')
    # print(title_link)
    a_url = title_link[0]['href']
    # print(a_url)
    source_article = urllib.request.urlopen((a_url))
    soup = BeautifulSoup(source_article, 'lxml', from_encoding='utf-8')

    contents = soup.select('div.article_txt')
    for imsi in contents:
        item = str(imsi.find_all(text=True))
        # print(item)
        msg = msg + item

print(msg)

from konlpy.tag import Okt
from collections import Counter

nlp = Okt()
nouns = nlp.nouns(msg)
result = []
for imsi in nouns:
    if len(imsi) > 1:
        result.append(imsi)
print(result)
count = Counter(result)
print(count)

tag = count.most_common(50)  # 상위 50개 단어만 워드 클라우드에 참여시킨다

import pytagcloud

taglist = pytagcloud.make_tags(tag, maxsize=100)
print(taglist[:10])

pytagcloud.create_tag_image(taglist, 'word.png', size=(1280, 960), fontname='korean', rectangular=False)#한글지원안됨C:\Users\{user}\Anaconda3\Lib\site-packages\pytagcloud\fonts 안에 폰트 넣고 fonts.json 파일 열어서 name 과 ttf 설정 한다fontname에 name명을 입력하면됨

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('word.png')
plt.imshow(img)
plt.show()

import webbrowser
webbrowser.open('word.png')