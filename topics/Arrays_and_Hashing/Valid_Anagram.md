# Valid Anagram

https://leetcode.com/problems/valid-anagram/description/

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

 

**Example 1:**

**Input:** s = "anagram", t = "nagaram"

**Output:** true

**Example 2:**

**Input:** s = "rat", t = "car"

**Output:** false

 

**Constraints:**

- `1 <= s.length, t.length <= 5 * 104`
- `s` and `t` consist of lowercase English letters.

 

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?



Reflections:

1. how to compare two dictionaries? `==`  This operator checks if two objects are equal, and for dictionaries, it verifies if both dictionaries have the same keys and values.
2. Add/update items in dict: `thisdict.update({"color": "red"})` must be a dictionary 
3. Empty the dictionary: `thisdict.clear()`
4. Remove item: `thisdict.pop('color')`
5. make a copy of the dictionary: `new_dict = thisdict.copy()