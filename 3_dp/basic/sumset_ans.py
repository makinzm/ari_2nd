"""
参考URL: https://tsutaj.hatenablog.com/entry/2018/03/04/012113
"""

n=int(input())

MOD=1000000000

dp=[0]*(n+1)

dp[1]=1
i=1
while(i<=n):
    print('===={}===='.format(i))
    for j in range(i,n+1):
        dp[j] += dp[j-i]
        dp[j] %=MOD
        print(dp)
    print('===={}===='.format(i))
    i*=2
print(dp[n])

"""
このように回すことによって,
1loop目で2^0=1を使う通りを全て確かめ
2loop目で2^0と2^1を一つ以上使う通りを全て確かめてといったように,
重なりを無くして足し合わせることができる.
"""