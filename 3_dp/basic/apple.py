"""
Problem URL: http://poj.org/problem?id=2385

bruise: /bruːz/
[n]:an injury appearing as an area of discoloured skin on the body,
 caused by a blow or impact rupturing underlying blood vessels.
[v]:inflict a bruise or bruises on (a part of the body).

Time: 0:00-1:00

苦戦した理由: dp_lstを[[]*t]*wにすると参照先が同じとなってしまい
        更新がうまくいかないことを知らなかった.

python実験
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
>>> lst=[[0]*2]*3
>>> lst
[[0, 0], [0, 0], [0, 0]]
>>> lst[1][1]=1
>>> lst
[[0, 1], [0, 1], [0, 1]]
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
"""
t,w=map(int,input().split())

lst=[]
for i in range(t):
    lst.append(int(input()))

dp_lst=[[-1 for _ in range(w+1)] for _ in range(t+1)]

def to_int(boolean):
    """
    booleanがTrueなら1をFalseなら0を返す
    """
    return 1 if boolean else 0

def dp(time,x):
    """
    timeにおいて,x回だけ木の移動をした際の最大の取れる数を返す.
    """
    global dp_lst
    if x==0 and time==0:
        dp_lst[time][x]=0
    """
    elif x==0 and time==1:
        dp_lst[time][x]=to_int(lst[time-1]==1)
    elif x==1 and time==1:
        dp_lst[time][x]=to_int(lst[time-1]==2)
    """
    if x<0 or time<0 or x>time:
        return 0
    if dp_lst[time][x]==-1:
        if x%2==0:
            #1の木にいる
            dp_lst[time][x]=max(dp(time-1,x),dp(time-1,x-1))+to_int(lst[time-1]==1)
        else:
            #2の木にいる.
            dp_lst[time][x]=max(dp(time-1,x),dp(time-1,x-1))+to_int(lst[time-1]==2)
    return dp_lst[time][x]

k=dp(t,w)

print(dp_lst[t][w])