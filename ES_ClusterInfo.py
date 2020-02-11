from elasticsearch import Elasticsearch
from elasticsearch import exceptions
import json

try:

    # declare a client instance of the Python Elasticsearch library
    client = Elasticsearch([{'host': 'sl-febi', 'port': '9200'}])

    # pass client object to info() method
    elastic_info = Elasticsearch.info(client)
    print ("Cluster info:", json.dumps(elastic_info, indent=4 ))

except Exception as err:
    print ("Elasticsearch client ERROR:", err)
    client = None