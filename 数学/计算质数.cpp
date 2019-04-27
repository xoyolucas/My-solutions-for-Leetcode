class Solution {
public:
    int countPrimes(int n) {
        bool* no_prime=new bool[n];
        for(int i=0;i<n;++i)
            no_prime[i]=false;
        
        
        int result=0;
        for(int i=2;i*i<n;i++){
            if(no_prime[i]==false){
                for(int j=i;i*j<n;j++){
                    no_prime[i*j]=true;
                }
            }
        }
        
        for(int i=2;i<n;i++){
            if(no_prime[i]==false)
                result++;
        }
        return result;
    }
};