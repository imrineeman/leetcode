#14. Longest Common Prefix

#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        s = strs[0]
        
        for i in range (len(s)):
            let = s[i]
            curr = ''
            
            for j in range (1,len(strs)):
                curr = strs[j][i]
                if curr == let and j == len(strs)-1:
                    res += let
                elif curr != let:
                    return res
                
        return res
    