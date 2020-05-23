# 제어문

var = 1

if var >= 3:
    print("크쿤")
    print('참')
else:
    print('거짓')

print('end1')

jum = 78
if jum <= 90 <= 100:
    print('A')
elif 70 <= jum < 90:
    print('B')
else:
    print('C')

a = 'kbs'
b = 9 if a == 'kbs' else 11
print(b)
a = 11
b = 'mbc' if a == 9 else 'kbs'
print(b)

# while
a = 1
while a <= 5:
    print(a, end='  ')
    a += 1
print()
colors = ['r,', 'g', 'b']
a = 0
while a < len(colors):
    print(colors[a], end=' ')
    a += 1

print()

import time

sw = input('폭탄 스위치를 누를까요(y/n)')
if sw == 'Y' or sw == 'y':
    count = 5
    while 1 <= count:
        print("{}초 남았어요".format(count))
        time.sleep(1)  # 1초
        count -= 1
    print('폭발')
elif sw == 'N' or sw == 'n':
    print('작업 취소')
else:
    print('Y or n 입력')

a = 0
while a < 10:
    a += 1
    if a == 5: continue
    if a == 7: break
    print(a)
else:
    print('while 정상 수행')

print()
while True:  # = while 1 :
    a = int(input('확인할 숫자'))
    if a == 0:
        print('종료')
        break
    elif a % 2 == 0:
        print("짝수")
        continue
    elif a % 2 == 1:
        print("홀수")
        continue

# for
for i in [1, 2, 3, 4, 5]:  # {1,2,3,4,5} , (1,2,3,4,5)
    print(i, end=' ')
print()

soft = {'java': 'a', 'python': 'b', 'oracle': 'c'}
print(soft)
for i in soft.items():
    print(i)

for i in soft.keys():
    print(i)

for i in soft.values():
    print(i)

for k, v in soft.items():
    print(k, ' ', v)

datas = [1, 2, 'a', True, 3]
li = [i * i for i in datas if type(i) == int]
print(li)

datas = {1, 1, 2, 2, 3}
se = {i + i for i in datas}
print(se)

id_name = {1: 'tom', 2: 'james'}
print(id_name)
name_id = {val: key for key, val in id_name.items()}
print(name_id)

print('과일값 계산')
price = {'사과': 500, '수박': 12000, '참외': 1000}
my = {'사과': 3, '수박': 1}
bill = sum(price[f] * my[f] for f in my)
print(bill)
print()

print(list(range(1, 6)))
print(list(range(6)))
print(list(range(1, 10, 3)))
tot = 0
for i in range(1, 11):
    tot += i
print('합은' + str(tot))
print(sum(range(1, 11)))
