"""
Count and Say
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string "3322251":


 

Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

"""
def Count_and_say(n):
    s = "1"
    if n == 1:
        return s
    for _ in range(2,n+1):
        j = 0
        temp = ""
        curr = ""
        count = 0
        while j < len(s):
            #print curr and count
            if curr == "":
                curr = s[j]
                count = 1
                j+= 1
            elif curr == s[j]:
                count += 1
                j += 1
            else:
                temp += str(count) + curr
                curr = ""
                count = 0
        temp+=str(count) + curr
       
        print("Example: ",temp + '\n')
        s = temp
    
    return s
        

if __name__ == "__main__":
    n = 4
    print(Count_and_say(n))