class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        if(strs.length>1)
        {
            String character = "";
            char s2;
            String s3;
            String otherString = "helen";
            otherString=otherString+character;
            int count=0;
            String first = strs[0];
            System.out.println(first);
            
            for(int i=1; i<strs.length; i++ )
            {
                String sec = strs[i];
                character="";
                for(int j=0;j<first.length() && j<sec.length();j++)
                {
                    
                    if(first.charAt(j)==sec.charAt(j))
                    {
                        count++;
                        s2=first.charAt(j);
                        s3=String.valueOf(s2);
                        character = character +s3;
                    }
                    if(count==0)
                    {
                        break;
                    }
                    
                }
                if(count==0)
                {
                    return "";
                }
                return character;
            }
            
            
        }
        return null;
        
    }
}