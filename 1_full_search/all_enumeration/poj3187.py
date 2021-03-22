"""
problem URL: http://poj.org/problem?id=3187

Time:20:43-20:57

苦戦しなかった理由: 再帰構造で簡単に解けることがわかったから.
"""

n,f=map(int,input().split())

import itertools

def calc(l,m):
    """
    長さmのあるリストが入ってきたときのfinalを計算する
    """
    nl=[]
    if m==1:
        return l[0]
    else:
        for i in range(m-1):
            nl.append(l[i]+l[i+1])
        return calc(nl,m-1)

for x in itertools.permutations(range(1,n+1)):
    final=calc(list(x),n)
    #タプルだとimmutableのため関数の処理としてはlistで扱うことにした
    if final==f:
        ans=x
        break

[print(x,end=' ') for x in ans]
print()