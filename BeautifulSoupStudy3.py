# 방법1
import urllib.request
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
data = urllib.request.urlopen(url).read()

soup = BeautifulSoup(data, 'lxml')
# print(soup)
# print(soup.select('div.tit3'))#==soup.select('div[class=tit3]')
for t in soup.select('div[class=tit3]'):
    print(t.text.strip())

# 방법2
import requests

data = requests.get(url)
print(data.status_code, ' ', data.encoding)  # 다른정보를 더 가져올수있음
datas = data.text
soup = BeautifulSoup(datas, 'lxml')
# print(datas)
m_list = soup.findAll("div", {"class": "tit3", })  # ==m_list = soup.findAll("div","tit3")
print(m_list)

print()


class Gogo():
    def start(self):
        url = "https://datalab.naver.com/keyword/realtimeList.naver"
        page = requests.get(url,headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'})#원래 안되던것 header달면 됨 headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

        soup = BeautifulSoup(page.text, 'lxml')
        #print(soup)
        title = soup.select('span.item_title')
        #print(title)
        print('<네이버 실시간 검색어>')
        count=0
        for i in title:
            count +=1
            print(str(count) + ")"+i.string)

if __name__ == '__main__':
    Gogo().start()
