# Quick Sort using Python

#  Best = Average = O(nlog(n)); Worst = O(n^2)

#Quick sort is divide-and-conquer algorithm. it works by a selecting a pivot element from an array and partitionong the other elements into two sub-array.
# according to wheather their are less that or greaterthan the pivot. the sub-arrays are then sorted recursively. 

#DIVIDE AND CONQUER METHOD
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

   print("%15s %1s %-15s"% (less_than_pivot,pivot,greater_than_pivot))
   return quick_sort(less_than_pivot)+[pivot]+quick_sort(greater_than_pivot)

if __name__ == "__main__":
  
   arr  = [4,6,3,2,9,7,3,5]
   print(arr)
   result = quick_sort(arr)
   print(result)

