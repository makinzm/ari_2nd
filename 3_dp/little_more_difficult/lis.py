"""
problem URL: http://poj.org/problem?id=1631

この問題はLIS(longest Increasing Subsequence)と呼ばれる問題で,
参考図書のp63にも解法が載っているものである.

今回の場合,前から順に見ていけば良いため.
dp[i]=長さがi+1であるような増加部分列における最終要素の最小の値
とすれば更新していける.
"""
n=int(input())
ans_lst=[]
for _ in range(n):
    p=int(input())
    lst=[]
    for i in range(p):
        lst.append(int(input()))

    INF=40001
    dp=[INF for _ in range(p)]
    for i in range(p):
        up=p
        down=0
        if dp[down]>lst[i]:
            dp[down]=lst[i]
        else:
            while(up-down>=1):
                k=(up+down)//2
                if dp[k]>lst[i]:
                    up=k
                else:
                    down=k+1
            dp[up]=lst[i]

    for i in range(p-1,-1,-1):
        if dp[i]!=INF:
            ans=i+1
            break
    ans_lst.append(ans)
[print(ans) for ans in ans_lst]