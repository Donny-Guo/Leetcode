'''
# O(n) space, O(n) time
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        left = 0
        right = len(new_str) - 1
        while left < right:
            if new_str[left] != new_str[right]:
                return False
            left += 1
            right -= 1
        return True
    
'''
# O(1) space, O(n) time
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True