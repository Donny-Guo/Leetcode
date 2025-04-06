# Group Anagrams

https://leetcode.com/problems/group-anagrams/description/

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

 

**Example 1:**

**Input:** strs = ["eat","tea","tan","ate","nat","bat"]

**Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]

**Explanation:**

- There is no string in strs that can be rearranged to form `"bat"`.
- The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.
- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

**Example 2:**

**Input:** strs = [""]

**Output:** [[""]]

**Example 3:**

**Input:** strs = ["a"]

**Output:** [["a"]]

 

**Constraints:**

- `1 <= strs.length <= 104`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.



**Reflections**:

- dict key can not be a list, turn it into tuple; 
- create unique key:
  - Sort the string
  - count freq for each letter
    - Option1: start from [0] * 26
    - Option2: start from empty dict, and sort by key later
      - sorted(freq.items(), key=itemgetter(0)) `from operator import itemgetter`
  - return list: `return list(res.values())`



Solution 1: sort the string

```python
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            res[key].append(s)
        
        return list(res.values())
```



Solution 2: count freq - Option1

```python
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list) 
        for s in strs:
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(s)
        
        return list(res.values())
```



Solution 3: count freq - Option2

```python
from collections import defaultdict
from operator import itemgetter

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = defaultdict(list)
        for s in strs:
            key = self.get_key(s)
            group[key].append(s)
        
        res = []
        for key in group.keys():
            res.append(group[key])
        return res

    def get_key(self, s: str) -> str:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1

        new_freq = sorted(freq.items(), key=itemgetter(0))
        new_list = [str(k)+str(v) for k, v in new_freq]
        anagram_key = ''.join(new_list)
        return anagram_key
```

