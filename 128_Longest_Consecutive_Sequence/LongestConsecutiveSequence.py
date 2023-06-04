# O(n) time, although it looks like O(n^2), the while loop only
# runs for n iterations throughout the entire program, so
# runtime is O(n+n) is still O(n)
# O(n) space since we use the set for look-up table
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        seen = set(nums)
        length = 1
        for num in seen:
            if num - 1 in seen:
                continue
            else:
                curr = num + 1
                curr_length = 1
                while curr in seen:
                    curr_length += 1
                    curr += 1
                length = max(curr_length, length)
        return length