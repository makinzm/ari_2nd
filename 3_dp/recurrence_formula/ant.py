"""
Problem URL: http://poj.org/problem?id=3046

Time:13:09-14:21

苦戦した理由:dpの再起構造を作ることに慣れていなかったから
しかし,これでは計算量の多いアルゴリズムとなってしまうため,改善の余地があると思う.
10^7だからセーフ?

poke around: look around a place, typically in search of something.

sibling:[n]each of two or more children or offspring having one or both parents in common; a brother or sister.
"""
import collections

t,a,s,b=map(int,input().split())

dp=[[-1 for _ in range(t+1)] for _ in range(a+1)]
##dp[x][i]:i種類までの家族を見て作れる個数xの構成の数を返す.

lst=[]
for i in range(a):
    lst.append(int(input()))

c=collections.Counter(lst).most_common()

dp[0][0]=1
#長さ0のは作れるとする.

for i in range(1,t+1):
    for x in range(0,a+1):
        if dp[x][i-1]>=0:
            dp[x][i]=dp[x][i-1]
        else:
            dp[x][i]=0
        for k in range(1,c[i-1][1]+1):
            if x-k>=0 and x-k<=a and dp[x-k][i-1]>0:
                dp[x][i]+=dp[x-k][i-1]
ans=0
for x in range(s,b+1):
    ans+=dp[x][t]
print(ans)
