class Solution {
   public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        int n = profit.size();
        int dp[n];

        pair<int, pair<int, int>> newarr[n];

        for (int i = 0; i < n; i++) {
            newarr[i].first = endTime[i];
            newarr[i].second.first = startTime[i];
            newarr[i].second.second = profit[i];
        }

        sort(newarr, newarr + n);
        for (int i = 0; i < n; i++) {
            endTime[i] = newarr[i].first;
            startTime[i] = newarr[i].second.first;
            profit[i] = newarr[i].second.second;
        }

        dp[0] = profit[0];
        for (int i = 1; i < n; i++) {
            dp[i] = max(dp[i - 1], profit[i]);

            for (int j = i - 1; j >= 0; j--) {
                if (endTime[j] <= startTime[i]) {
                    dp[i] = max(dp[i], profit[i] + dp[j]);
                    break;
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans = max(dp[i], ans);
        }
        return ans;
    }
};