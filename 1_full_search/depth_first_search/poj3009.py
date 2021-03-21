"""
problem URL: http://poj.org/problem?id=3009

Time: 14:38-15:28

苦戦理由: スタートの制約条件を入れ忘れ,flag導入までに時間がかかったこと.
"""

lst=[]
while(True):
    w,h=map(int,input().split())
    if(w==0 and h==0):
        break
    boad=[list(map(int,input().split())) for _ in range(h)]

    candidates=[]

    for x in range(w):
        for y in range(h):
            if boad[y][x]==2:
                sx,sy=x,y

    def dfs(x,y,direction,step,flag):
        """
        現在地(x,y)から一方向directionの方向へ進むことを考える.
        direction:右なら0,左なら1,下なら2,上なら3とする.
        stepが10以下であるため,10を越さないようにする.
        スタート条件に制限があるため,flagが0の場合スタートできるか考える.
        """
        if step>10:
            return 0
        
        if direction==0:
            nx,ny=x+1,y
        elif direction==1:
            nx,ny=x-1,y
        elif direction==2:
            nx,ny=x,y+1
        else:
            nx,ny=x,y-1
        
        if (nx<0 or w<=nx) or (ny<0 or h<=ny):
            return 0
        
        global boad
        if flag==0:
            if boad[ny][nx]==1:
                return 0
            else:
                flag=1
        
        if boad[ny][nx]==0 or boad[ny][nx]==2:
            dfs(nx,ny,direction,step,1)
            return 0
        elif boad[ny][nx]==1:
            boad[ny][nx]=0
            dfs(x,y,0,step+1,0)
            dfs(x,y,1,step+1,0)
            dfs(x,y,2,step+1,0)
            dfs(x,y,3,step+1,0)
            boad[ny][nx]=1
            return 0
        if boad[ny][nx]==3:
            global candidates
            candidates.append(step)
            return 0

    dfs(sx,sy,0,1,0)
    dfs(sx,sy,1,1,0)
    dfs(sx,sy,2,1,0)
    dfs(sx,sy,3,1,0)

    if len(candidates)==0:
        lst.append(-1)
    else:
        lst.append(min(candidates))

[print(i) for i in lst]