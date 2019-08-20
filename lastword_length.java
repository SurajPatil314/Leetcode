class Solution {
    public int lengthOfLastWord(String s) {
        if(s!=null)
        {
            String last="";
           String[] words=s.split("\\W+");
            for(int i=0;i<words.length;i++)
            {
                last=words[i];
            }
            int le= last.length();
            return le;
        }
        return 0;
        
    }
}