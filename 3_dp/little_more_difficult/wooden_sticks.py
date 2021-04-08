"""
Problem URL:http://poj.org/problem?id=1065

Reference URL: https://tsutaj.hatenablog.com/entry/2018/03/04/012113

dpではないけどいいのかな?
"""

t=int(input())
ans_lst=[]

for _ in range(t):
    n=int(input())
    tmp_lst=list(map(int,input().split()))
    lst=[]
    for i in range(n):
        lst.append((tmp_lst[2*i],tmp_lst[2*i+1]))

    lst.sort(key=lambda x:x[0])
    lst.sort(key=lambda x:x[1])
    ## 長さに関してsortした後に重さに関してsortする
    ## このことで,重さに関してのみ見ると,これ以上時間を取る必要のない状態となった.
    ## そして,追加する要素のうち最大のものを記憶するようにして考える.
    ## ここでグループ化する順番は重さに関して昇順であることが保証されているため,
    ## 最大のものより小さいものに関しての記憶はなくても,
    ## 最大のものを参照して追加できない場合は結局グループ化する必要が発生するため,覚えなくて良い.

    group=[]
    for i in range(n):
        flag=0
        for j in range(len(group)):
            if not ((lst[i][0]>=group[j][0])^(lst[i][1]>=group[j][1])):
                flag=1
                del group[j]
                group.append(lst[i])
                break
        if flag==0:
            group.append(lst[i])
    if len(group)==0:
        ans=1
    else:
        ans=len(group)
    ans_lst.append(ans)
[print(ans) for ans in ans_lst]
