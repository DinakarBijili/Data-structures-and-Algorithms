def isPlaindrome(S):
		# code here
        isplaindrome = S[::-1]
        if isplaindrome == S:
            return 1
        return 0

if __name__ == "__main__":
    S = "abba"
    print(isPlaindrome(S))