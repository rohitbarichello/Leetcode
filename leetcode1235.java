class Solution {
    
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        // data structure to organize our jobs, sorted by start time
        int[][] jobs = new int[startTime.length][3];
        for (int i = 0; i < startTime.length; i++) {
            jobs[i] = new int[]{endTime[i], startTime[i], profit[i]};
        }
        Arrays.sort(jobs, (a, b) -> a[0] - b[0]);
        
        // our DP array containing max profit as value and index as index corresponding to end time
        int[] dp = new int[jobs.length];
        
        // set first element of array as profit of first job
        dp[0] = jobs[0][2];
        
        // iterate through jobs and decide which ones to schedule
        for (int cur = 1; cur < jobs.length; cur++) {
            int prev = prevNonOverlapping(cur, jobs);
            int currentProfit = jobs[cur][2];
            int prevMaxProfit = (prev == -1 ? 0 : dp[prev]);
            
            dp[cur] = Math.max(currentProfit + prevMaxProfit, dp[cur - 1]);
        }
        
        return dp[dp.length - 1];
    }
    
    // returns index in jobs of prev job that doesn't overlap with the current one
    private int prevNonOverlapping(int cur, int[][] jobs) {
        for (int prev = cur - 1; prev >= 0; prev--) {
            int prevEnd = jobs[prev][0];
            int currentStart = jobs[cur][1];
            
            if (prevEnd <= currentStart) {
                return prev;   
            }
        }
        
        return -1;
    }
}