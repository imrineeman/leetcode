#322. Coin Change
#You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

#Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

#You may assume that you have an infinite number of each kind of coin.


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        
        dp[0] = 0
        
        for i in range(len(dp)):
            for c in coins:
                
                if i - c >= 0:
                    dp[i] = min(dp[i],dp[i-c] +1) 
        
        return dp[-1] if dp[-1] < amount + 1 else -1