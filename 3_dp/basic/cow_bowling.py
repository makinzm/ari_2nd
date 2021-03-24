"""
Problem URL: http://poj.org/problem?id=3176

Time: 13:06-13:21

苦戦した理由: 英語がスムーズに読めなかった.
though: 接続詞でも使用できて「ただし,」
diagonally adjascent: 対角上に隣接
"""

n=int(input())

lst=[]
dp_lst=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    dp_tmp=[-1]*(i+1)
    lst.append(tmp)
    dp_lst.append(dp_tmp)

def dp(i,j):
    """
    i行目のj列目に到達する際の最大値を返す.
    """
    global dp_lst
    if dp_lst[i][j]!=-1:
        return dp_lst[i][j]
    else:
        if i==0:
            dp_lst[i][j]=lst[i][j]
            return dp_lst[i][j]
        if j==0:
            dp_lst[i][j]=lst[i][j]+dp(i-1,0)
            return dp_lst[i][j]
        if i==j:
            dp_lst[i][j]=lst[i][j]+dp(i-1,j-1)
            return dp_lst[i][j]
        else:
            dp_lst[i][j]=max(dp(i-1,j-1),dp(i-1,j))+lst[i][j]
            return dp_lst[i][j]

ans_lst=[]
#for i in range(n):
for j in range(n):
    k=dp(n-1,j)
    ans_lst.append(k)

print(max(ans_lst))
