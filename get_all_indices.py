from elasticsearch import Elasticsearch
from elasticsearch import exceptions
import json

try:
    # declare an es client instance of the Python Elasticsearch library
    es = Elasticsearch([{'host': 'sl-febi', 'port': '9200'}])
except Exception as err:
    print ("Elasticsearch es ERROR:", err)
    es = None

# returns a list of all the cluster's indices
all_indices = es.indices.get_alias("*")

# print all the attributes for es.indices
print (dir(es.indices), "\n")

# iterate over the index names
for idx in all_indices:
    if idx.startswith('.') or idx.startswith('kibana') or idx=='hockey' or idx=='library' :
        #print(idx)
        pass
    else:
        print(idx)
        #es.indices.delete(index=idx, ignore=[400, 404])