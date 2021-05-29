# Sort an array of 0s, 1s and 2s 

# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


# Example 1:

# Input: 
# N = 5
# arr[]= {0 2 1 2 0}
# Output:
# 0 0 1 2 2
# Explanation:
# 0s 1s and 2s are segregated 
# into ascending order.

# Example 2:

# Input: 
# N = 3
# arr[] = {0 1 0}
# Output:
# 0 0 1
# Explanation:
# 0s 1s and 2s are segregated 
# into ascending order.

def quick_sort(arr):
   if len(arr) <= 1:
      return arr

   less_than_pivot = []
   greater_than_pivot = []
   pivot = arr[0] #first index
   
   for value in arr[1:]:
      if value <= pivot:
         less_than_pivot.append(value)
      else:
         greater_than_pivot.append(value)

   print("%15s %1s %15s"% (less_than_pivot,pivot,greater_than_pivot))
   return quick_sort(less_than_pivot)+[pivot]+quick_sort(greater_than_pivot)

if __name__ == "__main__":
  
   arr  = [4,6,3,2,9,7,3,5]
   print(arr)
   result = quick_sort(arr)
   print(result)
