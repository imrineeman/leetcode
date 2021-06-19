#13. Roman to Integer


class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        map = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
            '0':0
        }
        
        map_s = {
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }
        l = list(s)
        
        for i in range(len(l)):
            if i+1 < len(s) and l[i]+l[i+1] in map_s:
                sum += map_s[l[i]+l[i+1]]
                l[i+1] = '0'
            else:
                sum +=map[l[i]]
                
        return sum