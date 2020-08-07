/*
https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
*/
class Solution {
    public int oddCells(int n, int m, int[][] indices) {

        HashMap<Integer, Integer> rowm = new HashMap<Integer, Integer>();
        HashMap<Integer, Integer> colm = new HashMap<Integer, Integer>();

        int ans=0;

        for(int i = 0; i< indices.length; i++){

            if(rowm.containsKey(indices[i][0])){
                rowm.put(indices[i][0],rowm.get(indices[i][0])+1);
            }
            else{
                rowm.put(indices[i][0],1);
            }

            if(colm.containsKey(indices[i][1])){
                colm.put(indices[i][1],colm.get(indices[i][1])+1);
            }
            else{
                colm.put(indices[i][1],1);
            }

        }

        for(int i = 0 ; i<n; i++){
            for(int j=0; j<m;j++ ){
                int tempans = 0;
                if(rowm.containsKey(i)){
                    tempans = tempans+rowm.get(i);
                }

                if(colm.containsKey(j)){
                    tempans = tempans+colm.get(j);
                }

                if(tempans%2==1){
                    ans = ans+1;
                }

            }
        }
        return ans;
    }
}