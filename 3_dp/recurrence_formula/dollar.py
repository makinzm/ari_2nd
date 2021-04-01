"""
problem URL: http://poj.org/problem?id=3181

time: 17:26-17:55

苦戦した理由: 一元配列でもかけると思ったが,重複を考慮すると今考えるコインを使うか否かを分ける必要があることに
    初めのうちに気付けなかった.
"""

n,k=map(int,input().split())

# (dp[i][x]でi dollarの商品 まで使用して x dollarにする通りの数)
# ただし,dp[i][x]= dp[i-1][x]+dp[i][x-i]
### iを複数枚数使用することは,dp[i][x-i]の計算時に既に考えているため,考慮しなくて良い
# N*Kのorderのためいける.

dp=[[0 for _ in range(n+1)] for _ in range(k+1)]

for i in range(0,k+1):
    dp[i][0]=1

for i in range(1,k+1):
    for x in range(1,n+1):
        #ここに関して,場合わけを書かなくても上野式だけでもなぜかうまく計算できた.
        # というのもdp[i][x-i]はx-iが負の場合はpythonの性質で
        # dp[i][k+x-i+1]と同じ値であり,
        # その状況において dp[i][k+x-i+1]は
        # k+x-i+1>x <=> k+1 > i <=> 真 であるため
        # まだ更新されていない状況の値であり0である
        # その影響で場合分けを書かなくてもうまく計算ができる.
        if x-i>=0:
            dp[i][x]=dp[i-1][x]+dp[i][x-i]
        else:
            dp[i][x]=dp[i-1][x]

print(dp[k][n])