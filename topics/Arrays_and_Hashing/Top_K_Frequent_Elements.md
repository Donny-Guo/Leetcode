# Top K Frequent Elements

https://leetcode.com/problems/top-k-frequent-elements/description/

Given an integer array `nums` and an integer `k`, return *the* `k` *most frequent elements*. You may return the answer in **any order**.

 

**Example 1:**

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]
```

 

**Constraints:**

- `1 <= nums.length <= 105`
- `-104 <= nums[i] <= 104`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is **unique**.

 

**Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.



**Reflection**:

1. python heapq module is min heap: every parent node has a value less than or equal to any of its children

   1. Zero-index: smallest item is heap[0]

   2. `heapq.heappush(heap, item)`
   3. `heapq.heappop(heap)`
   4. `heapq.heapfiy(x)`: turn x into a heap in linear time

2. how to use Counter

   ```python
   from collections import Counter
   nums = [1,2,1,3,4,2,3]
   cnt = Counter(nums)
   cnt.most_common(2) # get 2 most common elements
   
   # other usage
   c.total()                       # total of all counts
   c.clear()                       # reset all counts
   list(c)                         # list unique elements
   set(c)                          # convert to a set
   dict(c)                         # convert to a regular dictionary
   c.items()                       # access the (elem, cnt) pairs
   Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
   c.most_common()[:-n-1:-1]       # n least common elements
   ```

3. min heap:

   1. use heapify and then pop k elements
   2. keep heap size to k

   

## Simple Sort

```python
from collections import defaultdict
from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get freq
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        # sort the freq dict by value
        freq = sorted(freq.items(), reverse=True, key=itemgetter(1))

        # return
        return [freq[i][0] for i in range(k)]
```

TC: O(n log n)

SC: O(n)

## Priority Queue 

Solution 1: pop k elements

```python
import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count freq
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        # create priority queue (heapq is a min heap)
        pq = []
        for key, value in freq.items():
            pq.append((-value, key))
        heapq.heapify(pq)

        # pop k elements from the priority queue
        res = []
        for i in range(k):
            res.append(heapq.heappop(pq)[1])

        return res
```

TC: O(n+k log n)

SC: O(n)

---

Solution 2: keep the size of heap to k

```python
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count freq
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        # create heap
        heap = []

        for key, value in freq.items():
            # add to heap until size is k
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            else: # len == k
                if value > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (value, key))
            
        # return result
        return [heapq.heappop(heap)[1] for _ in range(k)]
```

TC: O(n + n log k) = O(n log k)

SC: O(n)

## Bucket Sort

```python
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count freq
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        # create bucket
        n = len(nums)
        bucket = [[] for _ in range(n+1)]

        # put items in freq to bucket
        for key, value in freq.items():
            bucket[value].append(key)

        # go through bucket in reverse order and output
        res = []
        for i in range(n, -1, -1):
            for elem in bucket[i]:
                res.append(elem)
            if len(res) == k:
                return res
```

TC: O(n)

SC: O(n)

## Use Counter module

Ref: https://docs.python.org/3/library/collections.html#collections.Counter

```python
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create counter obj
        counter = Counter(nums)
        # return most common
        return [item[0] for item in counter.most_common(k)]
```

TC: ? not sure how "most_common" function is implemented

SC: O(n)