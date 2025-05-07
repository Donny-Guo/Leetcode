# Permutation in String

https://leetcode.com/problems/permutation-in-string/description/

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

 

**Example 1:**

```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

**Example 2:**

```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

 

**Constraints:**

- `1 <= s1.length, s2.length <= 104`
- `s1` and `s2` consist of lowercase English letters.



**Reflections**:

- notice that the window size is fixed in this case

---

## Solution

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        countS1 = [0] * 26
        countS2 = [0] * 26
        matches = 0

        # get countS2
        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1
        # get matches
        for i in range(26):
            if countS1[i] == countS2[i]:
                matches += 1
        
        left, right = 0, len(s1)

        while right < len(s2) and matches != 26:
            # move left ptr
            left_char_index = ord(s2[left]) - ord('a')
            if countS2[left_char_index] == countS1[left_char_index]:
                matches -= 1
            elif countS2[left_char_index] == countS1[left_char_index] + 1:
                matches += 1
            countS2[left_char_index] -= 1
            # move right ptr
            right_char_index = ord(s2[right]) - ord('a')
            if countS2[right_char_index] + 1 == countS1[right_char_index]:
                matches += 1
            elif countS2[right_char_index] == countS1[right_char_index]:
                matches -= 1
            countS2[right_char_index] += 1
        
            left += 1
            right += 1
        return matches == 26
```

TC: O(n)

SC: O(1)