#3. Longest Substring Without Repeating Characters

#Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s):
        
        bank = {}
        currLength=0
        longest=0
        start=0
        
        for i,let in enumerate(s):
            
            if let in bank and bank[let] >= start:
                start = bank[let] + 1
                currLength = i - bank[let]
                bank[let] = i

                if currLength > longest:
                    longest = currLength
                    
            else:
                bank[let] = i
                currLength += 1
                if currLength > longest:
                    longest = currLength 
            
        return longest