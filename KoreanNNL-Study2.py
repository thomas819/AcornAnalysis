# 웹 자료를 읽어 형태소 분석 후 가공. 단어별 유사도 출력
import pandas as pd
from konlpy.tag import Okt

okt = Okt()
with open('daumnews.txt', mode='r', encoding='utf-8') as f:
    # print(f.read())
    lines = f.read().split('\n')
    print(len(lines))

wordDic = {}

for line in lines:
    datas = okt.pos(line)
    # print(datas)
    for word in datas:
        if word[1] == 'Noun':
            # print(word[0])
            if not (word[0] in wordDic):
                wordDic[word[0]] = 0
            wordDic[word[0]] += 1

print(wordDic)

# 단어 건수별 내림차순

keys = sorted(wordDic.items(), key=lambda x: x[1], reverse=True)
print(keys)

# DataFrame
wordList = []
countList = []

for word, count in keys[:20]:
    wordList.append(word)
    countList.append(count)

df = pd.DataFrame()
df['word'] = wordList
df['count'] = countList
print(df)

# word2vec : 단어의 의미를 알기위해 벡터화. 단어의 유사성을 파악 가능
results = []
with open('daumnews.txt', mode='r', encoding='utf-8') as fr:
    lines = fr.read().split('\n')

    for line in lines:
        datas = okt.pos(line, stem=True)
        print(datas)
        imsi = []
        for word in datas:
            if not word[1] in ['Number', 'Josa', 'Punctuation', 'Foreign', 'Suffix', 'Verb']:  # 없앨것들 명시
                imsi.append(word[0])
        imsi2 = (" ".join(imsi)).strip()
        results.append(imsi2)
print(results)

fileName = 'daumenews2.txt'
with open(fileName, mode='w', encoding='utf-8') as fw:
    fw.write('\n'.join(results))
    print('저장성공')

print()
# 워드 임베딩 중 word2vec
from gensim.models import word2vec

sentence = [['python', 'len', 'program', 'computer', 'say']]
model = word2vec.Word2Vec(sentence, min_count=1)
print(model.wv.most_similar('python'))

genObj = word2vec.LineSentence(fileName)
print(genObj)
model = word2vec.Word2Vec(genObj, size=100, window=10, min_count=2,
                          sg=1)  # size=차원,window = 주변단어(앞,뒤) 10개 # sg=0 (CBOW=주변단어가지고 중심단어 예측ex) 나는 ~에 간다) ,sg=1 (skip_Gram)
print(model)
model.init_sims(replace=True)  # 쓸대없는메모리 제거

# 1번만실행햄
# try:
#     model.save('news.model')
#     print('ok')
# except Exception as e:
#     print('err ', e)
print()
# model 읽기
model = word2vec.Word2Vec.load('news.model')
print(model.wv.most_similar(positive=['인증서']))
print(model.wv.most_similar(positive=['인증서'], topn=3))
print(model.wv.most_similar(positive=['인증서','브라우저'], negative=['발급']))
