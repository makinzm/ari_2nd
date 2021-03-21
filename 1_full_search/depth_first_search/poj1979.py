"""
problem URL: http://poj.org/problem?id=1979

Time: 13:56-14:34

苦戦した理由:見慣れないinput方式,終了条件の漏れ
"""

lst=[]
while(True):
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    # width(x) height(y)

    tiles=[input() for _ in range(h)]
    visited=[[False for _ in range(h+1)]for _ in range(w+1)]

    for y in range(h):
        for x in range(w):
            if tiles[y][x]=='@':
                sx,sy=x,y
                break
    ans=1

    def dfs(x,y):
        """
        現在地(x,y)からいける場所を上下左右で探索する.
        loop構造として終了条件に注意する
        """
        global visited
        if (x<0 or w<=x) or (y<0 or h<=y):
            return 0
        if tiles[y][x]=='#':
            return 0
        if visited[x][y]:
            return 0
        else:
            visited[x][y]=True
            if tiles[y][x]=='.':
                global ans
                ans+=1
            return dfs(x+1,y)+dfs(x-1,y)+dfs(x,y+1)+dfs(x,y-1)
    dfs(sx,sy)
    lst.append(ans)

for i in lst:
    print(i)