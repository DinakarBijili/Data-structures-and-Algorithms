"""
Rabin-Karp Algorithm for Pattern Searching
 
Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.
Examples: 

Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12
"""
def Rabin_Kard_algorithm(txt, pat):
    s  = []
    
    for i in range(len(pat)):
        pre_str = pat[:i+1]
        print(pre_str)
    
        if pre_str in txt:                
            s.append(pre_str)

    return s
        
  
if __name__ == "__main__":
    txt = "THIS IS A TEST TEXT"
    pat = "TEST"
    print(Rabin_Kard_algorithm(txt, pat))