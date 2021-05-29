"""
Median of two sorted arrays of different sizes

Given two sorted arrays, a[] and b[], the task is to find the median of these sorted arrays, in O(log n + log m) time complexity, when n is the number of elements in the first array, and m is the number of elements in the second array.

Example: 

Input: ar1[] = {-5, 3, 6, 12, 15}
        ar2[] = {-12, -10, -6, -3, 4, 10}
Output : The median is 3.
Explanation : The merged array is :
        ar3[] = {-12, -10, -6, -5 , -3,
                 3, 4, 6, 10, 12, 15},
       So the median of the merged array is 3

Input: ar1[] = {2, 3, 5, 8}
        ar2[] = {10, 12, 14, 16, 18, 20}
Output : The median is 11.
Explanation : The merged array is :
        ar3[] = {2, 3, 5, 8, 10, 12, 14, 16, 18, 20}
        if the number of the elements are even, 
        so there are two middle elements,
        take the average between the two :
        (10 + 12) / 2 = 11.

"""
# from statistics import median

# def find_median(arr1, arr2):
#     res = list(set(arr1).union(arr2))
#     res.sort()
#     return median(res)

# if __name__ == "__main__":
#     arr1 = [2, 3, 5, 8]
#     arr2 = [10, 12, 14, 16, 18, 20]
#     result = find_median(arr1,arr2)
#     print(int(result))



#OTHER METHOD 

def find_median(arr1,arr2):
    res = list(set(arr1).union(arr2))
    n = len(res)
    res.sort()

    if n % 2 == 0:
        median1 =res[n//2]
        median2 = res[n//2-1]
        median = (median1 + median2)/2
        print(median)
        
    else:
        median = res[n//2]
    
    return median


if __name__ == "__main__":
    arr1 = [2, 3, 5, 8]
    arr2 = [10, 12, 14, 16, 18, 20]
    result = find_median(arr1,arr2)
    print(int(result))


