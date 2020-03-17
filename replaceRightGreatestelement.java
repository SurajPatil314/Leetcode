
/*
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
*/
class Solution {
    public int[] replaceElements(int[] arr) {

        if(arr.length==0){
            return arr;
        }
        if(arr.length==1){
            arr[0] = -1;
            return arr;
        }

        int gretest = arr[arr.length-1];

        for(int i = arr.length-2;i>=0;i--){
            if(i==arr.length-2){

                if(arr[i] > gretest){
                    gretest = arr[i];
                }
                arr[arr.length-2] = arr[arr.length-1];
            }
            else{
                int temp = arr[i];
                    arr[i]= gretest;
                if(temp>gretest){
                gretest = temp;
                }
            }

        }
        arr[arr.length-1] =-1;
        return arr;

    }
}