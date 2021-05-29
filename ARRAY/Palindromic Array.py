"""
Example:
Input:
2
5
111 222 333 444 555
3
121 131 20

Output:
1
0
"""
def palindromic(arr, n):
    rev = (arr[::-1])
    if rev == arr:
        return True 
    else:
        return False

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        if palindromic(arr, n):
            print(1)
        else:
            print(0)

        