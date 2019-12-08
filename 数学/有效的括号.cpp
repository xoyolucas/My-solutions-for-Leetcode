#include <stack>
#include <string>
#include <map>
using namespace std;

class Solution{
public:
    bool isValid(string s){
        stack<char> symbol_stack;
        map<char,char> symbol_map;
        symbol_map['('] = ')';
        symbol_map['{'] = '}';
        symbol_map['['] = ']';
        for (int i = 0; i < s.size(); ++i){
            if (s[i] == '(' || s[i] == '{' || s[i] == '['){
                symbol_stack.push(s[i]);
            }
            else if (s[i] == ')' || s[i] == '}' || s[i] == ']'){
                if (symbol_stack.empty() || symbol_map[symbol_stack.top()] != s[i]){
                    return false;
                }
                symbol_stack.pop();
            }
        }
        return symbol_stack.empty();
    }
};