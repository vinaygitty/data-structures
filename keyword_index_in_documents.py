"""
Imagine you are a librarian! You know, we got gazillion documents in the library, each represented as a string in a list. 
Your task is to whip up an index that's as nifty as a dictionary which logs in every unique word from these documents. 
Now, don't forget, each unique word is a key, mapping to another dictionary where the key is the document index and the value is how many times that word appeared in the document. 
It's sure gonna make searching a lot quicker, kinda like quantum speed, eh? Let's get rollin'!

Ensure that your code handles all the edge cases. The input would be a list, where each string inside the list is a document. 
And every string is just a regular english text, easy peasy.

The output should be a dictionary, where each unique word is a key, and the mapped value should be another dictionary, having document index as the key and its corresponding word count as the value.    
"""

def keyword_index(docs):
    result = {}
    for doc_idx, doc in enumerate(docs):
        words = doc.split()
        for word in words:
            if word not in result:
                result[word] = {}
            if doc_idx in result[word]:
                result[word][doc_idx] += 1
            else:
                result[word][doc_idx] = 1
    return result

docs = ["Hello world", "world of python", "python is a snake"]
print(keyword_index(docs))  # Expected output: {'Hello': {0: 1}, 'world': {0: 1, 1: 1}, 'of': {1: 1}, 'python': {1: 1, 2: 1}, 'is': {2: 1}, 'a': {2: 1}, 'snake': {2: 1}}
