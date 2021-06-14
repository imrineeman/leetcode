#53.Maximum subarray
#O(n) solution

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largest = -2**31
        curr = 0
        if len(nums) == 1:
            return nums[0]
        
        for i in range(len(nums)):
            if i == 0:
                curr = nums[i]
            elif i < len(nums):
                curr = max(curr + nums[i],nums[i])
            largest = max(curr,largest)
        return largest
                
        