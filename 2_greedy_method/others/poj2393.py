"""
Problem URL: http://poj.org/problem?id=2393

Time: 14:49-15:20

苦戦した理由: 変数設定をもっと読みやすいものにすればよかった
料金: fee_storage,cent等
"""
n,s=map(int,input().split())

c,y=[],[]
for i in range(n):
    ci,yi=map(int,input().split())
    c.append(ci)
    y.append(yi)

ans=0
storage=0

for week in range(n):
    k=0
    if week==0:
        k=y[week]*c[week]
        cheap=c[week]
        cheap_week=week
    else:
        if(s*(week-cheap_week)+cheap<c[week]):
            #今までで最も安いタイミングで作るかどうかを検討する
            k=y[week]*cheap
            storage+=y[week]
        else:
            #そうでなかった場合,安いタイミングが変わるためそれを更新する
            cheap=c[week]
            cheap_week=week
            storage=0
            k=y[week]*c[week]
    k+=storage*(week-cheap_week)*s
    ans+=k
print(ans)
        
