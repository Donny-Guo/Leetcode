'''
Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

Example:
>>> min_sub_array_length([2,3,1,2,4,3], 7)
2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
'''

def min_sub_array_length(nums, s):
    start_idx = 0
    min_length, subarray_sum = float('inf'), 0
    for end_idx in range(len(nums)):
        subarray_sum += nums[end_idx]
        while subarray_sum >= s:
            min_length = min(min_length, end_idx-start_idx + 1)
            subarray_sum -= nums[start_idx]
            start_idx += 1
    if min_length == float('inf'):
        return 0
    return min_length

def main():
    a = [2,3,1,2,4,3]
    s = 7
    print(min_sub_array_length(a, s))

if __name__ == "__main__":
    main()