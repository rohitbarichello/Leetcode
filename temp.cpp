class Solution {  // 48 ms, faster than 99.64%
   public:
    vector<vector<int>> updateMatrix(vector<vector<int>> &mat) {
        int m = mat.size();
        int n = mat[0].size();
        int INF = m + n;  // The distance of cells is up to (M+N)

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (mat[r][c] != 0) {
                    int top = INF;
                    int left = INF;

                    if (r - 1 >= 0) {
                        top = mat[r - 1][c];
                    }
                    if (c - 1 >= 0) {
                        left = mat[r][c - 1];
                    }

                    mat[r][c] = min(top, left) + 1;
                }
            }
        }

        for (int r = m - 1; r >= 0; r--) {
            for (int c = n - 1; c >= 0; c--) {
                if (mat[r][c] != 0) {
                    int bottom = INF;
                    int right = INF;

                    if (r + 1 < m) {
                        bottom = mat[r + 1][c];
                    }
                    if (c + 1 < n) {
                        right = mat[r][c + 1];
                    }

                    mat[r][c] = min(mat[r][c], min(bottom, right) + 1);
                }
            }
        }

        return mat;
    }
};