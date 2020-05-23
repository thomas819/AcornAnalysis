##참고 : http://cafe.daum.net/flowlife/RUrO/21
#이메일 리스트 크롤링할떄 씀,정보주고 크롤링해야할떄 씀
from selenium import webdriver

#browser = webdriver.Chrome('C:/Users/thomas/Desktop/chromedriver')# 브라우저 열기

#browser.implicitly_wait(5)         #        <== 선택적인 명령으로 지정한 시간(초)동안 기다린다.
#browser.get('https://daum.net')   #       <== 원하는 url을 적어 줌. 해당 사이트가 열린다.
#browser.quit()                    #         <== 모든 작업을 끝내고 브라우저를 닫음


from selenium import webdriver

try:

    url = "http://www.daum.net"
    browser = webdriver.Chrome('C:/Users/thomas/Desktop/chromedriver')
    browser.implicitly_wait(3)
    browser.get(url)
    browser.save_screenshot("daum_img.png")
    browser.quit()
    print('성공')

except Exception:

    print('에러')