/*
https://leetcode.com/problems/teemo-attacking/

In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.
*/

class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {

        int end = 0;
        int total = 0;
        for(int i = 0 ; i<timeSeries.length; i++){

            if(i==0){
                end =timeSeries[i]+duration-1;
                total = end-timeSeries[i]+1;
            }
            else{

                if(timeSeries[i]>end){
                    end =timeSeries[i]+duration-1;
                    total =total+(end-timeSeries[i]+1);

                }
                else{
                    total =total+(timeSeries[i]+duration-1-end);
                    end =timeSeries[i]+duration-1;


                }
            }


        }

        return total;

    }
}