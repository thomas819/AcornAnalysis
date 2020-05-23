# XML 읽기
import urllib.request as req
from bs4 import BeautifulSoup

url = "http://openapi.seoul.go.kr:8088/sample/xml/SeoulLibraryTime/1/5/"
plainText = req.urlopen(url).read().decode()
# print(plainText)
xmlObj = BeautifulSoup(plainText, 'lxml')
libData = xmlObj.select("row")
# print(libData)
for d in libData:
    name = d.find('lbrry_name').text
    addr = d.find('adres').text
    print('도서관명 : ', name, end=' ')
    print('주소 : ', addr)

# JSON 읽기
import json

url = "http://openapi.seoul.go.kr:8088/sample/json/SeoulLibraryTime/1/5/"
plainText = req.urlopen(url).read().decode()
# print(plainText, ' ', type(plainText))#<class 'str'>
jsonData = json.loads(plainText)  # json decoding (str ->dict)
print(jsonData, ' ', type(jsonData))  # <class 'dict'>
print(jsonData['SeoulLibraryTime']['row'][0]['LBRRY_NAME'])

print("json incoding dict-->str")
libData = jsonData.get('SeoulLibraryTime').get('row')
# print(libData)

name = libData[0].get('LBRRY_NAME')
print(name)
print("--------")
for ele in libData:
    name = ele.get('LBRRY_NAME')
    tel = ele.get('TEL_NO')
    addr = ele.get('ADRES')
    print(name+"\t"+tel+"\t"+addr)



#C:\Users\thomas\Desktop