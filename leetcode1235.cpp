struct Job {
    int start, end, profit;
};

bool compareJobs(Job job1, Job job2) {
    return job1.end < job2.end;
}

class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        int numJobs = startTime.size();
        
        // create data structure to organize jobs and sort it by end time
        Job jobs[numJobs];
        for(int i = 0; i < numJobs; i++) {
            jobs[i].end = endTime[i];
            jobs[i].start = startTime[i];
            jobs[i].profit = profit[i];
        }
        
        sort(jobs, jobs + numJobs, compareJobs);
        
        // dp map. Key corresponds to the job and value is the max profit at the end time of the job        
        unordered_map<int, int> dp = {};
        dp[0] = jobs[0].profit;

        for(int cur = 1; cur < numJobs; cur++) {
            int prevJob = prevNonOverlappingJob(cur, jobs);
            
            dp[cur] = max(jobs[cur].profit + (prevJob == -1 ? 0 : dp[prevJob]), dp[cur - 1]);
        }
        
        return dp[numJobs - 1];
    }
    
    int prevNonOverlappingJob(int cur, Job *jobs) {        
        for(int prev = cur - 1; prev >= 0; prev--) {            
            if(jobs[prev].end <= jobs[cur].start) {
                return prev;
            }
        }
        
        return -1;
    }
};