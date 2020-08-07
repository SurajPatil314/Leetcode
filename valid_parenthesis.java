/*
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.
*/
class Solution {
    public int minAddToMakeValid(String S) {
        int ans = 0;
        int finalans = 0;

        for(int i = 0 ; i<S.length(); i ++){

            if(S.charAt(i)=='('){
                if(ans<0){
                    finalans = finalans+Math.abs(ans);
                    ans = 1;
                }
                else{
                   ans++;
                }

            }
            else{
                    ans--;

            }
        }
        finalans = finalans+Math.abs(ans);
        return finalans;

    }
}