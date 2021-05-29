"""
* Binary Search is a search algorithm that finds the position of the target in an sorted array.
* In Binary Search the array should to Sorted.
* Binary search Compare the target value to the middle elements of the array.
1. First at check the mid value is equal or not. if it is equal to target return mid else it contitues by checking <(greater than mid), >(lessthan mid)
2. if mid is greater than the target then right =  mid-1 and now right value goes to mid left side value and mid value changes and goes to mid of left and right
3. if mid is less than the target then left =  mid+1 and now left value goes to mid right side value and mid value changes and goes to mid of left and right
"""
def Binary_search(arr, target):
    global iterations 
    iterations = 0
    
    left = 0 
    right = len(arr)-1  
    mid = 0
    while left<=right:
        iterations += 1
        mid = (left+right)//2
        if arr[mid] < target:
            left = mid + 1

        elif arr[mid] > target:
            right = mid - 1

        else:
            return mid

    return -1 

if __name__ == "__main__":
    #FOr USER INPUT
    # arr = list(map(int, input().split()))
    # target = int(input())

    arr = [12,23,32,37,56,76]
    target = 56
    result = Binary_search(arr, target)
    print("Found",target,"at position",result,"in",iterations,"Iterations")