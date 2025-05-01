# Median of Two Sorted Arrays

https://leetcode.com/problems/median-of-two-sorted-arrays/description/

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

 

**Example 1:**

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

**Example 2:**

```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

 

**Constraints:**

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-106 <= nums1[i], nums2[i] <= 106`



**Reflections**:

- do binary search on shorter array
- Compare boundary values and move ptrs



## Solution

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        if len(A) > len(B):
            A, B = B, A
        
        # do binary search in A
        left, right = 0, len(A) - 1
        while True:
            mid = (left + right) // 2
            Aleft = A[mid] if mid >= 0 else float('-inf')
            Aright = A[mid+1] if mid+1<len(A) else float('inf')
            j = half - mid - 2
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j+1] if j+1 < len(B) else float('inf')
            if (Aleft <= Bright and Bleft <= Aright):
                # odd
                if total % 2 == 1:
                    return min(Aright, Bright)

                else:# even
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = mid - 1

            elif Bleft > Aright:
                left = mid + 1
```

TC: O(log(min(m, n)))

SC: O(1)