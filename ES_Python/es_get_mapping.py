from elasticsearch import Elasticsearch
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

idx_name = 'cwc_customer'

# returns dict object of the index _mapping schema
es_idx_mapping = es.indices.get_mapping( idx_name )
print ("get_mapping() response:")
#print(json.dumps(es_idx_mapping, indent=4))

# Get the dict object’s keys to access the mapping’s fields
mapping_keys = es_idx_mapping[idx_name]["mappings"]["properties"]
print ("\n_mapping keys():", mapping_keys)

for key in mapping_keys:
    print(key)
    print(json.dumps(mapping_keys[key], indent=4) )

