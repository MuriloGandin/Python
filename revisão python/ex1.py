text = "murilo"

def isPalindrome(s):
    s = s.replace(" ", "")
    s = s.lower()
    return s == s[::-1]

print(isPalindrome(text))