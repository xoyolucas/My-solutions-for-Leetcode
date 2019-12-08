class Solution{
public:
    int hammingDistance(int x, int y){
        int result = 0;
        for (int i = x ^ y; i > 0; i = i >> 1){
            if (i & 1 == 1){
                result++;
            }
        }
        return result;
    }
};