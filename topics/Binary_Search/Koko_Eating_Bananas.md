# Koko Eating Bananas

https://leetcode.com/problems/koko-eating-bananas/description/

Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return *the minimum integer* `k` *such that she can eat all the bananas within* `h` *hours*.

 

**Example 1:**

```
Input: piles = [3,6,7,11], h = 8
Output: 4
```

**Example 2:**

```
Input: piles = [30,11,23,4,20], h = 5
Output: 30
```

**Example 3:**

```
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```

 

**Constraints:**

- `1 <= piles.length <= 104`
- `piles.length <= h <= 109`
- `1 <= piles[i] <= 109`



**Reflections**:

1. While loop condition: left <= right, 
2. Update left, right ptr: right = mid-1
3. return which result



## Solution

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # edge case
        if len(piles) == h:
            return max(piles)

        left, right = 1, max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            
            if hours <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res
```

TC: O(n*logm), n = len(piles), m = max(piles)

SC: O(1)