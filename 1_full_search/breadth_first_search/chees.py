"""
Problem URL:https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0558

参考 URL: https://tsutaj.hatenablog.com/entry/2017/12/23/000000
"""
import queue

h,w,n=map(int,input().split())
city=[list(input()) for _ in range(h)]

def search_cheese(m):
    """
    Cheeseの場所を探す(m=0とすると巣を探す)
    """
    global city
    for y in range(h):
        for x in range(w):
            if city[y][x]=='.' or city[y][x]=='X':
                pass
            elif (m==0 and city[y][x]=='S') or (int(city[y][x])==m):
                sx,sy=x,y
                city[y][x]='.'
                break
    return (sx,sy)

INF=10**7
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(sx,sy,gx,gy):
    """
    (sx,sy)から(gx,gy)への最短経路を返す関数
    """
    dist = [[INF for _ in range(h)] for _ in range(w)]
    dist[sx][sy]=0

    q=queue.Queue()
    q.put((sx,sy))
    while not q.empty():
        x,y=q.get()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if (nx<0 or w<=nx) or (ny<0 or h<=ny):
                continue
            if city[ny][nx]=='X':
                continue
            else:
                if dist[nx][ny]>dist[x][y]+1:
                    dist[nx][ny]=dist[x][y]+1
                    q.put((nx,ny))
    return dist[gx][gy]

cheese_x=[]
cheese_y=[]
for i in range(n+1):
    x,y=search_cheese(i)
    cheese_x.append(x)
    cheese_y.append(y)

ans=0
for i in range(n):
    ans+=bfs(cheese_x[i],cheese_y[i],cheese_x[i+1],cheese_y[i+1])
print(ans)