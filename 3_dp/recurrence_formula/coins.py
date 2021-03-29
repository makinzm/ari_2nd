"""
Problem URL: http://poj.org/problem?id=1742

time:16:52-17:52

苦戦理由: どのような漸化式を立てるのかを考えることが難しかった

p62の個数制限付き部分和問題
"""

ans_lst=[]
while(True):
    n,m=map(int,input().split())
    if(n==0 and m==0):
        break
    tmp=list(map(int,input().split()))
    a=[0]+tmp[:n]
    c=[0]+tmp[n:]

    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    """
    dp[i][j]:i番目 'まで' を使用してjを作る際に,iが余る最大の枚数
    (0<=i<=n,0<=j<=m)
    """
    #またこのdpはdp[i-1]しか見ないため,再帰的に配列を使用することも可能
    dp[0][0]=0
    for i in range(1,n+1):
        for j in range(m+1):
            if dp[i-1][j]>=0:
                dp[i][j]=c[i]
            elif j<a[i] or dp[i][j-a[i]]<=0:
                dp[i][j]=-1
            else:
                dp[i][j]=dp[i][j-a[i]]-1
    ans=0
    for i in range(1,m+1):
        if dp[-1][i]>=0:
            ans+=1

    ans_lst.append(ans)

[print(ans) for ans in ans_lst]