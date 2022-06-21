class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        
        // the value longestSubSeqAtIndex[x] is the longest subsequence at nums[x]
        vector<int> longestSubSeqAtIndex(n, 1);
        
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < i; j++) {
                if(nums[i] > nums[j] && longestSubSeqAtIndex[i] <= longestSubSeqAtIndex[j]) {
                    longestSubSeqAtIndex[i] = longestSubSeqAtIndex[j] + 1;
                }
            }
        }
        
        return *max_element(longestSubSeqAtIndex.begin(), longestSubSeqAtIndex.end());
    }
};