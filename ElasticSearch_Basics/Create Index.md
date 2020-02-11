# Creating Index
You can create an index and specify the number of shards and replicas to create:
```json
PUT /catalog
{
	"settings": {
		"index": {
			"number_of_shards": 5,
			"number_of_replicas": 2
		}
	}
}
```

It is possible to specify a mapping for a type at the time of index creation. The following command will create an index called catalog1, with five shards and two replicas. Additionally, it also defines two fields, one of the text type and another of the keyword type:
```json
PUT /catalog1
{
    "settings": {
        "index": {
            "number_of_shards": 5,
            "number_of_replicas": 2
        }
    },
    "mappings": {
        "properties": {
            "f1": {
                "type": "text"
            },
            "f2": {
                "type": "keyword"
            }
        }
    }
}
```

## Creating Type mapping in an existing Index
With Elasticsearch 7.0, indexes contain strictly one type, and hence it is generally recommended that you create the index and the default type within that index at index creation time. `The default type name is _doc`.
In the earlier versions of Elasticsearch (6.0 and before), it was possible to define an index and then add multiple types to that index as needed. This is still possible but it is a deprecated feature. 

A type can be added within an index after the index is created using the following code. The mappings for the type can be specified as follows:

```json
PUT /catalog/_mapping
{
	"properties": {
		"name": {
    		"type": "text"
		}
	}
}
```

This command creates a type called _doc, with one field of the text type in the existing index catalog. 

### Add Documents  in Index
Let's add a couple of documents after creating the new type:
```json
POST /catalog/_doc
{
	"name": "books"
}

POST /catalog/_doc
{
	"name": "phones"
}
```

After a few documents are indexed, you realize that you need to add fields in order to store the description of the category. Elasticsearch will assign a type automatically based on the value that you insert for the new field. It only takes into consideration the first value that it sees to guess the type of that field:
```json
POST /catalog/_doc
{
	"name": "music",
	"description": "On-demand streaming music"
}
```

### Mapping after document Indexing
When the new document is indexed with fields, the field is assigned a datatype based on its value in the initial document. Let's look at the mapping after this document is indexed:
```json
{
	"catalog" : {
		"mappings" : {
			"properties" : {
				"description" : {
					"type" : "text",
					"fields" : {
						"keyword" : {
                            "type" : "keyword",
                            "ignore_above" : 256
						}
					}
				},
				"name" : {
					"type" : "text"
				}
			}
		}
	}
}
```

The field description has been assigned the text datatype, with a field with the name keyword, which is of the keyword type. What this means is that, logically, there are two fields, description and description.keyword.

The description field is analyzed at the time of indexing, whereas the description.keyword field is not analyzed and is stored as is without any analysis. By default, fields that are indexed with double quotes for the first time are stored as both text and keyword types.

### Field Type Change in Index
If you want to take control of the type, you should define the mapping for the field before the first document containing that field is indexed. A field's type cannot be changed after one or more documents are indexed within that field. 

## Updating a mapping
Mappings for new fields can be added after a type has been created. A mapping can be updated for a type with the PUT mapping API. Let's add a code field, which is of the keyword type, but with no analysis:

```json
PUT /catalog/_mapping
{
	"properties": {
		"code": {
			"type": "keyword"
		}
	}
}
```

This mapping is merged into the existing mappings of the _doc type. The mapping looks like the following after it is merged:

```json
{
    "catalog": {
        "mappings": {
            "properties": {
                "code": {
                    "type": "keyword"
                },
                "description": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "name": {
                    "type": "text"
                }
            }
        }
    }
}
```

Any subsequent documents that are indexed with the code field are assigned the right datatype:

```json
POST /catalog/_doc
{
	"name": "sports",
	"code": "C004",
	"description": "Sports equipment"
}
```

This is how we can take control of the index creation and type mapping process, and add fields after the type is created.

