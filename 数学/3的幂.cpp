#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        int len=s.size();
        vector<int>convert;
        for(int i=0;i<len;i++){
            if (s[i]=='I') convert.push_back(1);
            else if (s[i]=='V') convert.push_back(5);
            else if (s[i]=='X') convert.push_back(10);
            else if (s[i]=='L') convert.push_back(50);
            else if (s[i]=='C') convert.push_back(100);
            else if (s[i]=='D') convert.push_back(500);
            else if (s[i]=='M') convert.push_back(1000);
        }
        int sum=convert[len-1];
        for (int j=len-1;j>0;j--){
            if (convert[j-1]<convert[j]) sum=sum-convert[j-1];
            else sum=sum+convert[j-1];    
        }
        return sum;
    }
};