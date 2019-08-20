class Solution {
    public boolean stoneGame(int[] piles) {
        
        Deque<Integer> deque = new LinkedList<Integer>(); 
        
         List<Integer> l1 = new ArrayList<Integer>(); 
         List<Integer> l2 = new ArrayList<Integer>(); 
        
        int first, last;
        int alexchance=1;
        
        if(piles.length==0)
        {
            return true;
        }
        else
        {
            for(int i=0;i<piles.length;i++)
            {
                deque.add(piles[i]);
            }
            
            
            
            while(deque.size()>0)
            {
                if(alexchance==1)
                {
                     if(deque.getFirst()>deque.getLast())
                     {
                         System.out.println("alexchance deque.getFirst() "+deque.getFirst());
                         l1.add(deque.getFirst());
                         deque.removeFirst();    
                         alexchance=0;
                         System.out.println(" deque.:: "+deque);
                     }
                    else
                    {
                        System.out.println("alexchance deque.getLast() "+deque.getLast());
                        l1.add(deque.getLast());
                        deque.removeLast();
                        alexchance=0;
                        System.out.println(" deque:: "+deque);
                    }
                }
                else
                {
                    if(deque.getFirst()>deque.getLast())
                     {
                         System.out.println("Lee deque.getLast() "+deque.getFirst());
                         l2.add(deque.getFirst());
                         deque.removeFirst();   
                         alexchance=1;
                        System.out.println("deque::"+deque);
                     }
                    else
                    {
                        System.out.println("Lee deque.getLast() "+deque.getLast());
                        l2.add(deque.getLast());
                        deque.removeLast();
                        alexchance=1;
                        System.out.println("deque::"+deque);
                    }
                    
                }
                 
               
            }
            
            int sum1 = l1.stream().mapToInt(Integer::intValue).sum();
            int sum2 = l2.stream().mapToInt(Integer::intValue).sum();
            
            System.out.println("sum1::"+sum1);
            System.out.println("sum2::"+sum2);
            
            if(sum1>sum2)
            {
                return true;
            }
            else
            {
                return false;
            }
        
       
            
        }
        
        
        
    }
}