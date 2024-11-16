"""
Find Anagrams:
You'll be given two arrays of words. 
Your task? Find the unique words in the first array that can rearrange their letters to match at least one word in the second array. 
Like transforming 'cinema' into 'iceman'. Cool, right?

The input will be two lists of words; they can be of any size, and words may repeat.
As for the output, we need a list of unique words from the first list that have anagrams in the second one.
Make sure the spaceship does not crash into an asteroid, and check that there aren't any duplicate words in the output. 
As for edge cases, watch out for case sensitivity and one-letter words!.
"""
def find_anagram_words(list_1, list_2):
    normalized_list_2 = {"".join(sorted(word.lower())) for word in list_2}
    result = set()
    
    for word in list_1:
        if "".join(sorted(word.lower())) in normalized_list_2:
            result.add(word)
    
    return(list(result))
        
        


print(find_anagram_words(['cinema', 'iceman'], ['iceman', 'cinema'])) # should return ['cinema', 'iceman']
print(find_anagram_words(['test', 'stet'], ['tent', 'nett'])) # should return []
print(find_anagram_words(['hello', 'world'], ['dolly', 'sir'])) # should return []
