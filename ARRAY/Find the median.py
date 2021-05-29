"""
Find the median 

Given an array arr[] of N integers, calculate the median

Example 1:

Input: N = 5
arr[] = 90 100 78 89 67
Output: 89
Explanation: After sorting the array 
middle element is the median 

Example 2:

Input: N = 4
arr[] = 56 67 30 79â€‹
Output: 61
Explanation: In case of even number of 
elemebts average of two middle elements 
is the median

"""

# def Find_median(arr):
#     n = len(arr)
#     print(n)
#     arr.sort()
    
#     if n % 2 == 0:
#         median1 = arr[n//2]
#         median2 = arr[n//2-1]
#         median = (median1 + median2)/2
#         print(median2)
#     else:
#         median = arr[n//2]
        

#     return int(median)
# if __name__ == "__main__":
#     arr = [19, 11,15,24,21]
#     result = Find_median(arr)
#     print(result)

#OTHER METHOD
# from statistics import median
# def Find_median(arr):
#     return median(arr)
# if __name__ == "__main__":
#     arr = [19, 11]
#     result = (Find_median(arr))
#     print (int(result))
    
