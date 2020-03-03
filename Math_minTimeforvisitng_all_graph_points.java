/*
On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.
*/

class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int ans=0;

        for(int i=0;i<points.length-1;i++){

            int[] a = new int[2];
            int[] b = new int[2];
            a= points[i];
            b= points[i+1];

            int xdiff = Math.abs(a[0]-b[0]);
            int ydiff = Math.abs(a[1]-b[1]);

            ans = ans + Math.abs(xdiff-ydiff) + Math.min(xdiff,ydiff);

        }

        return ans;
}
}