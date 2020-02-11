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
es_idx_settings = es.indices.get_settings( idx_name )
print ("get_settings() response:")
#print(json.dumps(es_idx_settings, indent=4))

# Get the dict object’s keys to access the setting fields
setting_keys = es_idx_settings[idx_name]["settings"]
print ("\n_setting keys():", setting_keys)

dict_analysis = setting_keys['index']['analysis'] 
for key in dict_analysis:
    print(key)
    if key in ('filter','analyzer'):
        for filter in dict_analysis[key]:
            print(filter, dict_analysis[key][filter] , sep='\n')
    else:
        print(json.dumps(dict_analysis[key], indent=4) )

