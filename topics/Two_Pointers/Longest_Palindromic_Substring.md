# Longest Palindromic Substring

https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string `s`, return *the longest* *palindromic* *substring* in `s`.

 

**Example 1:**

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

**Example 2:**

```
Input: s = "cbbd"
Output: "bb"
```

 

**Constraints:**

- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.



## Solution

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        for i in range(len(s) - 1):
            for left, right in [(i-1, i+1), (i, i+1)]:
                while 0 <= left and right < len(s):
                    if s[left] == s[right]:
                        if right - left + 1 > len(res):
                            res = s[left:right+1]
                        left -= 1
                        right += 1
                    else:
                        break
        return res
```

TC: O(N^2)

SC: O(N) for storing output