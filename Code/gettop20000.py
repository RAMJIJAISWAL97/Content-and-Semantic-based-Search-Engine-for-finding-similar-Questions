import json 
import time 
import sys 
from elasticsearch import Elasticsearch 
from elasticsearch.helpers import bulk 
import csv 
import tensorflow as tf 
import tensorflow_hub as hub 

f = open ('top20000data','w', encoding = 'latin1')

NUM_QUESTIONS_INDEXED = 20000

cnt = 0;

with open ('./data/Questions.csv', encoding = 'latin1') as csvfile :
  readCSV = csv.reader(csvfile, delimiter = ',')
  next(readCSV, None)
  for row in readCSV:
    doc_id = row[0]:
    title = row[5]:
    f.write(doc_id+","+tilte+"\n")
    cnt += 1
    if cnt % 100 == 0 :
      print(cnt)
    if cnt == NUM_QUESTIONS_INDEXED:
      break;
  print("done")
f.close()		