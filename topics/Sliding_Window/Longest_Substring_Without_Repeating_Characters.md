# Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string `s`, find the length of the **longest** **substring** without duplicate characters.

 

**Example 1:**

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

 

**Constraints:**

- `0 <= s.length <= 5 * 104`
- `s` consists of English letters, digits, symbols and spaces.



**Reflections**:

1. move left ptr when found duplicate
2. when update left ptr, check if the index+1 in map is on the left/right on current left ptr



## Solution1: use set

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      	res = 0
        left = 0
        charSet = set()
        
        for right in range(len(s)):
          while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
          charSet.add(s[right])
          res = max(res, right - left + 1)
        return res
```

TC: O(n)

SC: O(n)

## Solution2: use map

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        res = 0
        left = 0

        for i, c in enumerate(s):
            if c in mp:
                # move left ptr to mp[c] + 1 if it is on the right of left ptr
                left = max(left, mp[c] + 1)
            mp[c] = i
            res = max(i - left + 1, res)
        
        return res
```

TC: O(n)

SC: O(n)