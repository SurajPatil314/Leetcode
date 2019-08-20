class Solution {
    public int reverse(int x) {
        if(x!=0)
        {
            if(x>0)
            {
                String sp = Integer.toString(x);
                String sp1 = new StringBuffer(sp).reverse().toString();
                //String sp1 = sp.reverse();
                int sp2 = Integer.parseInt(sp1);
                return sp2;
            }
            if(x<0)
            {
                int x1= -x;
                String sp = Integer.toString(x1);
                //String sp1 = sp.reverse();
                String sp1 = new StringBuffer(sp).reverse().toString();
                int sp2 = Integer.parseInt(sp1);
                int sp3=-sp2;
                return sp3;
            }
             
        }
        return 0;
        
    }
}