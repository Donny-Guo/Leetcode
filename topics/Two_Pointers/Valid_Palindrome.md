# Valid Palindrome

https://leetcode.com/problems/valid-palindrome/description/
A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` *if it is a **palindrome**, or* `false` *otherwise*.

 

**Example 1:**

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

**Example 2:**

```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

**Example 3:**

```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

 

**Constraints:**

- `1 <= s.length <= 2 * 105`
- `s` consists only of printable ASCII characters.



**Reflections**:

1. some common methods with string: 
   1. `s.isalnum()`
   2. `s.isnumeric()`
   3. `s.isalpha()`
   4. `s.lower()`
   5. `s.upper()`



## Solution1: create new string

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean up string
        new_s = ''.join([c.lower() for c in s if c.isalnum()])

        # two ptr
        left, right = 0, len(new_s) - 1
        while left < right:
            if new_s[left] == new_s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
```

TC: O(n)

SC: O(n)



## Solution2: two-ptr only

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            
            if not s[right].isalnum():
                right -= 1
                continue
            
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        
        return True
```

TC: O(n)

SC: O(1)