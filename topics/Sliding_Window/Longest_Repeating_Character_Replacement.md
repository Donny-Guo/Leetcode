# Longest Repeating Character Replacement

https://leetcode.com/problems/longest-repeating-character-replacement/description/

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return *the length of the longest substring containing the same letter you can get after performing the above operations*.

 

**Example 1:**

```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

**Example 2:**

```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
```

 

**Constraints:**

- `1 <= s.length <= 105`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`



**Reflections**:

- valid window condition: (right - left + 1) - max_freq <= k



## Solution

```python
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        res = 0
        count = defaultdict(int)

        for right in range(len(s)):
            count[s[right]] += 1
        
            if right - left + 1 - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        
        return res
```

TC: O(26*n) = O(n)

SC: O(n)