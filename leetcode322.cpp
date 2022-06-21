class Solution {
public:
    // uses an array. Faster
    int coinChange_array(vector<int>& coins, int n) {
        int dp[n + 1];
        dp[0] = 0;
        
        sort(begin(coins), end(coins));
        
        for (int i = 1; i <= n; i++) {
            dp[i] = INT_MAX;

            for (int c: coins) {
                if (i - c < 0) {
                    break;
                }
                
                if (dp[i - c] != INT_MAX) {
                    dp[i] = min(dp[i], 1 + dp[i - c]);
                }
            }
        }
        
        return dp[n] == INT_MAX ? -1 : dp[n];
    }

    // uses a vector, potentially easier to write the code 
    int coinChange_vector(vector<int>& coins, int n) {
        vector<int> ways(n + 1, INT_MAX);
        ways[0] = 0;
        
        sort(begin(coins), end(coins));
        
        for(int i = 1; i <= n; i++) {
            for(int coin: coins) {
                if(i - coin < 0) {
                    break;
                }
                
                if(ways[i - coin] != INT_MAX) {
                    ways[i] = min(ways[i], 1 + ways[i - coin]);
                }
            }
        }
        
        if(ways[n] == INT_MAX) {
            return -1;
        }
        else {
            return ways[n];
        }
    }
};


