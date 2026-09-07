class Solution {
public:

    bool searchRow(vector<vector<int>>& matrix, int target, int row) {
        int n = matrix[0].size();
        int start = 0;
        int end = n - 1;

        while (start <= end) {
            int mid = (start + end) / 2;

            if (target == matrix[row][mid]) {
                return true;
            }
            else if (target > matrix[row][mid]) {
                start = mid + 1;
            }
            else {
                end = mid - 1;
            }
        }

        return false;
    }

    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();

        int start = 0;
        int end = m - 1;

        while (start <= end) {
            int mid = (start + end) / 2;

            if (target >= matrix[mid][0] && target <= matrix[mid][n - 1]) {
                return searchRow(matrix, target, mid);
            }
            else if (target > matrix[mid][n - 1]) {
                start = mid + 1;
            }
            else {
                end = mid - 1;
            }
        }

        return false;
    }
};