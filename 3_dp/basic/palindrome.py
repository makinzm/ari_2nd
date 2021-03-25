"""
Problem URL: http://poj.org/problem?id=3280

Hint URL: https://tsutaj.hatenablog.com/entry/2018/03/04/012113
        https://eagletmt.github.io/contests/blog/poj-3280/

palindrome: ˈpalɪndrəʊm/ a word, phrase, or sequence 
    that reads the same backwards as forwards, e.g. madam or nurses run.

mischievous: /ˈmɪstʃɪvəs/
    causing or showing a fondness for causing trouble in a playful way.

spoof: /spuːf/
    a humorous imitation of something, typically a film or a particular genre of film,
    in which its characteristic features are exaggerated for comic effect.


Time: 14:51-15:15,18:02-18:20 -> give up

O(m*m)で 今回m=2000のため間に合う.
"""
n,m=map(int,input().split())
name=list(input())
mydic={}
for i in range(n):
    alpha,add,delete=input().split()
    mydic[alpha]=(min(list(map(int,(add,delete)))))

"""
ある文字列Xの左端に文字aを付け足すことを考える.
そしてaXが回文になったとすると,Xの右端にはaがあることがわかる.
そのため,Xの右端からaをとっても回文となる(右端も同様).

また,YXのYとXの間に文字aを付け足すことを考える.
YaXが回文になったとすると,YXの付け足したところの対称位置にも
aがあるため,YXの対称箇所からaをとっても回文となる.

ただし,YとXが同じ長さであった場合はYXは既に回文であるため,
コストの変動はなくYXを作るコストが最小のコストとなる.

これをどの段階においても同様に考えることができるため,
aに関して追加するか削除するかのうちコストの少ないもののみを
使用しても回文を作成することができる.
"""

def is_palindrome(sentence):
    """
    return whether a sentence is palindrome.
    """
    for i in range(len(sentence)//2):
        if sentence[i]!= sentence[-i-1]:
            return False
    return True

length=len(name)

INF=(length+10)*(10**5)

dp=[[INF for _ in range(length+1)]for _ in range(length)]

"""
    dp[i][j]: iからj文字目まで[i,j)を回文にするため必要な経費を返す.
    0<=i<=length-1, 0<=j<=length, 0<=j-i<=length

    dp[i][i]=dp[i][i+1]=0
    dp[i-1][j]=min(dp[i-1][j],dp[i][j]+mydic[name[i-1]])
    dp[i][j+1]=min(dp[i][j+1],dp[i][j]+mydic[name[j]])
    dp[i-1][j+1]=dp[i][j]  (if name[i-1]==name[j])
                           ( cost(aXa)=cost(X) )
"""

updated=[[False for _ in range(length+1)]for _ in range(length)]

for i in range(length):
    dp[i][i]=0
    dp[i][i+1]=0
    updated[i][i]=True
    updated[i][i+1]=True


##　文字列の短いものから更新するようにすることで,問題なく更新できる,　
## というのも...
for len_name in range(length+1):
    for i in range(length):
        j=i+len_name
        if i>0 and j<=length:
            ## ここにおいてdp[i-1][j]を見るとき j-(i-1)>j-iのためdp[i][j]は既に更新済みのため
            dp[i-1][j]=min(dp[i-1][j],dp[i][j]+mydic[name[i-1]])
            updated[i-1][j]=True
        if i>=0 and j<length:
            ## ここにおいてdp[i][j+1]を見るとき j+1-i>j-iのためdp[i][j]は既に更新済みのため
            dp[i][j+1]=min(dp[i][j+1],dp[i][j]+mydic[name[j]])
            updated[i][j+1]=True
        if i>0 and j< length and name[i-1]==name[j]:
            ## ここにおいてdp[i-1][j+1]を見るとき j+1-(i-1)>j-iのためdp[i][j]は既に更新済みのため
            dp[i-1][j+1]=dp[i][j]
            updated[i-1][j+1]=True

# print(dp[0][m])
# しかし,このコードの場合,毎回異なった更新(i-1,j),(i,j+1),(i-1,j+1)の更新を行っているため,個人的に本当に探索し切れたかわかりづらい.
# そのため,dp(s,length)としてスタートの文字がs文字目でlengthの長さだった際の文字列を回文にすることを考えると.
"""
dp[i][0]=dp[i][1]=0
dp[i][x]=min(dp[i][x],dp[i+1][x-1]+mydic[name[i-1]])
dp[i][x]=min(dp[i][x],dp[i][x-1]+mydic[name[i+x-1]])
dp[i][x]=dp[i+1][x-2] if name[i-1]==name[i+x-1]

とした方が安心する
"""
dp_new=[[INF for _ in range(m+1)]for _ in range(m+1)]

for i in range(1,m+1):
    dp_new[i][0]=0
    dp_new[i][1]=0

for x in range(2,m+1):
    for s in range(1,m+1):
        if s+x-2<m:
            dp_new[s][x]=min(dp_new[s][x],dp_new[s][x-1]+mydic[name[s+x-2]])
        if s+1<m+1 and s-2<m:
            dp_new[s][x]=min(dp_new[s][x],dp_new[s+1][x-1]+mydic[name[s-1]])
        if s+x-2<m and s-1<m and s+1<m+1 and name[s-1]==name[s+x-2]:
            dp_new[s][x]=min(dp_new[s][x],dp_new[s+1][x-2])
            # 今までここで dp[s][x]>=dp[s+1][x-2]は自明としてきたと思うが,
            # 根拠が今わからないため,一応minを挟んでおく.
print(dp_new[1][m])