## Palindrome Partitioning

https://leetcode.com/problems/palindrome-partitioning/description/

Given a string `s`, partition `s` such that every substring of the partition is a **palindrome**. Return *all possible palindrome partitioning of* `s`.

 

**Example 1:**

```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

**Example 2:**

```
Input: s = "a"
Output: [["a"]]
```

 

**Constraints:**

- `1 <= s.length <= 16`
- `s` contains only lowercase English letters.



## Solution

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def isPalindrome(i, j):
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        def backtrack(i):
            if i == len(s):
                res.append(curr.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    curr.append(s[i:j+1])
                    backtrack(j+1)
                    curr.pop()
        backtrack(0)
        return res
```

TC: O(n * 2 ^ n) since there are 2^n possible substring and worst case each of them takes O(n) to generate and determine if it is a palindrome

SC: O(n) extra space and O(n * 2 ^ n) space for the output list.