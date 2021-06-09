#7. Reverse Integer

#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        maxInt = 2**31 -1
        minInt = -2**31
        if x == 0:
            return 0
        elif x > 0:
            strx = str(x)
            revStr = strx[::-1]
            revInt = int(revStr)
            if revInt > maxInt or revInt < minInt:
                return 0
            else: 
                return revInt
        elif x < 0:
            strx = str(x)
            revStr = strx[::-1]
            revStr = revStr[:(len(revStr)-1)]
            revInt = int(revStr)
            revInt = -revInt
            if revInt > maxInt or revInt < minInt:
                return 0
            else:
                return revInt
        
      