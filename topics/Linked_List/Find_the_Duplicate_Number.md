# Find the Duplicate Number

https://leetcode.com/problems/find-the-duplicate-number/description/

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return *this repeated number*.

You must solve the problem **without** modifying the array `nums` and using only constant extra space.

 

**Example 1:**

```
Input: nums = [1,3,4,2,2]
Output: 2
```

**Example 2:**

```
Input: nums = [3,1,3,4,2]
Output: 3
```

**Example 3:**

```
Input: nums = [3,3,3,3,3]
Output: 3
```

 

**Constraints:**

- `1 <= n <= 105`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- All the integers in `nums` appear only **once** except for **precisely one integer** which appears **two or more** times.

 

**Follow up:**

- How can we prove that at least one duplicate number must exist in `nums`?
- Can you solve the problem in linear runtime complexity?



**Reflections**:

- this is a linked list problem: 
  - either start with node.val=0, node.next=nums[0]
  - or start with node.val=nums[0], node.next=nums[nums[0]]
- Floyd algorithm:
  - fast and slow ptr meets
  - another slow ptr (slow2) begins at the beginning, and move slow ptr at the same time, the place they meet is the duplicate (where the cycle starts)



## Solution

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break

        slow2 = 0

        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        
        return slow
```

TC: O(n)

SC: O(1)