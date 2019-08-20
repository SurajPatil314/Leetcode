class Solution {
    public int numUniqueEmails(String[] emails) {
        
        List<String> q= new ArrayList<String>();
        StringBuilder sb = new StringBuilder();
        String s1;
        int r=0;
        int answer=0;
        
        for(String s:emails)
        {
            char[] q1 = s.toCharArray();
            s1="";
            sb.setLength(0);
            r=0;
		    for (char w : q1) {
                
                if(w=='+' && r!=2)
                {
                    r=1;
                }
                else if(w=='@')
                {
                    r=2;
                   // s1.add(Character.toString(w));
                    sb.append(w);
                }
                else if(w=='.' && r==0)
                {
                    continue;
                }
                else
                {
                   // s1.add(Character.toString(w));
                    if(r!=1)
                    {
                        sb.append(w);
                    }
                    
                }
                
		    }
            
            s1 = sb.toString();
            if(q.contains(s1))
            {
            }
            else
            {
                answer++;
                q.add(s1);
                System.out.println("ans::"+answer);
                System.out.println("ans string::"+s1);
                
            }
            
        }
        return answer;
    }
}