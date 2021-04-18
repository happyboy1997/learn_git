class Solution:
    def nthUglyNumber(self, n: int) -> int:
        a,b,c=0,0,0
        dp = [1 for _ in range(n)]
        for i in range(1,n):
            x,y,z = 2*dp[a],3*dp[b],5*dp[c]
            dp[i] = min(x,y,z)
            if dp[i]==x:
                a+=1
            if dp[i]==y:
                b+=1
            if dp[i]==z:
                c+=1
        return dp[n-1]