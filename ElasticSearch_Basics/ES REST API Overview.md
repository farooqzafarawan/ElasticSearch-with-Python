# REST API overview
Elasticsearch supports a wide variety of operation types. Some operations deal with documents, that is, creating, reading, updating, deleting, and more. Some operations provide search and aggregations, while other operations are for providing cluster-related operations,such as monitoring health. Broadly, the APIs that deal with Elasticsearch are categorized into the following types of APIs:
- Document APIs
- Search APIs
- Aggregation APIs
- Indexes APIs
- Cluster APIs
- cat APIs

We will conceptually understand, with examples, how the APIs can be leveraged to get the best out of Elasticsearch and the other components of the Elastic Stack.

## Common API conventions
All Elasticsearch REST APIs share some common features. They can be used across almost all APIs. In this section, we will cover the following features:
- Formatting the JSON response
- Dealing with multiple indexes

## Formatting JSON response
By default, the response of all the requests is not formatted. It returns an unformatted JSON string in a single line:

`curl -XGET http://localhost:9200/catalog/_doc/1`

The following response is not formatted:
```json
{"_index":"catalog","_type":"product","_id":"1","_version":3,"found":true,"_source":{
"sku": "SP000001",
"title": "Elasticsearch for Hadoop",
"description": "Elasticsearch for Hadoop",
"author": "Vishal Shukla",
"ISBN": "1785288997",
"price": 26.99
}}
```

Passing pretty=true formats the response:
```json
curl -XGET http://localhost:9200/catalog/_doc/1?pretty=true
{
    "_index" : "catalog",
    "_type" : "product",
    "_id" : "1",
    "_version" : 3,
    "found" : true,
    "_source" : {
        "sku" : "SP000001",
        "title" : "Elasticsearch for Hadoop",
        "description" : "Elasticsearch for Hadoop",
        "author" : "Vishal Shukla",
        "ISBN" : "1785288997",
        "price" : 26.99
        }
}
```

When you are using the Kibana Console UI, all responses are formatted by default. 

