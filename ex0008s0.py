#8. String to Integer (atoi)

#Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).


class Solution:
    def myAtoi(self, s: str) -> int:
        counter = 0
        s = s.strip()

        if len(s) == 0:
            return 0        
        
        res=''
        sign = 1
        if len(s) == 1:
            if s[0].isdigit():
                return s
            else:
                return 0
        
        elif s[0].isdigit():
            for i in s:
                if i.isdigit():
                    res +=i
                else:
                    return (max(-2**31, min((sign*int(res)),2**31-1)))
            return (max(-2**31, min((sign*int(res)),2**31-1)))
        else:
            if s[0] == '.':
                return 0
            if s[0].isalpha():
                return 0
            elif s[1].isdigit():
                sign = -1 if s[0] == '-' else 1
                s = s[1:]
                for i in s:
                    if i.isdigit():
                        res +=i
                    else:
                        return (max(-2**31, min((sign*int(res)),2**31-1)))
                return (max(-2**31, min((sign*int(res)),2**31-1)))
            else:
                return 0
            