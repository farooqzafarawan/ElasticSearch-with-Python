# Understanding Elasticsearch Analyzers
The main task of an analyzer is to take the value of a field and break it down into terms. The job of the analyzer is to take documents and each field within them and extract terms from them. These terms make the index searchable, that is, they can help us find out which documents contain particular search terms.
The analyzer performs this process of breaking up input character streams into terms. This happens twice: 
- At the time of indexing
- At the time of searching

### Process of Analysis
The core task of the analyzer is to parse the document fields and build the actual index.
Every field of text type needs to be analyzed before the document is indexed. This process of analysis is what makes the documents searchable by any term that 
is used at the time of searching.

## Analyzer configuration
Analyzers can be configured on a per field basis, that is, it is possible to have two fields of the text type within the same document, each one using different analyzers.

Elasticsearch uses analyzers to analyze text data. An analyzer has the following components:
- Character filters: Zero or more
- Tokenizer: Exactly one
- Token filters: Zero or more

The following diagram depicts the components of an analyzer:
[Anatomy of an analyzer](
onenote:https://d.docs.live.net/1fe31d0fa3731f2c/OneNote/NoSQL/ElasticSearch/ES%20Books/Learning%20Elastic%20Stack%207.one#Understanding%20Elasticsearch%20analyzers&section-id={E8F10BD9-E3DD-4F09-959F-DF47E26D368A}&page-id={EAE9068F-C268-4EB3-A7EA-CB5A3A6F68EF}&object-id={F0F7574E-DDCD-47B8-BCB4-74B28ADE0475}&37
)

## Character filters
When composing an analyzer, we can configure zero or more character filters. A character filter works on a stream of characters from the input field; each character filter can add, remove, or change the characters in the input field.
Elasticsearch ships with a few built-in character filters, which you can use to compose or create your own custom analyzer. 

### Mapping Char Filter
For example, one of the character filters that Elasticsearch ships with is the Mapping Char Filter. It can map a character or sequence of characters into target characters.
For example, you may want to transform emoticons into some text that represents those emoticons:
- :) should be translated to _smile_
- :( should be translated to _sad_
- :D should be translated to _laugh_

This can be achieved through the following character filter. The short name for the Mapping Char Filter is the mapping filter:
```json
"char_filter": {
	"my_char_filter": {
		"type": "mapping",
		"mappings": [
			":) => _smile_",
			":( => _sad_",
			":D => _laugh_"
		]
	}
}
```

Character filters can be useful for replacing characters with something more meaningful in certain cases, such as replacing the numeric characters from other languages with English language decimals, that is, digits from Hindi, Arabic, and other languages can be turned into 0, 1, 2, and so on.

You can go through [list of available built-in character filters](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-charfilters.html).

# Tokenizer
An analyzer has exactly one tokenizer. The responsibility of a tokenizer is to receive a stream of characters and generate a stream of tokens. These tokens are used to build an inverted index. A token is roughly equivalent to a word. In addition to breaking down characters into words or tokens, it also produces, in its output, the start and end offset of each token in the input stream.
Elasticsearch ships with a number of tokenizers that can be used to compose a custom analyzer; these tokenizers are also used by Elasticsearch itself to compose its built-in analyzers.

[List of available built-in tokenizers](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-tokenizers.html).

## Standard tokenizer
Standard tokenizer breaks down a stream of characters by separating them with whitespace characters and punctuation.
```json
POST _analyze
{
"tokenizer": "standard",
"text": "Tokenizer breaks characters into tokens!"
}
```

The preceding command produces the following output; notice the start_offset, end_offset, and positions in the output:
```json
{
"tokens": [
    {
        "token": "Tokenizer",
        "start_offset": 0,
        "end_offset": 9,
        "type": "<ALPHANUM>",
        "position": 0
    },
    {
        "token": "breaks",
        "start_offset": 10,
        "end_offset": 16,
        "type": "<ALPHANUM>",
        "position": 1
    },
    {
        "token": "characters",
        "start_offset": 17,
        "end_offset": 27,
        "type": "<ALPHANUM>",
        "position": 2
    },
    {
        "token": "into",
        "start_offset": 28,
        "end_offset": 32,
        "type": "<ALPHANUM>",
        "position": 3
    },
    {
        "token": "tokens",
        "start_offset": 33,
        "end_offset": 39,
        "type": "<ALPHANUM>",
        "position": 4
    }
]
}
```

This token stream can be further processed by the token filters of the analyzer.

## Token filters
There can be zero or more token filters in an analyzer. Every token filter can add, remove, or change tokens in the input token stream that it receives. Since it is possible to have multiple token filters in an analyzer, the output of each token filter is sent to the next one until all token filters are considered.
Elasticsearch comes with a number of token filters, and they can be used to compose your own custom analyzers.

Some examples of built-in token filters are the following:
	• Lowercase token filter: Replaces all tokens in the input with their lowercase versions.
	• Stop token filter: Removes stopwords, that is, words that do not add more meaning to the context. For example, in English sentences, words like is, a, an, and the, do not add extra meaning to a sentence. For many text search problems, it makes sense to remove such words, as they don't add any extra meaning or context to the content.

You can find a list of available built-in token filters here: 
https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-tokenfilters.html.

Thus far, we have looked at the role of character filters, tokenizers, and token filters. This sets us up to understand how some of the built-in analyzers in Elasticsearch are composed. 





