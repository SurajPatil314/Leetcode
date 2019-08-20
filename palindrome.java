class Solution {
    public boolean isPalindrome(String s) {
         if(s != null && !s.isEmpty())
         {
             String reverse ="";
             for(int i= s.length()-1; i>=0; i--)
             {
                 reverse= reverse + s.charAt(i);
             }
             System.out.println(reverse);
             if(s.equals(reverse))
                 return true;
             else
                 return false;
         }
        else
            return false;
        
        
    }
}