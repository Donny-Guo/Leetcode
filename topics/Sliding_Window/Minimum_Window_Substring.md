# Minimum Window Substring

https://leetcode.com/problems/minimum-window-substring/description/

Given two strings `s` and `t` of lengths `m` and `n` respectively, return *the **minimum window*** ***substring\*** *of* `s` *such that every character in* `t` *(**including duplicates**) is included in the window*. If there is no such substring, return *the empty string* `""`.

The testcases will be generated such that the answer is **unique**.

 

**Example 1:**

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

**Example 2:**

```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

**Example 3:**

```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

 

**Constraints:**

- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 105`
- `s` and `t` consist of uppercase and lowercase English letters.



**Reflections**:

- use matches to check valid condition



## Solution

```python
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case
        if len(s) < len(t): return ""
    
        countT = defaultdict(int)
        countS = defaultdict(int)
        for i in range(len(t)):
            countT[t[i]] += 1
            countS[s[i]] += 1
        # calculate matches
        matches = 0
        for c in countT.keys():
            if countT[c] <= countS[c]:
                matches += 1
        res = ""
        left, right = 0, len(t)
        k = len(countT.keys())
        if matches == k:
            return s[left:right]

        while right < len(s):
            # expand until valid
            countS[s[right]] += 1
            if countS[s[right]] == countT[s[right]]:
                matches += 1
            right += 1
            if matches < k: continue

            # update res
            if not res: 
                res = s[left:right]
            else:
                if right - left < len(res):
                    res = s[left:right]

            # shrink until not valid
            while matches == k:
                if right - left < len(res):
                    res = s[left:right]

                if countS[s[left]] == countT[s[left]]:
                    matches -= 1
                countS[s[left]] -= 1
                left += 1
                
        return res
```

TC: O(n)

SC: O(m) m: the total number of unique chars in t and s