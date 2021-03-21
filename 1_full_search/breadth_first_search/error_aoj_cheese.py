"""
problem URL: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0558

Time:16:00-17:38

ERROR: visitedの更新の仕方に間違いがある.

copyの方法をdeepcopyにしたことで解決した.
しかし,この方法では分岐が多くなるため,かなり時間がかかるため
アルゴリズムとしてOUT
"""
import copy

h,w,n=map(int,input().split())
city=[list(input()) for _ in range(h)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

for y in range(h):
    for x in range(w):
        if city[y][x]=='S':
            sx,sy=x,y
            city[y][x]='.'
            break

lst=[]
visited=[[False for _ in range(h)] for _ in range(w)]

def bfs(x,y,hp,step):
    """
    現在地(x,y)から体力hpのネズミが探索を始める.
    食べ終わった場所の工場は.に変換する
    また,食べれるのなら食べた方が早いため,食べることにする.
    nを食べ終わったら終わり.==(hp==n+1)
    visitedも保管して,hpに変更があった場合初期化を加える.
    """
    global visited
    global lst
    if (x<0 or w<=x) or (y<0 or h<=y):
        return 0
    if visited[x][y]:
        return 0
    
    visited[x][y]=True

    if city[y][x]=='X':
        return 0
    elif city[y][x]=='.':
        tmp_visited=copy.deepcopy(visited)
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            bfs(nx,ny,hp,step+1)
            visited=copy.deepcopy(tmp_visited)
        return 0
    else:
        if int(city[y][x])<=hp:
            if int(city[y][x])==n:
                lst.append(step)
                return 0
            tmp_city=city[y][x]
            tmp_visited=copy.deepcopy(visited)
            city[y][x]='.'
            visited=[[False for _ in range(h)] for _ in range(w)]
            visited[x][y]=True
            tmptmpvisited=copy.deepcopy(visited)
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                bfs(nx,ny,hp+1,step+1)
                visited=copy.deepcopy(tmptmpvisited)
            city[y][x]=tmp_city
            visited=copy.deepcopy(tmp_visited)
            return 0
        else:
            tmp_visited=copy.deepcopy(visited)
            for i in range(4):
                nnx,nny=x+dx[i],y+dy[i]
                bfs(nnx,nny,hp,step+1)
                visited=copy.deepcopy(tmp_visited)
            return 0

bfs(sx,sy,1,0)

print(min(lst))
