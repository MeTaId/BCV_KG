# -*- codeing = uft-8 -*-

import json
from stanfordcorenlp import StanfordCoreNLP
import requests

#文件的位置
nlp = StanfordCoreNLP(r'./stanford-corenlp-4.5.3')





sentence = 'bovine rotavirus A (RVA) and Bovine coronavirus (BCoV) are the two main viral enteropathogens associated with neonatal calf diarrhea.'
output = nlp.annotate(sentence, properties={
    'annotators': 'tokenize, ssplit, pos, depparse, parse, openie',
    "openie.triple.strict": "true",
    'outputFormat': 'json'
    })
data = json.loads(output)
print(data)
import json
path = './data/sentence.txt'

num_id = []
with open(path, 'r', encoding='utf-8') as f:
    data = f.readline()
    num_id.append(data)

for i in range(0,len(num_id)):
    print("正在标记第{}条句子！".format(int(i)))
output = nlp.annotate(data, properties={
    'annotators': 'tokenize, ssplit, pos, depparse, parse, openie',
    'outputFormat': 'json'
})

# 将json格式的output转为Python对象
data = json.loads(output)


# 获取 openie 信息
for sentence in data['sentences']:
    for triple in sentence['openie']:
        subject = triple['subject']
        relation = triple['relation']
        obj = triple['object']

        print(f"Subject: {subject}\tRelation: {relation}\tObject: {obj}")

