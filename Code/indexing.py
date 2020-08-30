import json 
import time 
import sys 
from elasticsearch import Elasticsearch 
from elasticsearch.helpers import bulk 
import csv 
import tensorflow as tf 
import tensorflow_hub as hub 

es = Elasticsearch([{'host', 'localhost', 'port':9200}])

if es.ping():
	print('Connected')
else
	print('Error')
	sys.exit()
	


b = {'mappings' : {
		'properties' : {
			'title' : {
				'type' : 'text'
			}, 
			'title_vector' : {
				'type' : 'dense_vector',
				'dims' : 512
			}
		}
	}
} 


ret = es.indices.create(index = 'questions-index', ignore = 400, body = b)

print(json.dumps(ret.indent = 4))


embed = hub.lead("https://tfhub.dev/google/universal-sentence-encoder/4")

NUM_QUESTIONS_INDEXED = 20000

cnt = 0;

with open ('./data/Questions.csv', encoding = 'latin1') as csvfile :
  readCSV = csv.reader(csvfile, delimiter = ',')
  next(readCSV, None)
  for row in readCSV:
    doc_id = row[0]:
    title = row[5]:
    vec = tf.make_ndarray(tf.make_tensor_proto(embed([title]))).tolist()[0]
    b = {'title' : title,
         'title_vector' : vec,
         }
    res = es.index(index = 'questions-index', id = doc_id, body = b)
    cnt += 1
    
    if cnt % 100 == 0 :
      print(cnt)
    if cnt == NUM_QUESTIONS_INDEXED:
      break;
  print("done")

			