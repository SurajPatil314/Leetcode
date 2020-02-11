/*
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
*/
class Solution {
    public int climbStairs(int n) {

        int[] ans =new int[n+1];
        // num_ways(n) = num_ways(N-1) + num_ways(N-2)
        if(n==0 || n==1)
        {
            return 1;
        }
        else
        {
            ans[0]=1;
            ans[1]=1;
            for(int i=2; i<=n; i++)
            {
                ans[i]= ans[i-1]+ans[i-2];
            }
            return ans[n];
        }

    }
}