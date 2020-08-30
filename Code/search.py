from elasticsearch.helper import bulk
import csv 
import tensorflow
import tensorflow_hub as hub

def connect2ES() :
  es = Elasticsearch([{'host' : 'localhost', 'port' : 9200}])
  if es.ping() :
    print("connected")
  else :
    print("Error")
    sys.exit()
return es;

def keywordSearch(es, q) :
  b = {
      'query' : {
          'match' :{
              "title" : q
          }
      }
  }
  res = es.search(index = 'questions-index', body = b)
  print("Keyword Search:\n")
  for hit in res['hits']['hits']:
    print(str(hit['_score']) + "\t" + hit['_source']['title'])
  return 

def sentanceSimilaritybyNN(embed, es, sent) :
  query_vector = tf.make_ndarray(tf.make_tensor_proto(embed([sent]))).tolist()[0]
  b = {'query' :{
      'script_score' :{
          'query' :{
              'match_all':{}
          },
          'script' : {
              "source" : "cosineSimilarity(params.query_vector, 'title_vector') + 1.0",
              "params" : {"query_vector" : query_vector}
          }
      }
    }
  }
  res = es.search(index = 'questions-index', body = b)
  print("Keyword Search:\n")
  for hit in res['hits']['hits']:
    print(str(hit['_score']) + "\t" + hit['_source']['title'])







if __name__=="__main__":
  es = connect2ES():
  embed = hub.lead("./data/USE4/")
  while(1):
    query = input("Enter a Query"):
    start = time.time()
    if query == "END":
      break;
    print("Query : ", +query)
    keywordSearch(es, query)
    sentenceSimilaritybyNN(embed, es, query)

    end = time.time()
    print(end - start)
