/*
https://leetcode.com/problems/simplified-fractions/

Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator is less-than-or-equal-to n. The fractions can be in any order.
*/


class Solution {
    public List<String> simplifiedFractions(int n) {

        ArrayList<String> ans = new ArrayList<String>();
        ArrayList<Float> ans1 = new ArrayList<Float>();

        for(int i=2; i <=n; i++){
            for(int j = 1 ; j<i; j++){

                if(!ans1.contains((float)j/i)){
                    String tempans = String.valueOf(j)+"/"+String.valueOf(i);
                ans.add(tempans);
                ans1.add((float) j/i);
                }

            }
        }

        return ans;
    }
}