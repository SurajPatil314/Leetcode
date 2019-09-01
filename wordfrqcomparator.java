/*
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
*/

class Solution {
    public int countCharacters(String[] words, String chars) {
        int fanswer=0;
        
        HashMap<Character, Integer> charsschar = new HashMap<Character, Integer>();
        
        if(chars.length()==0 || words.length==0)
        {
            return 0;
        }
        
        char[] strArray = chars.toCharArray(); 
        
          for (char c : strArray) { 
            if (charsschar.containsKey(c)) { 
                charsschar.put(c, charsschar.get(c) + 1); 
            } 
            else { 
                charsschar.put(c, 1); 
            } 
        }
        
        for(int i=0;i<words.length;i++)
        {
            String word1= words[i];
            
            
            HashMap<Character, Integer> wordschar = new HashMap<Character, Integer>();
            
            int addans= word1.length();
            
            char[] strArray1 = word1.toCharArray(); 
            
            for (char c : strArray1) { 
                if (wordschar.containsKey(c)) { 
                    wordschar.put(c, wordschar.get(c) + 1); 
                } 
                else { 
                    wordschar.put(c, 1); 
                } 
            }
            
            int ui=0;
            for (Map.Entry<Character, Integer> item : wordschar.entrySet()) {
                char key = item.getKey();
                int value = item.getValue();
                
                if(charsschar.containsKey(key))
                {
                    if(charsschar.get(key)>=value)
                    {
                        ui=1;
                    }
                    else
                    {
                        ui=0;
                        break;
                    }
                }
                else
                {
                    ui=0;
                    break;
                }
            }
            
            if(ui==1)
            {
                fanswer=fanswer+addans;
            }
            
            
            
        }
        
        return fanswer;
        
    }
}