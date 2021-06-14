#53. Maximum Subarray
#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largest = -2**31
        for i,num in enumerate(nums):
            curr = num
            if curr > largest:
                    largest = curr
            for j in range(i+1,len(nums)):
                curr += nums[j]
                if curr > largest:
                    largest = curr

        return largest
                