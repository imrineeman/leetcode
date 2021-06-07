#3. Longest Substring Without Repeating Characters

#Given a string s, find the length of the longest substring without repeating characters.


class Solution:
    
    def compute(self,c):
        score=0
        for i in c:
            if c[i] == 1:
                score +=1
            elif c[i] > 1:
                return 0
        return score
            
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = {}
        reset = {}
        bestOne = {}
        bestScore = 0
        
        if len(s) == 1:
            return 1
        
        # Init counter
        for i in s:
            counter[i] = 0
            reset[i] = 0
            
        # Iterate over letters
        for i in s:   
            for c in s:
                counter[c] += 1
                score = self.compute(counter)
                
                if score > bestScore:
                    bestScore = score
                    bestOne = counter.copy()
            for k in counter:
                counter[k] = 0
            s = s[1:]
            
        return bestScore                

            
        