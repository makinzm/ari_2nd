#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>

// g++
int main(){
    int c,l;
    std::cin >> c >>l;
    std::vector<std::pair<int, int> > cows(2500);
    for (int i = 0; i < c; i++) {
        int a,b;
        std::cin >> a>> b;
        cows[i]=std::make_pair(a,b);
    }
    /**
     * static std::pair<int,int> lotion[2500];
        for (int i = 0; i < l; i++) {
        std::cin >> lotion[i].first >> lotion[i].second;
        }
     * 
    **/ 
    std::vector<std::pair<int, int> > lotion(2500);
    for (int i = 0; i < l; i++) {
        int a,b;
        std::cin >> a>> b;
        lotion[i]=std::make_pair(a,b);
    }
    int used_cows[2500];
    memset(used_cows,0,sizeof(used_cows));

    sort(cows.begin(), cows.begin()+c);
    sort(lotion.begin(), lotion.begin()+l);

    int ans=0;

    for (int i=0; i<c; i++){
        for(int j=0; j<l; j++){
            if ((cows[i].first <= lotion[j].first) && (cows[i].second >= lotion[j].first) && (lotion[j].second>0) && (used_cows[i]==0)){
                ans+=1;
                lotion[j].second -=1;
                used_cows[i]=1;
                break;
            }
        }
    }

    std::cout << ans<< '\n';


    return 0;
}