# Understand
# Input: string
# Output: bool

# Match:
# 1. similar to substring
# 2. modulus operator
def repeatedSubstringPattern(s):
# Plan:
    if len(s) <= 1:
        return False
# for loop to start with s[0:1] -->s[0:len(s)//2]
    for i in range(1, len(s)//2 + 1):
# 1. take the substring of s
        sub = s[0:i]
# 2. append the substring 
        n = len(s) // len(sub)
        appended = sub * n
# 3. compare the appended string with the input s
        if (appended == s):
            return True
    return False
# Complexity:
# O(n) time complexity and O(n) space complexity

# Method2:
    # return s in (s+s)[1:-1] # find whether s is in the appended string excluding the first and the last char

def main():
    s = "aba"
    print(repeatedSubstringPattern(s))

if __name__ == "__main__":
    main()