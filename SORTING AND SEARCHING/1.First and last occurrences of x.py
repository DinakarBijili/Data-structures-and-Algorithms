"""
First and last occurrences of x

Given a sorted array arr containing n elements with possibly duplicate elements, the task is to find indexes of first and last occurrences of an element x in the given array.

Example 1:

Input:
n=9, x=5
arr[] = { 1, 3, 5, 5, 5, 5, 67, 123, 125 }
Output:  2 5
Explanation: First occurrence of 5 is at index 2 and last
             occurrence of 5 is at index 5. 
 

Example 2:

Input:
n=9, x=7
arr[] = { 1, 3, 5, 5, 5, 5, 7, 123, 125 }
Output:  6 6 

"""
def Find_first_and_last_of_x(arr,x,n): 
    myList = []
    for i in range(len(arr)):
        if arr[i] == x:
            myList.append(i)
        
    if myList == []:
        return -1,-1
    return myList[0] , myList[-1] 
    

if __name__ == "__main__":
    # arr = list(map(int, input().split())) 
    arr = [1,1 ,1, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 7, 7, 9, 9, 9, 9, 9, 10, 10, 10]
    x = 8
    n = len(arr)
    res = Find_first_and_last_of_x(arr, x,n)
    print(*res)

