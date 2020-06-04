/*
https://leetcode.com/problems/consecutive-characters/

Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

*/

class Solution {
    public int maxPower(String s) {

        if(s.length() <=1){return s.length();}


        char temp = s.charAt(0);
        int tempans = 1;
        int ans = 1;
        for(int i = 1; i<s.length(); i++){

            if(s.charAt(i) == temp){
                tempans++;
                if(tempans>ans){
                    ans = tempans;
                }
            }
            else{

                temp = s.charAt(i);
                tempans = 1;
            }

        }

        return ans;

    }
}