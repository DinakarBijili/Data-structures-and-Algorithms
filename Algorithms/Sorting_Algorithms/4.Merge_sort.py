#Merge Sort using python

#Conseptually merge sort works as Follows:
# Divide the unsorted list into a sublist.each containing one element (a list of one element is consider sorted ) 
#Repeatedly merge sub lists to produse new sorted sublist until their is only one list remaining. Thi will be the sorted list

#  Best = Average = Worst = O(nlog(n))
"""
Merge sort is an algorithm that follows the Divide and Conquers paradigm. It continuously divides the array into two equal halves. 
Later it starts sorting the lists having a single element each and continuously merges the sorted lists to form the complete sorted list.

"""
# def merge(a, b):
#     c = []
#     while len(a) != 0 and len(b) != 0: # Loop runs until the lrft and right becomes 0 
        
#         if a[0] < b[0]:
#             c.append(a[0])
#             a.remove(a[0])

#         else:
#             c.append(b[0])
#             b.remove(b[0])
#     if len(a) == 0:
#         c += b 
#     else:
#         c += a
#     return c
    
# def merge_sort(arr):
#     if (len(arr)== 0) or (len(arr)==1):
#         return arr

#     mid = len(arr)//2
#     a = merge_sort(arr[:mid]) # Right side 
#     b = merge_sort(arr[mid:]) # Left Side
#     return merge(a,b)


# if __name__ == "__main__":
#     arr = [3, 4, 2, 8, 6, 5, 7, 1, 9]
#     print("Sorted List",merge_sort(arr))



#OTHER METHOD
def merge_sort(arr):
    if len(arr) <=1 :
        return arr


    mid_value = len(arr)//2
    left_value = merge_sort(arr[:mid_value])
    right_value = merge_sort(arr[mid_value:])
    print("%15s %-15s"%(left_value,right_value))

    sorted_values = []
    left_index = 0
    right_index = 0
    while left_index < len(left_value) and right_index < len(right_value):
        if left_value[left_index] < right_value[right_index]:
            sorted_values.append(left_value[left_index])
            left_index += 1
        else:
            sorted_values.append(right_value[right_index])
            right_index += 1

    sorted_values += left_value[left_index:]
    sorted_values += right_value[right_index:]
    return sorted_values

if __name__=="__main__":
    arr = [4,6,3,2,9,7,3,5]
    print(arr)
    result = merge_sort(arr)
    print(result)
            
