#Insertion Sort using Python
#  Best O(n); Average O(n^2); Worst O(n^2) -> Time Complex 

# insertion sort iterates , consuming one input element each repetition and grow a sorted output List.
 
# At each iteration , insertion removes one element from the input data and finds the location it belongs within the sorted list and insert it their.
#It repeates until no input element remians

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i] # 4, 2, 8, 6, 5, 7, 1, 9
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1   #4, 2, 8, 6, 5, 7, 1
        for j in range(j,-1,-1):  
                  
            if arr[j] > key:
                arr[j],arr[j + 1] = arr[j + 1], arr[j]

    return arr
          
if __name__ == "__main__":
    # arr = list(map(int, input().split()))
    arr  = [3, 4, 2, 8, 6, 5, 7, 1, 9]

    print("Sorted array ",insertion_sort(arr))
