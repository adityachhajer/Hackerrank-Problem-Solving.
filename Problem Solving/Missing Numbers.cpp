#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int frequency[100001];
    for(int i = 1; i <= 100000; i++) {
        frequency[i] = 0;
    }
    int n, m;
    cin>>n;
    
    for(int i = 0; i < n; i++) {
        int tmp;
        cin>>tmp;
        frequency[tmp]++;
    }
    cin>>m;
    for(int i = 0; i < m; i++) {
        int tmp;
        cin>>tmp;
        frequency[tmp]--;
    }
    for(int i = 1; i <= 10000; i++) {
        if(frequency[i] != 0) {
            cout<<i<<" ";
        }
    }
    return 0;
}

