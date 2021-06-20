# 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        map = {}
        
        for i in range(len(nums)):
            if nums[i] in map:
                return True
            else:
                map[nums[i]] = i
                
        return False
        