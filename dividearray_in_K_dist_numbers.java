/*
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.
*/

class Solution {
    public boolean isPossibleDivide(int[] nums, int k) {

        HashMap<Integer, Integer> freMap = new HashMap<>();

        Arrays.sort(nums);


        for(int num : nums){
            freMap.put(num, freMap.getOrDefault(num, 0)+1);


            }


        for(int num : nums) {

            if (freMap.get(num) == 0) continue;

            for (int j = 0; j < k; j++) {
                if (freMap.getOrDefault(num + j, 0) <= 0) return false;
                freMap.put(num + j, freMap.get(num + j) - 1);
            }

        }

        return true;
    }
}