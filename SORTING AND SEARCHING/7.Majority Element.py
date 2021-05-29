"""
Majority Element 

Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.
 

Example 1:
Input:
N = 3 
A[] = {1,2,3} 
Output:
-1
Explanation:
Since, each element in 
{1,2,3} appears only once so there 
is no majority element.

Example 2:
Input:A[] = {3,1,3,3,2} 
Output: 3
Explanation:
Since, 3 is present more
than N/2 times, so it is 
the majority element.

"""
def Majority_elements(arr):
    if not arr:
        return []
    dict = {}
    for i in arr:
        if i not in dict: #[3:1, 4:1 , 2:1]
            dict[i] = 1 
        else:
            dict[i] += 1 #[3:2, 4:5 , 2:2]

        if dict[i] > len(arr)//2:
            return i
    return "No Majority Elements"

if __name__ == "__main__":
    arr = [3,1,3,2]
    res = (Majority_elements(arr))
    print(res)
    