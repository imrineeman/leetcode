#1221. Split a String in Balanced Strings
#Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

#Given a balanced string s, split it in the maximum amount of balanced strings.

#Return the maximum amount of split balanced strings.

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        stack = {
            'l' : 0,
            'r' : 0,
        }
        output = 0
        for c in s:
            if c == 'R':
                stack['r'] +=1
            else:
                stack['l'] +=1
            if stack['r'] == stack['l']:
                output +=1
                stack['r']=0
                stack['l']=0
                
        return output
        