# https://leetcode.com/problems/valid-anagram/
''' Using Hash table
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = dict()
        for c in s:
            if c not in seen:
                seen[c] = 1
            else:
                seen[c] += 1
        for c in t:
            if c not in seen:
                return False
            else:
                seen[c] -= 1
        for v in seen.values():
            if v != 0:
                return False
        return True
'''

# Using fixed-size counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = [0] * 26
        for c in s:
            counter[ord(c)-ord('a')] += 1
        for c in t:
            counter[ord(c)-ord('a')] -= 1
            if counter[ord(c)-ord('a')] < 0:
                return False
        return True