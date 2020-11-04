/*
https://leetcode.com/problems/uncrossed-lines/

We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.


*/

class Solution {
    int ans = 0;

    public int maxUncrossedLines(int[] A, int[] B) {

       		int n = A.length;
		int m = B.length;
        int[][] dp = new int[n+1][m+1];
        for(int i = 1; i<n+1; i++)
            for(int j = 1; j<m+1; j++){
                 if(A[i-1] == B[j-1])
                    dp[i][j] = dp[i-1][j-1] + 1;
                else
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);

            }
            return dp[n][m];
			}


}