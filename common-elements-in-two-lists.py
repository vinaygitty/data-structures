# presume that you're managing a database for a marketing company.
# You have two customer lists, each obtained through various marketing strategies. 
# Your task is to determine the customers that both strategies successfully targeted. 
# Essentially, these are the common elements in your two lists.

def array_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1 & set2
    return sorted(list(intersection))
