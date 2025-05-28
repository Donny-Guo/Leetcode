# Reorganize String

https://leetcode.com/problems/reorganize-string/description/

Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same.

Return *any possible rearrangement of* `s` *or return* `""` *if not possible*.

 

**Example 1:**

```
Input: s = "aab"
Output: "aba"
```

**Example 2:**

```
Input: s = "aaab"
Output: ""
```

 

**Constraints:**

- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.



**Reflections**:

- Pick the most freq and then hold
- Use heap to get the most freq char



---

## Solution1 (store prev)

```python
import heapq
from collections import defaultdict
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        
        res = ''
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)
        prev = None

        while True:
            if not maxHeap:
                if prev: return ''
                else: break
                
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt < 0:
                prev = [cnt, char]
        return res
```

TC: O(n log(26))

SC: O(log(26))

## Solution2: 

```python
from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        res = ''
        while maxHeap:
            # pop
            a = heapq.heappop(maxHeap)
            res += a[1]
            a[0] += 1

            # pop
            if maxHeap:
                b = heapq.heappop(maxHeap)
                res += b[1]
                b[0] += 1
            else:
                return '' if a[0] < 0 else res

            # push and push
            if b[0] < 0:
                heapq.heappush(maxHeap, b)
            if a[0] < 0:
                heapq.heappush(maxHeap, a)
        return res
```

TC: O(n log(26))

SC: O(log(26))

