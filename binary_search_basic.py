# Implementation of Binary Search on a specific use case

# List of sorted products' prices in an e-commerce company
products_price = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

def binary_search_iterative(data, target):
    low = 0
    high = len(data)
    while high - low > 1:
        mid = (low + high) // 2
        if target < data[mid]:
            high = mid 
        elif target > data[mid]:
            low = mid 
        else:  # if target is equal to data[mid]
            return mid
    return low if data[low] == target else None

def search_price(customer_query):
    result = binary_search_iterative(products_price, customer_query)
    if result is not None:
        print(f"Product of price ${customer_query} is found at position {result} in the price list.")
    else:
        print(f"No product is found with price ${customer_query}.")

# Searching for a price that exists
search_price(30)

# Searching for a price that doesn't exist
search_price(31)


#------------------------------------------------------------------------------------------------------#

# Implementation of Binary Search on a specific use case using recursions

# List of sorted word lengths in a dictionary
word_lengths = [i for i in range(1, 501)]  # Lengths from 1 to 500

# TODO: Implement the recursion-based binary_search_recursive method
def binary_search_recursive(data, target, low, high):
    if high - low <= 1:
        return low if data[low] == target else None
    mid = (low + high)//2
    if target < data[mid]:
        return binary_search_recursive(data, target, low, mid)
    else:
        return binary_search_recursive(data, target, mid, high)
            

# Suppose there is a spelling bee, and a contestant is given a word.
# The contestant knows the word is in the dictionary, so let's find what position the length of this word would hold in our sorted list of word lengths
word_length_query = 237
result = binary_search_recursive(word_lengths, word_length_query, 0, len(word_lengths))
if result is not None:
    print(f"Words of length {word_length_query} are found at position {result} in the word lengths list.")
else:
    print(f"No words are found with length {word_length_query}.")
