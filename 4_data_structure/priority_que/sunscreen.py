"""
Problem URL: http://poj.org/problem?id=3614

Time: 21:25-43 (問題文理解)
    9:44-9:58
"""
c,l=map(int,input().split())

cows=[]
for i in range(c):
    cows.append(list(map(int,input().split())))

lotion=[]
for i in range(l):
    lotion.append(list(map(int,input().split())))

"""
まず,少量のクリームでokな順に牛を並べて,少量のクリームから使用していく.
その際に,最大のクリーム量を個していない場合は塗り,そうでなければ永遠にpassする.
そして,クリームの塗った範囲を減少させるようにする.

そうすればO(c*l)<9*10^6 で実行できる
"""
cows.sort(key=lambda x:x[0])
lotion.sort(key=lambda x:x[0])

used_cows=[False for _ in range(c)]
ans=0
for i in range(c):
    for j in range(l):
        if not(used_cows[i]) and cows[i][0]<=lotion[j][0] and cows[i][1]>=lotion[j][0] and lotion[j][1]>0:
            ans+=1
            lotion[j][1]-=1
            used_cows[i]=True
            break
print(ans)