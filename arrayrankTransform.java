/*
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.

*/

class Solution {
    public int[] arrayRankTransform(int[] arr) {
        HashMap<Integer, Integer> numh = new HashMap<Integer, Integer>();
        int[] ans = new int[arr.length];

        for(int i = 0; i<arr.length; i++){
            ans[i]= arr[i];
        }


        Arrays.sort(arr);
        int i1 = 1;

        for(int i = 0; i<arr.length; i++){
            if(numh.containsKey(arr[i])){
                continue;
            }
            else{
                numh.put(arr[i],i1);
                i1++;
            }
        }

        for(int i = 0; i<ans.length; i++){

            int pa = numh.get(ans[i]);
            ans[i] = pa;
        }

        return ans;


    }
}