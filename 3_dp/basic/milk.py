"""
Problem URL: http://poj.org/problem?id=3616

Time: 12:30-13:52

overlap: /əʊvəˈlap/ extend over so as to cover partly.

苦戦した理由: 
    lstをending_timeでソートする必要があることに気づかなかったこと
    エラーの原因がIndentのズレによるものだったと気づけなかったこと
"""

n,m,r=map(int,input().split())

lst=[]
for i in range(m):
    start,ending,efficiency=map(int,input().split())
    lst.append((start,ending,efficiency))

lst.sort(key=lambda x: x[1])

dp_lst=[0 for _ in range(n+1)]

dp_lst[0]=0

nl=lst

for time in range(1,n+1):
    if dp_lst[time]==0:
        flag=time
        nl=[(s,e,eff) for(s,e,eff) in nl if e>=time]
        for s,e,eff in nl:
            if time==e:
                flag=-1
                if s-r<0:
                    dp_lst[time]=max([eff,dp_lst[time-1],dp_lst[time]])
                else:
                    dp_lst[time]=max([dp_lst[s-r]+eff,dp_lst[time-1],dp_lst[time]])
            else:
                if flag==-1:
                    break
                else:
                    dp_lst[time]=dp_lst[time-1]
                    break
print(dp_lst[n])


# Noneが返ってきたしまいmax計算がうまくいかなかった
# Indexの位置がずれていた.
#
# また関数の方がlstの更新を行えないためlstの探索が多いため,計算量として好ましくない
# また関数でstの更新を行うためには,どのlstを探索させるかをいちいち考える必要があるため好ましくない.
# 関数でないものは先頭から順にdp_lstだけでなく,lstも減らしながら更新できるため効率が良い

dp_lst=[0 for _ in range(n+1)]
nl=lst

def dp(time):
    """
    時刻timeにおける最大の生産量を返す
    """
    global dp_lst
    if time <= 0:
        return 0
    else:
        if dp_lst[time]==0:
            flag=time
            for s,e,eff in lst:
                if time==e:
                    dp_lst[time]=max([dp(s-r)+eff,dp(time-1),dp_lst[time]])
                    flag=-1
                else:
                    if flag==-1:
                        break
                    else:
                        dp_lst[time]=dp(time-1)
        return dp_lst[time]
print(dp(n))