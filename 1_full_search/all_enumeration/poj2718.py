"""
problem URL: http://poj.org/problem?id=2718

Time: 19:20-19:34,19:48-20:14

苦戦した理由: n!通り試す方法をimport itertoolsで行うこと
     英語を読むのが遅かった.
"""
import itertools

n=int(input())

def calculate_min(lst1,lst2):
    """
    lst1とlst2から作成できる数字の並びのうち絶対値が最小のものを出力する.
    しかし,先頭の文字が0のものは除去する
    """
    ans=10**10
    for x in itertools.permutations(lst1):
        for y in itertools.permutations(lst2):
            sx="".join(map(str,x))
            sy="".join(map(str,y))
            if sx[0]=='0' or sy[0]=='0':
                continue
            else:
                xx=int(sx)
                yy=int(sy)
            ans=min(ans,abs(xx-yy))
    return ans

anslst=[]

for i in range(n):
    lst=list(map(int,input().split()))
    ans=10*10
    for j in range(2**(len(lst))):
        lst1,lst2=[],[]
        for k in range(len(lst)):
            if (j>>k)&1:
                lst1.append(lst[k])
            else:
                lst2.append(lst[k])
        if len(lst1)==len(lst)//2 or len(lst2)==len(lst)//2:
            cand=calculate_min(lst1,lst2)
            ans=min(ans,cand)
    anslst.append(ans)

[print(x) for x in anslst]