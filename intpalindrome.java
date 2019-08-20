class Solution {
    public boolean isPalindrome(int x) {
        if(x<0)
            return false;
        else
        {
                String sp = Integer.toString(x);
                String sp1 = new StringBuffer(sp).reverse().toString();
            System.out.println("sp::"+sp);
            System.out.println("sp1::"+sp1);
                if(sp.equals(sp1))
                    return true;
                else
                    return false;
                
        }
        
    }
}