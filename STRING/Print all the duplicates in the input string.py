
def duplicate_string(x):

    for char in set(x):
        counts = x.count(char)
        while counts > 1:
            print(char, ":", counts, end=' ')
            break

if __name__ == "__main__":
    str = "geeksforgeeks"
    duplicate_string(str)
    
