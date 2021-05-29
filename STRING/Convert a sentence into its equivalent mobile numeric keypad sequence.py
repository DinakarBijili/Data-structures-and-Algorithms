"""
Convert a sentence into its equivalent mobile numeric keypad sequence
Given a sentence in the form of a string, convert it into its equivalent mobile numeric keypad sequence. 
 

Mobile-keypad

Examples : 
 

Input : GEEKSFORGEEKS
Output : 4333355777733366677743333557777
For obtaining a number, we need to press a
number corresponding to that character for 
number of times equal to position of the 
character. For example, for character C, 
we press number 2 three times and accordingly.

Input : HELLO WORLD
Output : 4433555555666096667775553

"""
def phone_pattern(string):
    dict = {"A B C":'2', "DEF":'3', "GHI":'4', "JKL":'5',"MNO":'6', "PQRS":'7' , "TUV":'8', "WXYZ":'9'}
    l = []
    for i in range(len(string)):
        pre_str = string[:i+1]
        print(pre_str)
        if pre_str in dict.keys():
            l.append(pre_str)

    return l
    
if __name__ == "__main__":
    string = "GEEKSFORGEEKS"
    print(phone_pattern(string))