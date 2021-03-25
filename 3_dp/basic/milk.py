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

nl=lst
for time in range(1,n+1):
    if dp_lst[time]==0:
        flag=time
        while(nl!=[] and nl[0][1]==time):
            flag=-1
            s,e,eff=nl[0]
            # prev=max(0,s-r)として書いた方がきれいになる.
            if s-r<0:
                dp_lst[time]=max([eff,dp_lst[time-1],dp_lst[time]])
            else:
                dp_lst[time]=max([dp_lst[s-r]+eff,dp_lst[time-1],dp_lst[time]])
            nl=nl[1:]
        if flag!=-1:
            dp_lst[time]=dp_lst[time-1]
print(dp_lst[n])


# Noneが返ってきたしまいmax計算がうまくいかなかった
# Indexの位置がずれていた.
#
# また関数の方がlstの更新を行えないためlstの探索が多いため,計算量として好ましくない
# また関数でstの更新を行うためには,どのlstを探索させるかをいちいち考える必要があるため好ましくない.
# 関数でないものは先頭から順にdp_lstの更新だけでなく,考える仕事のlstも減らしながら更新できるため効率が良い

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