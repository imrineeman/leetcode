#1. Two Sum

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            num = target - i
            if num == i and nums.count(i) > 1:
                return [ n for n,d in enumerate(nums) if d == num]
            elif num == i:
                continue
            elif num in nums:
                return [nums.index(i),nums.index(num)]
            else:
                continue