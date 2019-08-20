class Solution {
    public int myAtoi(String str) {
        
        
        int h=0;
        ArrayList<String> qw4= new ArrayList<String>();
        for (int i = 0; i < str.length(); i++)
        {
            if(h==0)
            {
                if(Character.isWhitespace(str.charAt(i)))
                {
                        continue;
                }
                else
                {
                    qw4.add(String.valueOf(str.charAt(i)) );
                    h=1;
                }
            }
            else
            {
                qw4.add(String.valueOf(str.charAt(i)) );
            }
            
            
        }
        
        String str1 = String.join("", qw4);
        
        ArrayList<String> qw= new ArrayList<String>();
        
        for (int i = 0; i < str1.length(); i++) {
			
            
            if(i==0)
            {
                System.out.print(str1.charAt(i));
                
                if(str1.charAt(i)=='+') 
                {
                    System.out.println("OOOO "+str1.charAt(i));
                      
                }
                else
                {
                    if(str1.charAt(i)!='-') 
                    {
                       if(Character.isDigit(str1.charAt(i))) {
                            System.out.println("QQQ "+str1.charAt(i));
                            int result = Character.getNumericValue(str1.charAt(i));
                            qw.add(String.valueOf(result) );
                        }

                        else{

                            System.out.println("AAA "+str1.charAt(i));
                            break;
                        }

                    }
                    else
                    {
                        System.out.println("XXX "+str1.charAt(i));
                        qw.add(String.valueOf(str1.charAt(i)) );
                        
                    }
                }
                
               
            }
            else
            {
                if(Character.isDigit(str1.charAt(i)))
                {
                    System.out.println("PPP "+str1.charAt(i));
                    qw.add(String.valueOf(str1.charAt(i)) );
                }
                else
                {
                    break;
                }
                
            }
		}
        /*
        StringBuilder sb = new StringBuilder();
        for (String s : list)
        {
            sb.append(s);
            sb.append("\t");
        }
        */
        
        if(qw.size()==0)
        {
            return 0;
        }
        else
        {
            ArrayList<String> qw1= new ArrayList<String>();
            
            int p=0;
            
            for(String y:qw)
            {
                
                if(y.equals("-"))
                {
                    qw1.add(y);
                }
                else
                {
                    if(p==0)
                    {
                        if(y.equals("0"))
                        {
                    
                            continue;
                        }
                        else
                        {                                                    
                            qw1.add(y);
                            p=1;
                            
                        }
                    }
                    else
                    {
                        qw1.add(y);
                    }
               
                }
                
                
            }
            
            System.out.println("ttttt::"+qw1);
            
            if(qw1.size()==0)
            {
                return 0;
            }
            if(qw1.size()>11)
            {
                System.out.println("uiuiui");
                System.out.println(qw1.get(0));
                
                if (qw1.get(0).equals("-"))
                {
                    System.out.println("opopop");
                    return Integer.MIN_VALUE;
                }
                else
                {
                    System.out.println("nmnmnm");
                    return Integer.MAX_VALUE;
                }
            }
            
            
            String listString = String.join("", qw1);
            System.out.println("MMM::"+listString);
            
            
            
            if(listString.equals("-"))
            {
                System.out.println("ioio");
                return -0;
            }
            else if(listString.equals("+"))
            {
                return +0;
            }
            else
            {
                Long ans= Long.parseLong(listString);
                if(ans<Integer.MIN_VALUE)
            {
               return Integer.MIN_VALUE;
            }
            else if(ans>Integer.MAX_VALUE)
            {
                return Integer.MAX_VALUE;
            }
            else
            {
                int ans1= Integer.parseInt(listString);
                return ans1;
            }
                
            }
                
            
        }
        
            
        
        
        
    }
}