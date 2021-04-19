"""
Problem URL: http://poj.org/problem?id=3666

Time : 15:22-16:03

It is difficult ...汗
"""

n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))

## aを反転させる事を考えて昇順の最小スコアのものを算出すれば良い
## 









"""
証明できなかったためOUT

コストの計算方法を考えると,dpで現在出現している数の中の最も大きい要素で構成される昇順のlistを作成していけば良い.?
まず昇順のリストである必要があるため,昇順にする必要がある.
そして,tmpの更新に関しての候補は
1. tmp<=a[i]の場合
　昇順にする必要があるため,tmpの候補kは tmp,...,a[i]となる.
  そして,その中で最もコストが安いのはa[i]である.
  というのもa[i]で今回増加するコストは0であるが,
  他の場合は|a[i]-k|がコストに加わる.
  そして,次のコストを計算する場合 tmp=kとなるが ←ここで論理が破綻
2. tmp>a[i]の場合
  昇順にする必要があるため,tmpをそのままにすることが最適コストとなる.

ans_lst=[]
for j in range(2):
    if j==1:
        a.reverse()
    ans=0
    tmp=a[0]
    for i in range(1,n):
        tmp=max(tmp,a[i])
        ans+=abs(tmp-a[i])
    ans_lst.append(ans)
print(min(ans_lst))
"""



