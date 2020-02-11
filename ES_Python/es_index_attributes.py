from elasticsearch import Elasticsearch

try:
    # declare an es client instance of the Python Elasticsearch library
    es = Elasticsearch([{'host': 'sl-febi', 'port': '9200'}])
except Exception as err:
    print ("Elasticsearch es ERROR:", err)
    es = None

# returns a list of all the cluster's indices
all_indices = es.indices.get_alias("*")

# print all the attributes for es.indices
idx_attribs = dir(es.indices)

# iterate over the index names
for attr in idx_attribs:
    if attr.startswith('__'): #or idx.startswith('kibana') or idx=='hockey' or idx=='library' :
        #print(attr)
        pass
    else:
        print(attr)
        #es.indices.delete(index=idx, ignore=[400, 404])