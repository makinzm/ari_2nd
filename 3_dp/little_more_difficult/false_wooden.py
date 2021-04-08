"""
Problem URL:http://poj.org/problem?id=1065

time: 17:01-17:48
"""

n=int(input())
tmp_lst=list(map(int,input().split()))
lst=[]
for i in range(n):
    lst.append((tmp_lst[2*i],tmp_lst[2*i+1]))

"""
dp[i][c]: コストcまででiのをできるかどうか? <- true falseは良くないからX

dp[i][l]: 番号がi以上 i+l以下の木材にかかる最小のコスト
dp[i][l]=min{dp[i][l-1]+func(i,l-1,i+l),dp[i+1][l-1]+func(i+1,l-1,i)}
func(i,l,x): 番号がi以上 i+l以下の木材にxよりwとlともに同じ不等号であるものが存在するかどうかを判定
    存在する場合は0を返し,存在しない場合は1を返す.
funcのorderはO(n)
dpのfor回数はO(n^2)　=> O(n^3)そのため X

dp[i]: 番号0からi番目までの木材にかかる最小のコスト
dp[0]=1
dp[i]=dp[i-1]+func(i-1,i)
func(i,x): 番号が0からi番目までの木材の中でwとlともに同じ不等号であるものが存在するかどうかを判定
    存在する場合は0を返し,存在しない場合は1を返す.
    しかし,これだと,既に組み合わせたものを考慮していない状況下にあるため,
    どれとどれがsetになっているかの状況も見る必要があり困難になる
"""
dp=[0 for _ in range(n)]
dp[0]=1
def func(l,x):
    flag=1
    for i in range(l+1):
        if not ((lst[x][0]>=lst[i][0])^(lst[x][1]>=lst[i][1])):
            flag=0
            break
    return flag

for i in range(1,n):
    dp[i]=dp[i-1]+func(i-1,i)
    print(dp)
print(dp[n-1])