# Bubble sort is a Simple Sorting algorithm that repeatedly steps through the array, compare adjecent and swaps them if they are in the wrong order.
# pass through the array is repeated until the array is sorted

#Best O(n^2); Average O(n^2); Worst O(n^2)
"""
Approach
Starting with the first element(index = 0), compare the current element with the next element of the array.

If the current element is greater than the next element of the array, swap them.

If the current element is less than the next element, move to the next element.
"""

def bubble_sort(List):
    for i in range(len(List)): # Traverse through all array elements
        for j in range(len(List)-1, i, - 1): # Last i elements are already in correct position(reverse order)
            if List[j] < List[j - 1]:
                List[j],List[j - 1] = List[j - 1], List[j] #swap
    return List

if __name__  == "__main__":
    # List = list(map(int,input().split())) <-- for user input 
    List = [3, 4, 2, 6, 5, 7, 1, 9]
    print("Sorting List", bubble_sort(List))  
