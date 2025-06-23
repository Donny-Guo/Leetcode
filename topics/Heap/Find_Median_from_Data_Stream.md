# Find Median from Data Stream

https://leetcode.com/problems/find-median-from-data-stream/description/

The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

- For example, for `arr = [2,3,4]`, the median is `3`.
- For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

Implement the MedianFinder class:

- `MedianFinder()` initializes the `MedianFinder` object.
- `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
- `double findMedian()` returns the median of all elements so far. Answers within `10-5` of the actual answer will be accepted.

 

**Example 1:**

```
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

 

**Constraints:**

- `-105 <= num <= 105`
- There will be at least one element in the data structure before calling `findMedian`.
- At most `5 * 104` calls will be made to `addNum` and `findMedian`.

 

**Follow up:**

- If all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?
- If `99%` of all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?



**Reflections**:

- since we just need to find the median, we focus on finding the middle value. However, inserting in-order takes O(n) -> we can optimize it by split the array into two almost similar size heap

## Solution 1: insert in-order

```python
class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        nums = self.nums
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < num:
                left = mid + 1
            elif nums[mid] >= num:
                right = mid - 1
        nums.insert(left, num)
        
    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2 == 1:
            return self.nums[n // 2]
        else:
            # n = 4
            # 0 1 2 3
            return (self.nums[n // 2] + self.nums[n // 2 - 1]) / 2
```

TC: O(1) for findMedian and O(n) for addNum

SC: O(n)

## Solution 2: heap

```python
import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        small, large = self.small, self.large

        if small and num > -self.small[0]:
            heapq.heappush(large, num)
        else:
            heapq.heappush(small, -num)
        
        if abs(len(small) - len(large)) == 2:
            if len(small) > len(large):
                item = heapq.heappop(small)
                heapq.heappush(large, -item)
            else:
                item = heapq.heappop(large)
                heapq.heappush(small, -item)

    def findMedian(self) -> float:
        s_len = len(self.small)
        l_len = len(self.large)
        if s_len == l_len:
            return (-self.small[0] + self.large[0]) / 2
        elif s_len > l_len:
            return -self.small[0]
        else:
            return self.large[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```

TC: O(1) for findMedian and O(log n) for addNum

SC: O(n)