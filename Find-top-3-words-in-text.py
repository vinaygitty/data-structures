"""
Dictionaries: Find top 3 words in text
"""
def frequent_words_finder(text):
    from collections import defaultdict

    text = text.lower()
    word_counts = defaultdict(int)
    word_list = text.split()
    for word in word_list:
        word_counts[word] += 1
    top_three = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:3]
    return top_three

print(frequent_words_finder("Hey there hot shot Are you ready for a challenge This might be trickier than it looks")) # Expected Output: [('hey', 1), ('there', 1), ('hot', 1)]

print(frequent_words_finder("The quick brown fox jumps over the lazy dog The fox is quick but the dog is lazy")) # Expected Output: [('the', 4), ('quick', 2), ('fox', 2)]

print(frequent_words_finder("")) # Expected Output: []
