import urllib.request as req
import bs4

# <div id="kakaoIndex">
#    <a href="#kakaoBody">본문 바로가기</a>
#    <a href="#kakaoGnb">메뉴 바로가기</a>
#   </div>


# url = "https://news.v.daum.net/v/20200523110832326"
# daum = req.urlopen(url)
# print(daum)
# soup = bs4.BeautifulSoup(daum, 'lxml')
# print(soup.select_one('div#kakaoIndex > a').string)
# datas = soup.select('div#kakaoIndex a')
# print(datas)
# print()
# for i in datas:
#     href = i.attrs['href']
#     text = i.string
#     print("href:{},text:{}".format(href, text))
# print()
#
# datas2 = soup.findAll('a')
# print(datas2)
#
# for i in datas2[:2]:
#     href = i.attrs['href']
#     text = i.string
#     print("href:{},text:{}".format(href, text))

print()
print()

# BBQ 홈페이지 자료
# <div class="box">
# 							<div class="img">
# 								<a href="./menuView.asp?midx=1080&amp;cidx=0&amp;cname=%EB%AA%A8%EB%93%A0+%EB%B9%84%EB%B9%84%ED%81%90%EC%B9%98%ED%82%A8"><img src="https://img.bbq.co.kr:449/uploads/bbq_d/thumbnail/레드착착_찐킹.png" alt="" width="330px" height="330px"></a>
# 								<ul class="over">
# 									<!-- <li class="cart"><a href="javascript: mobile_cart_window_open()"> 장바구니</a></li> -->
# 									<li class="dir"><a href="javascript: mobile_order_window_open();"> 온라인주문</a></li>
# 								</ul>
# 							</div>
# 							<div class="info">
# 								<p class="name">핫황금올리브™콤보반반(레드착착+찐킹소스)</p>
# 								<p class="sum">레드착착+찐킹소스</p>
# 								<p class="pay">19,000원</p>
# 							</div>
# 						</div>
url = "https://www.bbq.co.kr/menu/menuList.asp"
bbq = req.urlopen(url)
# print(bbq)
soup = bs4.BeautifulSoup(bbq, 'lxml')
# print(soup)
data1 = soup.select('div.box > div.info > p.name')
print(data1)
data2 = soup.select('div.box > div.info > p.pay')

name = []
pay = []

for tb in data1:
    name.append(tb.text)

for tb in data2:
    # pay.append(tb.text)
    pay.append(int(tb.text.replace(',', '').replace('원', '')))

# print(name)
print(pay)

datas = {'name': name, 'pay': pay}
from pandas import DataFrame

df = DataFrame(datas)
print(df.head(3))

print("가격 평균 : ", round(df['pay'].mean(), 1))
print("가격 표준편차 : ", round(df['pay'].std(), 1))

#content > div.section.inner_sub > table.type2 > tbody > tr > td.title > a