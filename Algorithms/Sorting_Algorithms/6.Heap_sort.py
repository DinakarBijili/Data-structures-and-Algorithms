# Heap Sort using

#  Best O(nlog(n)); Average O(nlog(n)); Worst O(nlog(n)).

# heapify
def heapify(arr,n, i):
    largest = i # larger value
    l = 2 * i + 1 # Left 
    r = 2 * i + 2 # right
      # if left child exists
    if l < n and arr[i] < arr[l]:
      largest = l
    # if right child exits
    if r < n and arr[largest] < arr[r]:
      largest = r
    # root
    if largest != i:
      arr[i],arr[largest] = arr[largest],arr[i] # swap
      # root.
      heapify(arr, n, largest)
#sort
def heap_sort(arr):
    n = len(arr)
    #max_heap
    for i in range(n, -1, -1): 
        heapify(arr,n,i)
    # elements extraction
    for i in range(n-1,0,-1):# reverse order len(arr)-1 to 1 index because stop to 0 
        arr[i],arr[0] = arr[0],arr[i] #swap
        heapify(arr,i,0)
        
    return arr
if __name__ == "__main__":
    arr = [3, 4, 2, 8, 6, 5, 7, 1, 9]
    result = heap_sort(arr)
    print("Sorted array:",result)

