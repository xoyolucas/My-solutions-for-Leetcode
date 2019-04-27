#include <vector>
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> result;
        for(int i=1;i<=n;++i){
            int a=i%5,b=i%3;
            if(a==0&&b==0)
                result.push_back("FizzBuzz");
            else if(a==0)
                result.push_back("Buzz");
            else if(b==0)
                result.push_back("Fizz");
            else
                result.push_back(to_string(i));
        }
        return result;
    }
};