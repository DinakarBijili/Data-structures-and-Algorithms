"""
Word Break 

Given a string A and a dictionary of n words B, find out if A can be segmented into a space-separated sequence of dictionary words. 


Example 1:

Input:
n = 12
B = { "i", "like", "sam", "sung", "samsung", "mobile",
"ice","cream", "icecream", "man", "go", "mango" }
A = "ilike"
Output: 1
Explanation:The string can be segmented as "i like".

â€‹Example 2:

Input:
n = 12
B = { "i", "like", "sam", "sung", "samsung", "mobile",
"ice","cream", "icecream", "man", "go", "mango" }
A = "ilikesamsung"
Output: 1
Explanation: The string can be segmented as 
"i like samsung" or "i like sam sung".

"""
def Word_Break(dict, word):
    res = []
    words = []
    words.append(word)
    for i in range(len(word)):
        pre_st = word[:i+1]
        
        if pre_st in dict:
            res.append(pre_st)
            word = word[i:]
            print(res,words)
      
            if res == words:
                return True
            return False
    return res
                
if __name__ == "__main__":
    # dict = ['acehc']
    # word = "acehcacehc"
    
    dict = ['scd', 'rjmowfrx', 'jybldbe', 'sarcbyne', 'dyggxxp', 'lorel', 'nmpa' ,'qfwkho', 'kmcoqhnw', 'kuewhsqmgb']
    word ="dyggxxp"
    print(Word_Break(dict, word))
    
    


