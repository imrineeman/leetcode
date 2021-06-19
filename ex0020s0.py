#20. Valid Parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            '}' : '{',
            ')' :'(',
            ']' : '['
        }
        
        stack = []
        stack.append(s[0])
        for i in range(1,len(s)):
            if s[i] in map and len(stack) >0 and stack[-1] == map[s[i]]:
                stack.pop()
            else:
                stack.append(s[i])
        if len(stack) ==0:
            return True
        return False
                
        
        
    
        
        