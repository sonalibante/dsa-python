"""
DATA STRUCTURE : Array
OPERATION      : Insertion
TASK           : insert_at_end(arr, value)
                 insert_at_index(arr, index, value): shift by hand
                 insert_at_start(arr, value): reuse the function above

                 Test each on [10, 20, 30], on [], at index 0, and at index len(arr). 
                 Decide what should happen if index is 5 on a list of 3, and handle it.

EDGE CASES     : negative or out of range indexes modification will return same list as answer. 
  -

COMPLEXITY     : insert_at_end: time O(1)   space O(1), insert_at_index: time O(n-index)   space O(1), 
                 insert_at_start: time O(n)   space O(1)

MISTAKES       : considered enumerate before range. 
                 Instead of each function call changed last known array instead of starting fresh
                 wrong space complexity was calculated. missed handle what happens if -ve index was asked to change. 
  -

DATE DONE      : 27th Nov, 2026
"""


# your code here
def insert_at_end(arr, value):
    ans = arr
    ans.append(value)
    return ans

def insert_at_index(arr, index, value):
    if index > len(arr) or index < 0:
        return arr
    ans = arr
    ans.append(None)
    for i in range(len(arr)-1, index, -1):
        ans[i] = ans[i-1]

    ans[index] = value
    return ans

def insert_at_start(arr, value):
    ans = arr
    return insert_at_index(ans, 0, value) 

if __name__ == "__main__":
    array = [10, 20, 30]

    print(insert_at_end(array, 40))
    print(insert_at_index(array, 2, 40))
    print(insert_at_index(array, 5, 40))
    print(insert_at_start(array, 40))

    print(insert_at_end([], 40))
    print(insert_at_index([], 2, 40))
    print(insert_at_index([], 5, 40))
    print(insert_at_index([], 0, 40))
    print(insert_at_start([], 40))