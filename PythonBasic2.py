# String
# 집합형 : str (순서 수정 가능,read only)
s = 'sequence'
print(type(s), ' ', s, ' ', len(s), ' ', s.count('e'))
print(s[0], ' ', s[1:5], s[::2], ' ', s[-4:-1], ' ', s[5:], ' ', s[:5])
# s[0]='l' # err
print(id(s))
s = 'kequence'
print(id(s))

s2 = 'kbs mbc'
s3 = s2.split(sep=' ')
print(s3, type(s3), ' ', s3[0])
print(' '.join(s3))

# List : 순서 있음 ,중복,수정 수정가능
a = [1, 2, 3]
b = [10, a, 1.5, True, 'a']
print(b)
print(b[0], ' ', b[1], ' ', b[1][1])
b[0] = 'korea'
b.append('a')  # 넣기
b.extend(['bb', 'cc'])  # 넣기
b.insert(0, 'good')  # 수정
b.remove('good')
del b[0]
print(b)

# tuple :list 와 유사 수정불가, 속도 빠름
# t = ('a', 'b', 'c', 'd', 'd')
t = 'a', 'b', 'c', 'd', 'd'
print(t)
tt = 1,
print(type(tt))
print(t[0])
# t[0]='ll' #error 수정불가
q = list(t)
q[0] = 'kk'
t = tuple(q)
print(t)

# set : 순서 없음,중복 x
a = {1, 2, 3, 4, 1, 4, 5}
print(a)
# print(a[0])
a.discard(1)  # 값에 의한 삭제
a.remove(2)  # 값에 의한 삭제
# a.discard(1)  # 값없으면 pass
# a.remove(2)  # 값없으면 error
print(a)

# dict :{'key':'value'} 순서없다,
myDic = dict(k1=1, k2='abc', k3=3.4)
print(myDic)

dic = {'파이썬': '뱀', '자바': '커피', '스프링': '봄'}
print(dic)
print(dic['자바'])
# print(dic[0]) #error 순서가없으니 에러
dic['오라클'] = '예언자'
print(dic)
del dic['오라클']
print(dic.get('자바'))

# 정규 표현식
import re

ss = '1234 abcAB가나다123_1234'
print(ss)
print(re.findall(r'123', ss))
print(re.findall(r'\d', ss))
print(re.findall(r'[0-9]', ss))
print(re.findall(r'[0-9]+', ss))
print(re.findall(r'[0-9]{2,3}', ss))
print(re.findall(r'[^0-9]+', ss))
print(re.findall(r'[가-힣]+', ss))


