class Solution:
    def climbStairs(self, n: int) -> int:
        recentStair, stairBefore = 1, 1

        for i in range(n - 1):
            temp = recentStair
            recentStair = recentStair + stairBefore
            stairBefore = temp

        return recentStair