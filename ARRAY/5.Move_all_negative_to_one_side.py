"""
Move all negative numbers to beginning and positive to end with constant extra space


An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.
Examples : 

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5
"""

def negative_elements(arr):
    arr.sort()
    my_list = []
    for i in arr:
        if i <= -1:
            my_list.append(i)
        else:
            my_list.append(i)
    return my_list

if __name__ == "__main__":
    arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    result = negative_elements(arr)
    print(result)