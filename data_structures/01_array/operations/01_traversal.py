"""
DATA STRUCTURE : Array
OPERATION      : Traversal
TASK           : print every element forwards
                  print every element backwards (by index)
                  print index and value together
                  In __main__, call each function on [10, 20, 30], [] and [7].

  -

EDGE CASES     : empty list and single valued list
  -

COMPLEXITY     : traverse_forward: time O(n)   space O(n), 
                  traverse_backwards: time O(n)   space O(n), 
                  traverse_with_index: time O(n)   space O(n) 
                  (note: space can be O(1) if print inside function and not use ans to store result. 

MISTAKES       : tried using appendleft it is not method for list. missed 0th index when reversing the list with range. 
  -

DATE DONE      : 26 Nov, 2026
"""


# your code here
def traverse_forward(arr):
    ans = []
    for value in arr:
        ans.append(value)
    return ans

def traverse_backwards(arr):
    ans = []
    for index in range(len(arr) - 1, -1, -1):
        ans.append(arr[index])
    return ans

def traverse_with_index(arr):
    ans = []
    for index, value in enumerate(arr):
        ans.append((index, value))
    return ans


if __name__ == "__main__":

    arr = [10, 20, 30]
    print(traverse_forward(arr))
    print(traverse_backwards(arr))
    print(traverse_with_index(arr))

    arr = []
    print(traverse_forward(arr))
    print(traverse_backwards(arr))
    print(traverse_with_index(arr))

    arr = [7]
    print(traverse_forward(arr))
    print(traverse_backwards(arr))
    print(traverse_with_index(arr))
