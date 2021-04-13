"""
problem URL: http://poj.org/problem?id=1631

Time:12:19-13:00

苦戦した理由: 英語を読むのが遅かったこと.
    dpの設定をすぐに思い付けなかったこと.
"""
n=int(input())
ans_lst=[]

for _ in range(n):
    p=int(input())
    lst=[]
    for i in range(p):
        lst.append(int(input()))

    INF=40001
    dp=[[INF for _ in range(p+1)]for _ in range(p+1)]
    ## dp[i+1][x]:0からi本までをx本 使用して到達する最小の端の場所.(I={0,...,p-1},X={0,...,p})
    ## dp[i+1][x]=min{dp[i][x],max{lst[i],dp[i][x-1]}}
    ## Orderは16*(10^8)=O(10^9)...?
    ## 多分違うけどとりあえず実装

    for i in range(p):
        dp[i][0]=0

    for i in range(p):
        for x in range(1,p+1):
            if lst[i]>dp[i][x-1]:
                dp[i+1][x]=min(dp[i][x],lst[i])
            else:
                dp[i+1][x]=dp[i][x]

    for i in range(p,-1,-1):
        if dp[p][i]!=INF:
            ans=i
            break
    ans_lst.append(ans)

[print(ans) for ans in ans_lst]