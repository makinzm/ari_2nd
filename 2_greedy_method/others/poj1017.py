"""
Problem URL : http://poj.org/problem?id=1017

Time : 15:37-16:20

全列挙するしかなさそう.
全ての図形を考えて列挙する.
もう少しSの扱い方を工夫すれば短くなると思う.
"""
anslst=[]
while(True):
    lst=list(map(int,input().split()))
    if all([x==0 for x in lst]):
        break
    lst.reverse()

    ans=0
    for idx, quantity in enumerate(lst):
        idx=6-idx
        #print(idx,quantity)
        while(quantity>0):
            if idx==6:
                ans+=1
                quantity-=1
            elif idx==5:
                ans+=1
                lst[5]=max(0,lst[5]-(36-25))
                quantity-=1
            elif idx==4:
                ans+=1
                if lst[4]-5<=0:
                    lst[5]=max(0,lst[5]-(20-lst[4]*4))
                    lst[4]=0
                else:
                    lst[4]=lst[4]-5
                quantity-=1
            elif idx==3:
                ans+=1
                if quantity==4:
                    quantity=0
                elif quantity==3:
                    if lst[4]>0:
                        lst[4]-=1
                        lst[5]=max(0,lst[5]-5)
                    else:
                        lst[5]=max(0,lst[5]-9)
                    quantity=0
                elif quantity==2:
                    S=18
                    S-=4*(min(3,lst[4]))
                    lst[4]=max(0,lst[4]-3)
                    lst[5]=max(0,lst[5]-S)
                    quantity=0
                elif quantity==1:
                    S=27
                    S-=4*(min(5,lst[4]))
                    lst[4]=max(0,lst[4]-5)
                    lst[5]=max(0,lst[5]-S)
                    quantity=0
                else:
                    quantity-=4
            elif idx==2:
                ans+=1
                S=36-4*min(9,quantity)
                quantity=max(quantity-9,0)
                lst[5]=max(lst[5]-S,0)
            else:
                ans+=1
                quantity=max(0,quantity-36)
    anslst.append(ans)
[print(x) for x in anslst]