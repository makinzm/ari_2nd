# https://sune2.hatenadiary.org/entry/20120719/1342658409

# sunscreen.pyにおいて,最もmaxSPFが小さいものから順に使用する.
# (そうしなければ,最大の数を求められないため)
INF=10**4

c,l=map(int,input().split())

cows=[]
for i in range(c):
    cows.append(list(map(int,input().split())))

lotion=[]
for i in range(l):
    lotion.append(list(map(int,input().split())))

cows.sort(key=lambda x:x[0])
lotion.sort(key=lambda x:x[0])

ans=0
i,j=0,0
for j in range(l):
    h=[]
    for i in range(c):
        if cows[i][0]<=lotion[j][0] and cows[i][1]>=lotion[j][0] and lotion[j][1]>0:
            h.append((i,cows[i]))
    if len(h)!=0:
        h.sort(key=lambda x:x[1][1])
        #print(h,lotion[j])
        #print(cows[h[0][0]])
        cows[h[0][0]][0]=INF
        lotion[j][1]-=1
        ans+=1
print(ans)
