class Solution {
public:
    // Memoization
    int climbStairs_1(int n) {
        if (n == 1) {
            return 1;
        }
        
        vector<int> ways(n+1, 0);
        ways[1] = 1;
        ways[2] = 2;
        
        for (int i = 3; i<=n; i++) {
            ways[i] = ways[i-1] + ways[i-2];
        }
        
        return ways[n];
    }

    // Recursion. Bad because it takes too long. Lots of recalculation. Fails in leetcode
    int climbStairs_2(int n) {
        if (n == 1) {
            return 1;
        }
        else if (n == 2) {
            return 2;
        }
        else {
            return climbStairs(n - 2) + climbStairs(n - 1);
        }
    }

    // recursion and memoization, uses too much memory, fails in leetcode
    int climbStairs_3(int n) {
        unordered_map<int, int> ways = {};
        ways[1] = 1;
        ways[2] = 2;
        
        return recursion(ways, n);
    }
    
    int recursion(unordered_map<int, int> ways, int n) {
        if (ways.count(n)) {
            return ways[n];
        }
        
        return recursion(ways, n - 1) + recursion(ways, n - 2);
    }

    // memoization but with two variables instead of a map or vector. Better space complexity but can be slower
    int climbStairs_4(int n) {
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }
        
        int way_1 = 1;
        int way_2 = 2;
        int ways;
        
        for (int i = 3; i<=n; i++) {
            ways = way_1 + way_2;
            way_1 = way_2;
            way_2 = ways;
        }
        
        return ways;
    }
};