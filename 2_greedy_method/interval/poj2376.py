"""
Problem URL : http://poj.org/problem?id=2376

Time: 22:45-23:20

苦戦した理由 : 区間から長いものから順に使用していけば良いという発想にすぐならなかった.
"""

n,t=map(int,input().split())
cows=[]

for i in range(n):
    s,g=map(int,input().split())
    s,g=s-1,g-1
    cows.append((s,g,g-s))

#区間が長いものから使用していけば良い.

new_cows=sorted(cows,key=lambda x:x[2],reverse=True)
#λ関数を使用して,区間でソートをする

Finished=[False]*t

ans=0
flag=0
for s,g,r in new_cows:
    ans+=1
    for i in range(s,g+1):
        Finished[i]=True
    if all(Finished):
        flag=1
        break

print(ans if flag==1 else -1)
