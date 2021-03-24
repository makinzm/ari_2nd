"""
Problem URL: http://poj.org/problem?id=2229

Time:13:34-14:18

I gave up ...
"""
import math

n=int(input())

dp=[-1]*(n+1)

for x in range(1,n+1):
    """
    xを2の累乗のみで作る場合の数を返す.
    """
    if dp[x]!= -1:
        continue
    else:
        if x==1:
            dp[x]=1
        else:
            m=math.log2(x)
            if m.is_integer():
                ans=1
            else:
                ans=0
            m=int(m)

            for i in range(m):

                #ans+=dp[x-2**i]
                #重なりの部分だけ大きい値になってしまう.
            dp[x]=ans
    print(dp[x])

