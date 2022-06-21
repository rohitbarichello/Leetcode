class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<double> ways(target + 1, 0);
        sort(begin(nums), end(nums));
        ways[0] = 1;
        
        for(int i = 1; i < target + 1; i++) {
            for(int j = 0; j < nums.size(); j++) {
                if(i - nums[j] >= 0) {
                    ways[i] += ways[i - nums[j]];
                }
                else {
                    break;
                }
            }
        }
        
        return ways[target];
    }
};