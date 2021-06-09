#1470. Shuffle the Array

#Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

#Return the array in the form [x1,y1,x2,y2,...,xn,yn].



class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=0
        y=n
        newlist = []
        i = 0
        while i < n:
            newlist.append(nums[x+i])
            newlist.append(nums[y+i])
            i+=1
        
        return newlist
        