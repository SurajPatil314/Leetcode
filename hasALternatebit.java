/*
https://leetcode.com/problems/binary-number-with-alternating-bits/

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always
 have different values.
*/

class Solution {
    public boolean hasAlternatingBits(int n) {
        if(n<3) return true;
        String s = Integer.toBinaryString(n);
        for (int i = 1; i <s.length(); i++) {
            if(s.charAt(i-1) == s.charAt(i)) return false;
		}
        return true;

    }
}