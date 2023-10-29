#include<iostream>
#include<bits/stdc++.h>
#include<algorithm>
using namespace std;

// int divide(int dividend, int divisor) {
//     if(dividend == INT_MIN && divisor == 1) return INT_MIN;
//     if(dividend == INT_MAX && divisor == 1) return INT_MAX;        
//     if(dividend == INT_MIN && divisor == -1) return INT_MAX;
//     if(dividend == INT_MAX && divisor == -1) return INT_MIN+1;

//     int divs = abs(divisor);
//     int divd = abs(dividend);

//     if(divd == divs) {
//         return (dividend < 0) == (divisor < 0) ? 1 : -1;
//     }
    
//     int ans = 0;
//     int start = 0;
//     int end = divd;
//     int mid = start + (end-start)/2;

//     while(start <= end){
//         if(abs(mid*divs-divd) <= 1){
//             ans = mid;
//             break;
//         }
//         else if(mid > divd/divs){
//             end = mid-1;
//         }
//         else{
//             ans = mid;
//             start = mid+1;
//         }
//         mid = start + (end-start)/2;
//     }

//     return (dividend < 0) == (divisor < 0) ? ans : -ans;
// }

// int main(){
//     cout << divide(2147483647, 3) << endl;
// }


class parent {
    public:
    char bloodGroup = 'A';

    void group(){
        cout << bloodGroup << endl;
    }
};

class child : private parent {
    public:
    void group(){
        bloodGroup = 'B';
        cout << bloodGroup << endl;
    }
};

int main(){
    // parent p;
    // // cout << "blood group is : " << p.bloodGroup << endl;
    // child c;
    // // c.group();
    // // cout << c.bloodGroup << endl;

    // int* a = new int[10];
    // delete[] a;  


    int **p;
    int nr=3, nc=3, r, c;

    p = new int*[nr];
    cout << "point of pointer is : " << p << endl;
    for(r=0; r<nr; r++){
        p[r] = new int[nc];
        cout << "point of an arr : " << p[r] << endl;
    }
    delete p;
}
