//Given an integer, return its base 7 string representation.
class Solution {
    public String convertToBase7(int num) {

        String ans = "";
        int neg = 0;
        if(num==0){
            return "0";
        }
        if(num<0){
            neg = 1;
            num=0-num;
        }
        while(num>0){
            ans = String.valueOf(num%7)+ans;
            num = num/7;
        }
        if(neg==1){
            return "-"+ans;
        }
        return ans;
    }
}