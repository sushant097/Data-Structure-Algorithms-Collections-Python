'''
Climbing Staris:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

# Brute Force Solution
class Solution:
    def climbStairs(self, n: int) -> int:
        def countClimbStairs(i, n):
            if i > n:
                return 0
            if i == n:
                return 1
            
            return countClimbStairs(i+1, n) + countClimbStairs(i+2, n)
        
        return countClimbStairs(0, n)

class Solution:
    def climbStairs(self, n: int) -> int:
        lPoint, rPoint = 0, 1
        for i in range(n+1):
            temp = lPoint
            lPoint = lPoint + rPoint
            rPoint = temp
        return lPoint


class Solution:
    def climbStairs(self, n: int) -> int:
        c1 = 1
        c2 = 1
        for i in range(n-1):
            next = c1 + c2
            c1= c2
            c2 = next
        return c2



        
    