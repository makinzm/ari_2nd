"""
Problem URL : http://poj.org/problem?id=1017

Time : 15:37-16:08

全列挙するしかなさそう.(予定があるため,途中まで)
"""
lst=list(map(int,input().split()))
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
            if quantity<=4:
                quantity=0
                
            


