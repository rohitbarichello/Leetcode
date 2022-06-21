class Solution {
   public:
    vector<int> DIR = {0, 1, 0, -1, 0};
    struct Cell {
        int i, j;
    };

    // BFS Solution
    vector<vector<int>> updateMatrix_BFS(vector<vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();
        queue<struct Cell> q;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 0) {
                    struct Cell cell = {i, j};
                    q.emplace(cell);
                }
                else {
                    mat[i][j] = -1;
                }
            }
        }

        while (!q.empty()) {
            int i = q.front().i;
            int j = q.front().j;
            q.pop();

            for (int x = 0; x < 4; ++x) {
                int ni = i + DIR[x];
                int nj = j + DIR[x + 1];
                
                if(ni >= 0 && ni < m && nj >= 0 && nj < n && mat[ni][nj] == -1) {
                    mat[ni][nj] = mat[i][j] + 1;
                
                    struct Cell newCell = {ni, nj};
                    q.emplace(newCell);
                }
            }
        }
        
        return mat;
    }
};