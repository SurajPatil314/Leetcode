class Solution {
    public boolean isAnagram(String s, String t) {
        
        if(s != null && !s.isEmpty())
        {
           if(t != null && !t.isEmpty())
           {
               int b=0;           
               char[] input1 = s.toCharArray();
               char[] input2 = t.toCharArray();
               // System.out.println(input1[1]);
               //System.out.println(input2[1]);
               for (char x : input1) {
                   do
                   {
                        for (char y : input2){
                            if (x == y) {
                            b=1;
                            }
                   }
                    }while(b==1);
               
                }
               if(b==1)
                return true;
               else
                   return false;
           } 
          else
           {
            System.out.println("input string is empty");
            return false;
           }
        
        }
        else
        {
            System.out.println("input string is empty");
            return false;
        }
    }
}