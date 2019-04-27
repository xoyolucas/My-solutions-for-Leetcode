#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

void rotate(vector<vector<int>>& matrix) {
    int n=matrix.size();
    
    for(size_t i = 0; i < n/2; i++){
        for(size_t j = i; j < n-i-1; j++){
            int tmp=matrix[i][j];
            matrix[i][j]=matrix[n-1-j][i];
            matrix[n-1-j][i]=matrix[n-1-i][n-1-j];
            matrix[n-1-i][n-1-j]=matrix[j][n-1-i];
            matrix[j][n-1-i]=tmp;
        }
    }
}

int main(int argc, char const *argv[]){
    vector<vector<int> > matrix(3);
    for(size_t i = 0; i < 3; i++){
        matrix[i].resize(3);
    }
    for(size_t i = 0; i < 3 ; i++){
        for(size_t j = 0; j < 3; j++){
            matrix[i][j]=(i+1)*(j+1);   
        }
    }
    for(size_t i = 0; i < 3 ; i++){
        for(size_t j = 0; j < 3; j++){
            cout<<matrix[i][j];   
        }
        cout<<endl;
    }
    rotate(matrix);
    cout<<endl;
    for(size_t i = 0; i < 3 ; i++){
        for(size_t j = 0; j < 3; j++){
            cout<<matrix[i][j];   
        }
        cout<<endl;
    }
    return 0;
}
