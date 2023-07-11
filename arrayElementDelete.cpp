#include<bits/stdc++.h>
using namespace std;


int main(){

    int arr[10],elm=10,n=5,found = 0;
    cout << "Enter Element : "<<endl;
    for(int i = 0 ;i<n; i++){
        cin >> arr[i];
    }

    for(int i = 0 ;i<n; i++){
        if(arr[i] == elm){
            for(int j = i; j < n; j++){
                arr[j] = arr[j + 1];
            }
            found++;
            n--;
        }
    }
    for(int i = 0 ;i<n; i++){
        cout << "Element after delete : " <<arr[i] << endl;
    }


}