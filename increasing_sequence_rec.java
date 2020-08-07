/*
https://leetcode.com/problems/increasing-subsequences/


Given an integer array, your task is to find all the different possible increasing subsequences of the given array,
 and the length of an increasing subsequence should be at least 2.
*/
class Solution {
    Set<List<Integer>> ans = new HashSet<>();
    public List<List<Integer>> findSubsequences(int[] nums) {

        List<Integer> temp2 = new ArrayList<Integer>();
        rec(nums,0,temp2);
        return new ArrayList<>(ans);

    }

    public void rec(int[] nums,int pos,List<Integer> temp2 ){

        if(pos>=nums.length){
            if(temp2.size()>1){
                    ans.add(List.copyOf(temp2));
            }
            return;
        }
        else{
            if(temp2.isEmpty()|| temp2.get(temp2.size()-1)<=nums[pos] ){

                temp2.add(nums[pos]);
                rec(nums,pos+1,temp2);
                temp2.remove(temp2.size() - 1);
            }

            rec(nums,pos+1,temp2);
        }

    }
}