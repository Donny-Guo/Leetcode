# https://leetcode.com/problems/two-sum/
'''
# O(n^2) solution (brute force)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
'''
'''
# Using dict (two pass): O(n) space and O(n) time
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = dict()
        for i in range(len(nums)):
            dict1[nums[i]] = i
        for i in range(len(nums)):
            expected = target - nums[i]
            if expected in dict1 and dict1[expected] != i:
                return [i, dict1[expected]]
'''

# Using dict (one pass): O(n) space and O(n) time
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = dict()
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in dict1:
                return [i, dict1[comp]]
            dict1[nums[i]] = i
        