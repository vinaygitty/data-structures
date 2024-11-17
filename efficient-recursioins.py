#Problem 1: Efficient Approach for fibonnaci 
def fib(n, computed={0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib(n - 1, computed) + fib(n - 2, computed)
    return computed[n]

#Problem 2: Summing Array Elements
def arraySum(arr, index=0): 
   if index == len(arr): 
       return 0 
   else:
       return arr[index] + arraySum(arr, index + 1)
   
#Problem 3: Factorials
def factorial(num,computed={0:1,1:1}):
    if num < 0 :
        computed[num] = 'Error'
        return computed[num]
    if num not in computed:
        computed[num] = num * factorial(num-1)
    return computed[num]

def factorials(nums):
    return [factorial(num) if factorial(num) is not None else 'Error' for num in nums]

print(factorials([2, 3, 4])) # should print: [2, 6, 24]
print(factorials([1, 5, 6])) # should print: [1, 120, 720]
print(factorials([0, -3, 10])) # should print: [1, 'Error', 3628800]
