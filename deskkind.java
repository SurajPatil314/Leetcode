//In a deck of cards, each card has an integer written on it.

//Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

//Each group has exactly X cards.
//All the cards in each group have the same integer.

class Solution {
    public boolean hasGroupsSizeX(int[] deck) {
    
    if(deck.length<2 )
    {
        return false;
    }   
    else
    {
        
      
        
        Set<Integer> num=new HashSet<Integer>();
        List<Integer> zero= new ArrayList<Integer>();
        List<Integer> one= new ArrayList<Integer>();
        List<Integer> two= new ArrayList<Integer>();
        List<Integer> three= new ArrayList<Integer>();
        List<Integer> four= new ArrayList<Integer>();
        List<Integer> five= new ArrayList<Integer>();
        List<Integer> six= new ArrayList<Integer>();
        List<Integer> seven= new ArrayList<Integer>();
        List<Integer> eight= new ArrayList<Integer>();
        List<Integer> nine= new ArrayList<Integer>();
        List<Integer> ten= new ArrayList<Integer>();
        List<Integer> ele= new ArrayList<Integer>();
        List<Integer> twel= new ArrayList<Integer>();
        List<Integer> thir= new ArrayList<Integer>();
        
        for(int i=0; i<deck.length; i++)
        {
            if(deck[i]==0)
            {
                num.add(deck[i]);
                zero.add(deck[i]);
            }
            if(deck[i]==1)
            {
                num.add(deck[i]);
                one.add(deck[i]);
            }
            if(deck[i]==2)
            {
                num.add(deck[i]);
                two.add(deck[i]);
            }
            if(deck[i]==3)
            {
                num.add(deck[i]);
                three.add(deck[i]);
            }
            if(deck[i]==4)
            {
                num.add(deck[i]);
                four.add(deck[i]);
            }
            if(deck[i]==5)
            {
                num.add(deck[i]);
                five.add(deck[i]);
            }
            if(deck[i]==6)
            {
                num.add(deck[i]);
                six.add(deck[i]);
            }
            if(deck[i]==7)
            {
                num.add(deck[i]);
                seven.add(deck[i]);
            }
            if(deck[i]==8)
            {
                num.add(deck[i]);
                eight.add(deck[i]);
            }
            if(deck[i]==9)
            {
                num.add(deck[i]);
                nine.add(deck[i]);
            }
            if(deck[i]==9)
            {
                num.add(deck[i]);
                nine.add(deck[i]);
            }
            if(deck[i]==10)
            {
                num.add(deck[i]);
                ten.add(deck[i]);
            }
            if(deck[i]==11)
            {
                num.add(deck[i]);
                ele.add(deck[i]);
            }
            if(deck[i]==12)
            {
                num.add(deck[i]);
                twel.add(deck[i]);
            }
            if(deck[i]==13)
            {
                num.add(deck[i]);
                thir.add(deck[i]);
            }
        }
        
        System.out.println("numbers present::"+num.size());
        int[] i = new int[14];
        i[0] = zero.size();
        
        i[1] = one.size();
        i[2] = two.size();
        i[3] = three.size();
        i[4] = four.size();
        i[5] = five.size();
        i[6] = six.size();
        i[7] = seven.size();
        i[8] = eight.size();
        i[9] = nine.size();
        i[10] = ten.size();
        i[11] = ele.size();
        i[12] = twel.size();
        i[13] = thir.size();
        int q=1;
        for(int j1=0; j1<14; j1++)
        {
            if(i[j1]>0)
            {
                q=i[j1];
                break;
            }
        }
        
        
            
        
        for(int j=0; j<14; j++)
        {
           
                if(i[j]!=0 )
                {
                    
                    if(q>i[j])
                    {
                        q=i[j];
                    }
                }
            
        }
        System.out.println("lowest count"+q);
        if(q==1)
        {
            return false;
        }
        for(int i1=2; i1<=q;i1++)
        {
            if(q%i1==0)
            {
                q=i1;
                break;
            }
        }
      if(zero.size()==0 || zero.size()%q==0)   
      {
          
          System.out.println("zero cleared with size");
        if(one.size()==0 || one.size()%q==0)
        {
           
             System.out.println("one cleared with size");
            if(two.size()==0 || two.size()%q==0)
            {
                System.out.println("two cleared with size");
                 if(three.size()==0 || three.size()%q==0)
                 {   System.out.println("three cleared");
                      if(four.size()==0 || four.size()%q==0)
                      {  System.out.println("four cleared");
                           if(five.size()==0 || five.size()%q==0)
                           {    System.out.println("five cleared");
                                if(six.size()==0 || six.size()%q==0)
                                {   System.out.println("six cleared");
                                     if(seven.size()==0 || seven.size()%q==0)
                                     {   System.out.println("seven cleared");
                                          if(eight.size()==0 || eight.size()%q==0)
                                          {   System.out.println("eight cleared");
                                               
                                               if(nine.size()==0 || nine.size()%q==0)
                                               {
                                                   System.out.println("nine cleared");
                                                    if(ten.size()==0 || ten.size()%q==0)
                                                    {
                                                        System.out.println("ten cleared");
                                                        if(ele.size()==0 || ele.size()%q==0)
                                                        {
                                                            System.out.println("ele cleared");
                                                            if(twel.size()==0 || twel.size()%q==0)
                                                        {
                                                            System.out.println("twel cleared");
                                                                if(thir.size()==0 || thir.size()%q==0)
                                                        {
                                                            System.out.println("thir cleared");
                                                                    return true;
                                                        
                                                         }
                                                        
                                                         }
                                                        
                                                         }
                                                        
                                                    }
                                                  
                                                   
                                               }
        }
      }
                                }            }}}}}}
     
              return false;
        
        
        
   
        
        
    }
    
    }
}