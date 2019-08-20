class Solution {
    public boolean isHappy(int n) {
    int nq;
     int count =100;
        while (n != 1&& count!=0)
        {
             nq=0;
            int qw=0;
            List<Integer> list = new ArrayList<>();
            
       while (n!=0)
       {
            list.add( n % 10 );
            n = n / 10;
           System.out.println("n first"+n);
       }

 System.out.println("list size"+list.size());
for (Integer s : list)
{       
        nq= nq+s*s;
          
            }   
            System.out.println("nq:"+nq); 
       n=nq; 
       count--;
    }
        System.out.println("count::"+count);
        if(n==1)
            return true;
         
        else if(count==0)
            return false;
        else
            return false;
    }
}