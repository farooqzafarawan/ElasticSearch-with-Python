# Dealing with multiple indexes
Operations such as search and aggregations can run against multiple indexes in the same query. It is possible to specify which indexes should be searched by using different URLs in the GET request. Let's understand how the URLs can be used to search in different indexes and the types within them. We cover the following scenarios when dealing with multiple indexes within a cluster:
- Searching all documents in all indexes
- Searching all documents in one index
- Searching all documents of one type in an index
- Searching all documents in multiple indexes
- Searching all documents of a particular type in all indexes

### Match All Documents
The following query matches all documents. The documents that are actually returned by the query will be limited to 10 in this case. The default size of the result is 10, unless specified otherwise in the query:

`GET /_search`

This will return all the documents from all the indexes of the cluster. The response looks similar to the following, and it is truncated to remove the unnecessary repetition of documents:
```json
{
"took": 3,
"timed_out": false,
"_shards": {
"total": 16,
"successful": 16,
</span>"failed": 0
},
"hits": {
"total": 4,
"max_score": 1,
"hits": [
{
"_index": ".kibana",
"_type": "doc",
"_id": "config:7.0.0",
"_score": 1,
"_source": {
"type": "config",
"config": {
"buildNum": 16070
}
}
},
...
...
]
}
}
```

Clearly, this is not a very useful operation, but let's use it to understand the search response:
- **took**: The number of milliseconds taken by the cluster to return the result.
- **timed_out**: false: This means that the operation completed successfully without timing out.
- _shards: Shows the summary of how many shards across the entire cluster were searched for successfully, or failed.
- hits: Contains the actual documents that matched. It contains total, which signifies the total documents that matched the search criteria across all indexes. The max_score displays the score of the best matching document from the search hits. The hits child of this element contains the actual document list. 

### Hits List
The hits list contained within an array doesn't contain all matched documents. It would be wasteful to return everything that matched the search criteria, as there could be millions or billions of such matched documents. Elasticsearch truncates the hits by size, which can be optionally specified as a request parameter using `GET /_search?size=100`. 

The default value for the size is 10, hence the search hits array will contain up to 10 records by default.

## Searching all documents in one index
The following code will search for all documents, but only within the catalog index:
`GET /catalog/_search`

You can also be more specific and include the type in addition to the index name, like so:
`GET /catalog/_doc/_search`

The version with the _doc type name produces a deprecation warning because each index is supposed to contain only one type.

## Searching all documents in multiple indexes
The following will search for all the documents within the catalog index and an index named my_index:
`GET /catalog,my_index/_search`

## Searching all documents of particular type in all indexes
The following will search all the indexes in the cluster, but only documents of the product type will be searched:
`GET /_all/_doc/_search`

This feature can be quite handy when you have multiple indexes, with each index containing the exact same type. This type of query can help you query data for that type from all indexes.