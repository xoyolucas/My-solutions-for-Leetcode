#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

bool isValidSudoku(vector<vector<char>>& board) {
    unordered_set<char> row[10];
    unordered_set<char> column[10];
    unordered_set<char> block[3][3];
    
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[i].size(); j++) {                
            char c = board[i][j];
            
            if (c == '.') {
                continue;
            }
            
            if (row[i].count(c) > 0) {
                return false;
            }
            if (column[j].count(c) > 0) {
                return false;
            }
            if (block[i/3][j/3].count(c) > 0) {
                return false;
            }
            
            row[i].insert(c);
            column[j].insert(c);
            block[i/3][j/3].insert(c);
        }
    }
    return true;
}

