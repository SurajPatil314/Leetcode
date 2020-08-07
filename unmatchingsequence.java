/*
https://leetcode.com/problems/number-of-matching-subsequences/

Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.
*/

class Solution {
    public int numMatchingSubseq(String S, String[] words) {
        int ans = 0;

        ArrayList<String> accp = new ArrayList<String>();
        ArrayList<String> naccp = new ArrayList<String>();


        for(int i=0; i <words.length; i++){

            if(accp.contains(words[i])){
                ans++;

            }
            else if(naccp.contains(words[i])){
                ans = ans;

            }
            else{
                int j = 0;
            int k = 0;
            int temp = 0;


            String word1 = words[i];

            while(j<words[i].length() && k<S.length()){
                 if(word1.charAt(j) == S.charAt(k)){
                     j++;
                     k++;

                     if(j == words[i].length()){
                        ans++;
                        temp = 1;
                        break;
                     }
                    }

                else{
                    k++;
                }

            }

            if(temp == 1){
                accp.add(words[i]);
            }
            else{
                 naccp.add(words[i]);
            }

            }
        }

        return ans;

    }
}