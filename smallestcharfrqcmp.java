/*
Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.
*/
 


class Solution {
    public int[] numSmallerByFrequency(String[] queries, String[] words) {
        
        //List<Integer> ansset=new ArrayList<Integer>();  
        int[] ansset = new int[queries.length];
        int[] wordfrqarray = new int[words.length];
        
        for(int i=0; i<words.length; i++)
        {
            String str2 = words[i];
            char min=str2.charAt(0);
            int fr1=0;
            for(int i1=0;i1<str2.length();i1++)
            {
                char ch1=str2.charAt(i1);
                
                if(ch1<min){min=ch1;}
                
            }
            for(int i1=0;i1<str2.length();i1++)
            {
                if(min==str2.charAt(i1))
                {
                    fr1++;
                }
                
            }
            
            wordfrqarray[i]=fr1;
            
        }
        
        for(int o=0; o<wordfrqarray.length; o++)
        {
            System.out.println("frequecies::"+wordfrqarray[o]);
        }
        
        for(int i=0; i<queries.length; i++)
        {
            String str1 = queries[i];
            
            
            char max='z';
            char min=str1.charAt(0);;
            
            
            //get lowest char
            for(int i1=0;i1<str1.length();i1++)
            {
                char ch1=str1.charAt(i1);
                
                if(ch1<min){min=ch1;}
                
            }
            
            //get lowest char freq
            int fr1=0;
            
            for(int i1=0;i1<str1.length();i1++)
            {
                if(min==str1.charAt(i1))
                {
                    fr1++;
                }
                
            }         
            System.out.println("min char frequency::"+fr1);
            
            int diffcount=0;
            for(int o=0; o<wordfrqarray.length; o++)
            {
                if(fr1<wordfrqarray[o])
                {
                    diffcount++;
                }
            }
            
            ansset[i]=diffcount;
            
            
        }
        
        return ansset;
        
    }
}