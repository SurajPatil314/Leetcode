/*
https://leetcode.com/problems/rotting-oranges/


In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.


*/

class Solution {
    public int orangesRotting(int[][] grid) {
       ArrayList<ArrayList<Integer>> rotten = new ArrayList<ArrayList<Integer>>();
       ArrayList<ArrayList<Integer>> visited = new ArrayList<ArrayList<Integer>>();
        int fresh = 0;
        int ans = 0;
        for (int row = 0; row < grid.length; row++)
        {
            for (int col = 0; col < grid[row].length; col++)
            {
                if(grid[row][col] == 2){
                    ArrayList<Integer> temp = new ArrayList<>();
                    temp.add(row);
                    temp.add(col);
                    rotten.add(temp);
                    visited.add(temp);
                }
                if(grid[row][col]==1){
                    fresh++;
                }
            }

        }
        if(fresh == 0){return 0;}
        if(rotten.size() == 0){return -1;}

        ArrayList<ArrayList<Integer>> rotten1 = new ArrayList<ArrayList<Integer>>();

        while(rotten1.size()>0 || rotten.size()>0)
        {
            System.out.println(rotten);
            while(rotten.size()>0){
                ArrayList<Integer> qw = rotten.remove(0);

                if(qw.get(0)>0){
                    ArrayList<Integer> qw1 = new ArrayList<>();
                    qw1.add((qw.get(0)-1));
                    qw1.add(qw.get(1));
                    if(!(visited.contains(qw1))){
                        if(grid[qw.get(0)-1][qw.get(1)] == 2) {
                            visited.add(qw1);
                            rotten1.add(qw1);
                        }
                        if(grid[qw.get(0)-1][qw.get(1)] == 1) {
                            visited.add(qw1);
                            grid[qw.get(0)-1][qw.get(1)]  = 2;
                            rotten1.add(qw1);
                            fresh--;
                        }
                    }
                }
                if(qw.get(0)<(grid.length-1)){
                    ArrayList<Integer> qw1 = new ArrayList<>();
                    qw1.add((qw.get(0)+1));
                    qw1.add(qw.get(1));

                    if(!visited.contains(qw1)){
                        if(grid[qw.get(0)+1][qw.get(1)] == 2) {
                            visited.add(qw1);
                            rotten1.add(qw1);
                        }
                        if(grid[qw.get(0)+1][qw.get(1)] == 1) {
                            visited.add(qw1);
                            grid[qw.get(0)+1][qw.get(1)]  = 2;
                            rotten1.add(qw1);
                            fresh--;
                        }
                    }
                }
                if(qw.get(1)>0){
                    ArrayList<Integer> qw1 = new ArrayList<>();
                    qw1.add(qw.get(0));
                    qw1.add(qw.get(1)-1);

                    if(!visited.contains(qw1)){
                        if(grid[qw.get(0)][qw.get(1)-1] == 2) {
                            visited.add(qw1);
                            rotten1.add(qw1);
                        }
                        if(grid[qw.get(0)][qw.get(1)-1] == 1) {
                            visited.add(qw1);
                            grid[qw.get(0)][qw.get(1)-1]  = 2;
                            rotten1.add(qw1);
                            fresh--;
                        }
                    }
                }

                if(qw.get(1)<grid[qw.get(0)].length-1){
                    ArrayList<Integer> qw1 = new ArrayList<>();
                    qw1.add(qw.get(0));
                    qw1.add(qw.get(1)+1);

                    if(!visited.contains(qw1)){
                        if(grid[qw.get(0)][qw.get(1)+1] == 2) {
                            visited.add(qw1);
                            rotten1.add(qw1);
                        }
                        if(grid[qw.get(0)][qw.get(1)+1] == 1) {
                            visited.add(qw1);
                            grid[qw.get(0)][qw.get(1)+1]  = 2;
                            rotten1.add(qw1);
                            fresh--;
                        }
                    }

                    }
            }
            ans++;
            if(fresh == 0)
            {
                return ans;
            }

            while(rotten1.size()>0){
                ArrayList<Integer> qw = rotten1.remove(0);

                if(qw.get(0)>0){
                    ArrayList<Integer> qw1 = new ArrayList<>();
                    qw1.add((qw.get(0)-1));
                    qw1.add(qw.get(1));
                    if(!(visited.contains(qw1))){
                        if(grid[qw.get(0)-1][qw.get(1)] == 2) {
                            visited.add(qw1);
                            rotten.add(qw1);
                        }
                        if(grid[qw.get(0)-1][qw.get(1)] == 1) {
                            visited.add(qw1);
                            grid[qw.get(0)-1][qw.get(1)]  = 2;
                            rotten.add(qw1);
                            fresh--;
                        }
                    }
                }
                if(qw.get(0)<(grid.length-1)){
                    ArrayList<Integer> qw1 = new ArrayList<>();
                    qw1.add((qw.get(0)+1));
                    qw1.add(qw.get(1));

                    if(!visited.contains(qw1)){
                        if(grid[qw.get(0)+1][qw.get(1)] == 2) {
                            visited.add(qw1);
                            rotten.add(qw1);
                        }
                        if(grid[qw.get(0)+1][qw.get(1)] == 1) {
                            visited.add(qw1);
                            grid[qw.get(0)+1][qw.get(1)]  = 2;
                            rotten.add(qw1);
                            fresh--;
                        }
                    }
                }
                if(qw.get(1)>0){
                    ArrayList<Integer> qw1 = new ArrayList<>();
                    qw1.add(qw.get(0));
                    qw1.add(qw.get(1)-1);

                    if(!visited.contains(qw1)){
                        if(grid[qw.get(0)][qw.get(1)-1] == 2) {
                            visited.add(qw1);
                            rotten.add(qw1);
                        }
                        if(grid[qw.get(0)][qw.get(1)-1] == 1) {
                            visited.add(qw1);
                            grid[qw.get(0)][qw.get(1)-1]  = 2;
                            rotten.add(qw1);
                            fresh--;
                        }
                    }
                }

                if(qw.get(1)<grid[qw.get(0)].length-1){
                    ArrayList<Integer> qw1 = new ArrayList<>();
                    qw1.add(qw.get(0));
                    qw1.add(qw.get(1)+1);

                    if(!visited.contains(qw1)){
                        if(grid[qw.get(0)][qw.get(1)+1] == 2) {
                            visited.add(qw1);
                            rotten.add(qw1);
                        }
                        if(grid[qw.get(0)][qw.get(1)+1] == 1) {
                            visited.add(qw1);
                            grid[qw.get(0)][qw.get(1)+1]  = 2;
                            rotten.add(qw1);
                            fresh--;
                        }
                    }

                    }
            }
            ans++;
            if(fresh == 0)
            {
                return ans;
            }


        }


        return -1;

    }
}