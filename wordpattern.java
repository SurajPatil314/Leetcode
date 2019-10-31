/*
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
*/

class Solution {
    public boolean wordPattern(String pattern, String str) {

        HashMap<Character, String> cmap = new HashMap<Character, String>();

        ArrayList<String> sep2 = new ArrayList<String>();

        String[] sep1 = str.split(" ");
        List<String> sep = Arrays.asList(sep1);


        if(pattern.length()!= sep.size())
        {
            return false;
        }

        for (int i = 0; i < pattern.length(); i++) {
			System.out.print(pattern.charAt(i));

            if (cmap.containsKey(pattern.charAt(i))) {

                if(cmap.get(pattern.charAt(i)).equals(sep.get(i)))
                {

                }
                else
                {
                    return false;
                }

            }
            else
            {
                if(sep2.contains(sep.get(i)))
                {
                    return false;
                }
                else
                {
                    sep2.add(sep.get(i));
                }
                cmap.put(pattern.charAt(i), sep.get(i));
                sep2.add(sep.get(i));
            }
		}

        return true;

    }
}