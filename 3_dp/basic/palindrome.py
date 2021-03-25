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
例えばaXが回文になったとすると,Xの右端にはaがあることがわかる.
そのため,Xの右端からaをとっても回文となる.
つまり,aに関して追加するか削除するかのうちコストの少ないもののみを
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
    0<=i<=length-1, 0<=j<=length

    dp[i][i]=dp[i][i+1]=0
    dp[i-1][j]=min(dp[i-1][j],dp[i][j]+mydic[name[i-1]])
    dp[i][j+1]=min(dp[i][j+1],dp[i][j]+mydic[name[j]])
    dp[i-1][j+1]=dp[i][j]  (if name[i-1]==name[j])
                           ( cost(aXa)=cost(X) )
"""
for i in range(length):
    dp[i][i]=0
    dp[i][i+1]=0

for i in range(length):
    for j in range(i,length+1):
        if i>0:
            dp[i-1][j]=min(dp[i-1][j],dp[i][j]+mydic[name[i-1]])
        if j<length:
            dp[i][j+1]=min(dp[i][j+1],dp[i][j]+mydic[name[j]])
        if i>0 and j< length and name[i-1]==name[j]:
            dp[i-1][j+1]=dp[i][j]

print(dp[0][length])
print(dp)