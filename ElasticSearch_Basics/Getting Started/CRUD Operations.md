# CRUD Operations
We will look at how to perform basic CRUD operations, which are the most fundamental operations required by any data store. Elasticsearch has a very well-designed REST API, and the CRUD operations are targeted at documents. 

To understand how to perform CRUD operations, we will cover the following APIs. These APIs fall under the category of document APIs, which deal with documents:

- Index API
- Get API
- Update API
- Delete API

# Index API
In Elasticsearch terminology, adding (or creating) a document to a type within an index of Elasticsearch is called an indexing operation. Essentially, it involves adding the document to the index by parsing all the fields within the document and building the inverted index. This is why this operation is known as an indexing operation.

There are two ways we can index a document:
- Indexing a document by providing an ID
- Indexing a document without providing an ID

## Indexing a document by providing an ID
We have already seen this version of the indexing operation. The user can provide the ID of the document using the PUT method.
The format of this request is PUT /<index>/<type>/<id>, with the JSON document as the body of the request:

```json
POST /catalog/_doc/1
{
  "sku": "SP000001",
  "title": "Elasticsearch for Hadoop",
  "description": "Elasticsearch for Hadoop",
  "author": "Vishal Shukla",
  "ISBN": "1785288997",
  "price": 26.99
}
```
Output

```json
{
  "_index" : "catalog",
  "_type" : "_doc",
  "_id" : "1",
  "_version" : 1,
  "_seq_no" : 1,
  "_primary_term" : 1,
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

## Indexing a document without providing an ID
If you don't want to control the ID generation for the documents, you can use the POST method.
The format of this request is POST /<index>/<type>, with the JSON document as the body of the request:

```json
POST /catalog/_doc
{
    "sku": "SP000003",
    "title": "Mastering Elasticsearch",
    "description": "Mastering Elasticsearch",
    "author": "Bharvi Dixit",
    "price": 54.99
}
```

The ID, in this case, will be generated by Elasticsearch. It is a hash string, as highlighted in the response:

**Response**
```json
{
	"_index" : "catalog",
	"_type" : "_doc",
	"_id" : "BXUeGnABd6vEGtiMBYL5",
	"_version" : 1,
	"result" : "created",
	"_shards" : {
		"total" : 2,
		"successful" : 1,
		"failed" : 0
	},
	"_seq_no" : 4,
	"_primary_term" : 1
}
```

As per pure REST conventions, POST is used for creating a new resource and PUT is used for updating an existing resource. Here, the usage of PUT is equivalent to saying I know the ID that I want to assign, so use this ID while indexing this document. 



# Get API
The get API is useful for retrieving a document when you already know the ID of the document. It is essentially a get by primary key operation.

## Retrieving a document by providing an ID

```GET /catalog/_doc/1```

**Response**
```json
{
    "_index" : "catalog",
    "_type" : "_doc",
    "_id" : "1",
    "_version" : 1,
    "_seq_no" : 1,
    "_primary_term" : 1,
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

## Retrieving a document without providing an ID

```GET /catalog/_doc/BXUeGnABd6vEGtiMBYL5```

The format of this request is `GET /<index>/<type>/<id>`. The response would be as expected:

**Response**
```json
{
    "_index" : "catalog",
    "_type" : "_doc",
    "_id" : "BXUeGnABd6vEGtiMBYL5",
    "_version" : 1,
    "_seq_no" : 2,
    "_primary_term" : 1,
    "found" : true,
    "_source" : {
      "sku" : "SP000003",
      "title" : "Mastering Elasticsearch",
      "description" : "Mastering Elasticsearch",
      "author" : "Bharvi Dixit",
      "price" : 54.99
    }
}
```


# Update API
The update API is useful for updating the existing document by ID.
The format of an update request is POST <index>/<type>/<id>/_update, with a JSON request as the body:

```json
POST /catalog/_update/1
{
    "doc": {
        "price": "28.99"
    }
}
```

The properties specified under the doc element are merged into the existing document. The previous version of this document with an ID of 1 had a price of 26.99. This update operation just updates the price and leaves the other fields of the document unchanged. This type of update means that doc is specified and used as a partial document to merge with an existing document; there are other types of updates supported.

**Response**

The response of the update request is as follows:
```json
{
    "_index": "catalog",
    "_type": "_doc",
    "_id": "1",
    "_version": 2,
    "result": "updated",
    "_shards": {
        "total": 2,
        "successful": 1,
        "failed": 0
    }
}
```

Internally, Elasticsearch maintains the version of each document. Whenever a document is updated, the version number is incremented.

## Partial Update
The partial update that we saw in the preceding code will work only if the document existed beforehand. If the document with the given ID did not exist, Elasticsearch will return an error saying that the document is missing. Let's understand how to do an upsert operation using the update API. The term upsert loosely means update or insert, that is, update the document if it exists, otherwise, insert the new document.

### doc_as_upsert
The doc_as_upsert parameter checks whether the document with the given ID already exists and merges the provided doc with the existing document. If the document with the given ID doesn't exist, it inserts a new document with the given document contents.

The following example uses doc_as_upsert to merge into the document with an ID of 3 or insert a new document if it doesn't exist:

```json
POST /catalog/_update/3
{
    "doc": {
    "author": "Albert Paro",
    "title": "Elasticsearch 5.0 Cookbook",
    "description": "Elasticsearch 5.0 Cookbook Third Edition",
    "price": "54.99"
    },
    "doc_as_upsert": true
}
```

### Update using scripting
We can update the value of a field based on the existing value of that field or another field in the document. The following update uses an inline script to increase the price by two for a specific product:

```json
POST /catalog/_update/1ZFMpmoBa_wgE5i2FfWV
{
    "script": {
        "source": "ctx._source.price += params.increment",
        "lang": "painless",
            "params": {
            "increment": 2
        }
    }
}
```

Scripting support allows you to read the existing value, increment the value by a variable, and store it in a single operation. The inline script that's used here is Elasticsearch's own painless scripting language. The syntax for incrementing an existing variable is similar to most other programming languages.
