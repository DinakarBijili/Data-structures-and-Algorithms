"""
* Linear Search or Sequencial Search is a method for Finding an element within a list. I
* It Sequencially checks each element in a list until a match is Found or a whole list has been searched.

"""

def Linear_search(arr, target):
    global iterations
    iterations = 0
    for i in range(len(arr)):
        iterations += 1
        if arr[i] == target:
            return i
    return -1 # if target not Found in the arr it returns -1

if __name__ == "__main__":
    #For input User
    # arr = list(map(int,input().split()))
    # target = int(input())
    arr = [12,23,12,32,34,56,76]
    target = 34
    result = Linear_search(arr, target)
    print("Found",target,"at position",result,"in",iterations,"Iterations")