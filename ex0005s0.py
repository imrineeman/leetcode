#5. Longest Palindromic Substring

#Given a string s, return the longest palindromic substring in s.

class Solution:

    def longestPalindrome(self, s: str) -> str:
        longest= ''
        for i,let in enumerate(s):
            temp = s[i:]
            
            if len(temp) <= len(longest):
                return longest

            if len(s)<=1:
                print('ran all letters!')
                return s
            for l,letter in enumerate(temp):
                if l is not 0: 
                    temp2 = temp[:-l]
                else:
                    temp2 = temp
                if temp2 == temp2[::-1] and len(longest) <= len(temp2):
                    longest = temp2
                    break
                elif len(longest) > len(temp2):
                    break

                
            
                
        
        
        
                
            
                
        
        
        