# Quick Sort using Python

#  Best = Average = O(nlog(n)); Worst = O(n^2)

#Quick sort is divide-and-conquer algorithm. it works by a selecting a pivot element from an array and partitionong the other elements into two sub-array.
# according to wheather their are less that or greaterthan the pivot. the sub-arrays are then sorted recursively. 

#DIVIDE AND CONQUER METHOD

#OTHER METHOD With Visuals
# def quick_sort(arr):
#    if len(arr) <= 1:
#       return arr

#    less_than_pivot = []
#    greater_than_pivot = []
#    pivot = arr[0] #first index
   
#    for value in arr[1:]:
#       if value <= pivot:
#          less_than_pivot.append(value)
#       else:
#          greater_than_pivot.append(value)

#    print("%15s %1s %-15s"% (less_than_pivot,pivot,greater_than_pivot))
#    return quick_sort(less_than_pivot)+[pivot]+quick_sort(greater_than_pivot)

# if __name__ == "__main__":
  
#    arr  = [4,6,3,2,9,7,3,5]
#    print(arr)
#    result = quick_sort(arr)
#    print(result)

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # If the element found is greater than the next element, swap
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

        print(arr)


arr = [3, 8, 2, 5, 6, 1, 9, 4, 7]
bubble_sort(arr)
print("Sorted array is:", arr)
