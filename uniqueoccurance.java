/*
Given an array of integers arr, write a function that returns true if and only if the number of occurrences
 of each value in the array is unique.
*/

class Solution {
    public boolean uniqueOccurrences(int[] arr) {

        HashMap<Integer, Integer> occ = new HashMap<Integer, Integer>();

        ArrayList<Integer> occ1= new ArrayList<Integer>();


        for(int i=0; i<arr.length; i++)
        {
            if (occ.containsKey(arr[i]))
            {
                occ.put(arr[i], occ.get(arr[i]) + 1);
            }
            else
            {
                occ.put(arr[i], 1);
            }
        }


        for (Map.Entry<Integer, Integer> item : occ.entrySet()) {
            Integer value = item.getValue();

            if(occ1.contains(value))
            {
                return false;
            }
            else
            {
                occ1.add(value);
            }
            }

        return true;

    }
}